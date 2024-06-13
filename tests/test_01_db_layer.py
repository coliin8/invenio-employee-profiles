from invenio_employee_profiles.records.models import EmployeeProfileModel


def test_db_create(app, db, users, employee_profile_data, search_clear):
    u, data = employee_profile_data
    profile = EmployeeProfileModel(json=data, user_id=u.id, active=True)
    db.session.add(profile)
    db.session.commit()
    profile_id = profile.id

    created_profile = EmployeeProfileModel.query.get(profile_id)

    # db.session.expunge_all()

    assert profile_id is not None

    assert created_profile.user_id == u.id
    assert created_profile.json == data
    assert created_profile.active == True
