# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Test files resource integration."""

from io import BytesIO

import pytest

from invenio_employee_profiles.files.models import EmployeeProfileFileModel
from invenio_employee_profiles.records.models import EmployeeProfileModel

# @pytest.fixture()
# def published_id(authenticated_client, employee_profile_data, location, headers):
#     """A published record."""
#     h = headers
#     u, data = employee_profile_data
#     # Create a draft
#     res = authenticated_client.post('/employee-profiles', json={
#         **data,
#         'active': True,
#         'user': {
#             'id': str(u.id),
#         }
#     })
#     assert res.status_code == 201
#     id_ = res.json["id"]

#     # Initialize files upload
#     res = authenticated_client.post(
#         f"/employee-profiles/{id_}/files", headers=h, json=[{"key": "test.pdf"}]
#     )
#     assert res.status_code == 201
#     assert res.json["entries"][0]["key"] == "test.pdf"
#     assert res.json["entries"][0]["status"] == "pending"

#     # Upload a file
#     res = authenticated_client.put(
#         f"/employee-profiles/{id_}/files/test.pdf/content",
#         headers={"content-type": "application/octet-stream"},
#         data=BytesIO(b"testfile"),
#     )
#     assert res.status_code == 200

#     # Commit the file
#     res = authenticated_client.post(f"/employee-profiles/{id_}/files/test.pdf/commit", headers=h)
#     assert res.status_code == 200
#     assert res.json["key"] == "test.pdf"
#     assert res.json["status"] == "completed"

#     # Publish the record
#     res = authenticated_client.post(f"/employee-profiles/{id_}/actions/publish", headers=h)
#     assert res.status_code == 202

#     return id_


def test_files_publish_flow(
    authenticated_client,
    employee_profile_data,
    search_clear,
    location,
    headers,
    db
):
    """Test record creation."""
    h = headers
    u, data = employee_profile_data
    # Create a draft
    res = authenticated_client.post('/employee-profiles', json={
        **data,
        'active': True,
        'user': {
            'id': str(u.id),
        }
    })
    assert res.status_code == 201
    id_ = res.json["id"]
    # Initialize files upload
    res = authenticated_client.post(
        f"/employee-profiles/{id_}/files", headers=h, json=[{"key": "test.pdf"}]
    )
    assert res.status_code == 201
    assert res.json["entries"][0]["key"] == "test.pdf"
    assert res.json["entries"][0]["status"] == "pending"

    # Upload a file
    res = authenticated_client.put(
        f"/employee-profiles/{id_}/files/test.pdf/content",
        headers={"content-type": "application/octet-stream"},
        data=BytesIO(b"testfile"),
    )
    assert res.status_code == 200

    # Commit the file
    res = authenticated_client.post(f"/employee-profiles/{id_}/files/test.pdf/commit", headers=h)
    assert res.status_code == 200
    assert res.json["key"] == "test.pdf"
    assert res.json["status"] == "completed"

    # Check published files
    res = authenticated_client.get(f"/employee-profiles/{id_}/files", headers=h)
    assert res.status_code == 200
    assert res.json["entries"][0]["key"] == "test.pdf"
    assert res.json["entries"][0]["status"] == "completed"

    # Test Database to see connection
    epm = EmployeeProfileModel.query.get(id_)
    epfm = EmployeeProfileFileModel.query.filter(EmployeeProfileFileModel.record_id == epm.id).all()
    assert epfm[0].record_id == epm.id


    # Edit the record
    # res = client.post(f"/mocks/{id_}/draft", headers=h)
    # assert res.status_code == 201

    # # Publish again
    # res = client.post(f"/mocks/{id_}/draft/actions/publish", headers=h)
    # assert res.status_code == 202

    # # Check published files
    # res = authenticated_client.get(f"/employee-profiles/{id_}/files", headers=h)
    # assert res.status_code == 200
    # assert res.json["entries"][0]["key"] == "test.pdf"
    # assert res.json["entries"][0]["status"] == "completed"


# def test_import_files(client, search_clear, location, headers, published_id):
#     """Test import files from previous version."""
#     h = headers
#     id_ = published_id

#     # New version
#     res = client.post(f"/mocks/{id_}/versions", headers=h)
#     assert res.status_code == 201
#     new_id = res.json["id"]

#     # Check new version files
#     res = client.get(f"/mocks/{new_id}/draft/files", headers=h)
#     assert res.status_code == 200
#     assert len(res.json["entries"]) == 0

#     # Import files from previous version
#     res = client.post(f"/mocks/{new_id}/draft/actions/files-import", headers=h)
#     assert res.status_code == 201
#     assert res.content_type == "application/json"

#     # Check new version files
#     res = client.get(f"/mocks/{new_id}/draft/files", headers=h)
#     assert res.status_code == 200
#     assert len(res.json["entries"]) == 1


# def test_import_files_metadata_only(client, search_clear, location, headers):
#     """Test import files from previous version."""
#     h = headers

#     res = client.post(
#         "/mocks",
#         headers=h,
#         json={"metadata": {"title": "Test"}, "files": {"enabled": False}},
#     )
#     assert res.status_code == 201
#     id_ = res.json["id"]

#     # Publish
#     res = client.post(f"/mocks/{id_}/draft/actions/publish", headers=h)
#     assert res.status_code == 202

#     # New version
#     res = client.post(f"/mocks/{id_}/versions", headers=h)
#     assert res.status_code == 201
#     new_id = res.json["id"]

#     # Check new version files
#     res = client.get(f"/mocks/{new_id}/draft/files", headers=h)
#     assert res.status_code == 200
#     assert "entries" not in res.json

#     # Import files from previous version
#     res = client.post(f"/mocks/{new_id}/draft/actions/files-import", headers=h)
#     assert res.status_code == 400


# def test_import_files_no_version(client, search_clear, location, headers):
#     """Test import files from previous version."""
#     h = headers

#     res = client.post(
#         "/mocks",
#         headers=h,
#         json={"metadata": {"title": "Test"}, "files": {"enabled": True}},
#     )
#     assert res.status_code == 201
#     id_ = res.json["id"]

#     # Cannot import files from a non-existing previous version
#     res = client.post(f"/mocks/{id_}/draft/actions/files-import", headers=h)
#     assert res.status_code == 404
