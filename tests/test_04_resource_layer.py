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
            "user": {'id': '1',
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
