from flask import g, render_template

from ..proxies import current_profiles


def employee_profiles_search():
    """Employee Profiles search page."""
    can_create = current_profiles.records_service.check_permission(g.identity, "create")
    return render_template(
        # This seems to point to invenio_employee_profiles/templates/semantic-ui/invenio_employee_profiles/search.html
        "invenio_employee_profiles/search.html",
        permissions=dict(can_create=can_create),
    )
