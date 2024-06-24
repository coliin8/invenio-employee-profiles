from flask import current_app, g, render_template


def employee_profiles_search():
    """Employee Profiles search page."""
    return render_template(
        # This seems to point to invenio_employee_profiles/templates/semantic-ui/invenio_employee_profiles/search.html
        "invenio_employee_profiles/search.html",
    )