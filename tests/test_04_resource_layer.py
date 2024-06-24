from io import BytesIO


def test_resource(app, db, users, search_clear, search, employee_profile_data, location, authenticated_client):
    u, data = employee_profile_data

    # Create
    with authenticated_client.post('/employee-profiles', json={
        **data,
        'active': True,
        'user': {
            'id': str(u.id),
        }
    }) as response:
        assert response.status_code == 201
        assert response.json.items() >= {
            "email_address": "johndoe@example.com",
            "biography": "John Doe is a software engineer with over 10 years of experience in the tech industry. He specializes in backend development, particularly with Python and Django. He has a passion for clean, efficient code and enjoys working on complex, challenging problems.",
            "profile_image": "https://example.com/johndoe.png",
            "active": True,
            "user": {
                'id': '1',
                'identities': {},
                'is_current_user': True,
                'links': {},
                'profile': {'affiliations': 'CERN', 'full_name': 'Tim Smith'},
                'username': 'pubres'
            }
        }.items()
        id_ = response.json['id']

    with authenticated_client.get(f'/employee-profiles/{id_}') as response:
        assert response.status_code == 200

    # Update Record
    data["email_address"] = "jakecollins1976@gmail.com"
    with authenticated_client.put(f'/employee-profiles/{id_}', json={
        **data,
        'active': True,
        'user': {
            'id': str(u.id),
        }
    }) as response:
        assert response.json["email_address"] == "jakecollins1976@gmail.com"
        assert response.status_code == 200

    # Delete Record
    with authenticated_client.delete(f'/employee-profiles/{id_}') as response:
        assert response.status_code == 204

    # No Longer exists
    with authenticated_client.get(f'/employee-profiles/{id_}') as response:
        assert response.status_code == 404


def test_logo_flow(
    app, db, users, search_clear, search, employee_profile_data, location, authenticated_client, headers
):
    """Test logo workflow."""
    u, data = employee_profile_data

    # Create an employee Profile
    res = authenticated_client.post(
        '/employee-profiles',
        json={
            **data,
            'active': True,
            'user': {
                'id': str(u.id),
            }
        }
    )
    assert res.status_code == 201
    created_ep = res.json
    id_ = created_ep["id"]

    assert (
        created_ep["links"]["logo"]
        == f"https://127.0.0.1:5000/api/employee-profiles/{id_}/logo"
    )

    # Get non-existent logo
    res = authenticated_client.get(f"/employee-profiles/{id_}/logo")
    assert res.status_code == 404
    assert res.json["message"] == "No logo exists for this community."

    # Delete non-existent logo
    res = authenticated_client.delete(f"/employee-profiles/{id_}/logo", headers=headers)
    assert res.status_code == 404
    assert res.json["message"] == "No logo exists for this community."

    # Update logo
    res = authenticated_client.put(
        f"/employee-profiles/{id_}/logo",
        headers={
            **headers,
            "content-type": "application/octet-stream",
        },
        data=BytesIO(b"logo"),
    )
    assert res.status_code == 200
    assert res.json["size"] == 4

    # Get logo
    res = authenticated_client.get(f"/employee-profiles/{id_}/logo")
    assert res.status_code == 200
    assert res.data == b"logo"

    # Update logo again
    res = authenticated_client.put(
        f"/employee-profiles/{id_}/logo",
        headers={
            **headers,
            "content-type": "application/octet-stream",
        },
        data=BytesIO(b"new_logo"),
    )
    assert res.status_code == 200
    assert res.json["size"] == 8

    # Get new logo
    res = authenticated_client.get(f"/employee-profiles/{id_}/logo")
    assert res.status_code == 200
    assert res.data == b"new_logo"

    # Delete logo with unauthorized user
    with app.test_client() as anon_client:
        res = anon_client.delete(f"/employee-profiles/{id_}/logo", headers=headers)
        assert res.status_code == 403

    # Delete logo
    res = authenticated_client.delete(f"/employee-profiles/{id_}/logo", headers=headers)
    assert res.status_code == 204

    # Try to get deleted logo
    res = authenticated_client.get(f"/employee-profiles/{id_}/logo")
    assert res.status_code == 404
    assert res.json["message"] == "No logo exists for this community."

    # TODO: Delete community and try all of the above operations


def test_logo_max_content_length(
     app, db, users, search_clear, search, employee_profile_data, location, authenticated_client, headers
):
    """Test logo max size."""
    u, data = employee_profile_data

    # Create an employee Profile
    res = authenticated_client.post(
        '/employee-profiles',
        json={
            **data,
            'active': True,
            'user': {
                'id': str(u.id),
            }
        }
    )
    assert res.status_code == 201
    created_ep = res.json
    id_ = created_ep["id"]
    assert (
        created_ep["links"]["logo"]
        == f"https://127.0.0.1:5000/api/employee-profiles/{id_}/logo"
    )

    # Update app max size for community logos
    max_size = 10**6
    app.config["EMPLOYEE_PROFILES_LOGO_MAX_FILE_SIZE"] = max_size

    # Update logo with big content
    logo_data = b"logo" * (max_size + 1)
    res = authenticated_client.put(
        f"/employee-profiles/{id_}/logo",
        headers={
            **headers,
            "content-type": "application/octet-stream",
        },
        data=BytesIO(logo_data),
    )
    assert res.status_code == 400

    # Update logo with small content
    logo_data = b"logo"
    res = authenticated_client.put(
        f"/employee-profiles/{id_}/logo",
        headers={
            **headers,
            "content-type": "application/octet-stream",
        },
        data=BytesIO(logo_data),
    )
    assert res.status_code == 200
