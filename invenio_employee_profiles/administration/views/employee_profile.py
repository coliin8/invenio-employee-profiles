from invenio_administration.views.base import (
    AdminResourceListView,
    AdminResourceCreateView,
    AdminResourceEditView,
    AdminResourceDetailView
)


class EmployeeProfileListView(AdminResourceListView):
    """Configuration for OAI-PMH sets list view."""

    api_endpoint = "/employee-profiles"
    name = "Employee Profiles"
    resource_config = "records_resource"
    search_request_headers = {"Accept": "application/json"}
    title = "Employee Profile Sets"
    category = "Site management"
    pid_path = "id"
    icon = "exchange"
    # template = "invenio_rdm_records/oai-search.html"

    display_search = True
    display_delete = True
    display_edit = True

    item_field_list = {
        "email_address": {"text": "Set name", "order": 1},
        "search_pattern": {"text": "Search query", "order": 2},
        "created": {"text": "Created", "order": 3},
        "updated": {"text": "Updated", "order": 4},
    }

    search_config_name = "EMPLOYEE_PROFILE_SEARCH"
    search_facets_config_name = "EMPLOYEE_PROFILE_FACETS"
    search_sort_config_name = "EMPLOYEE_PROFILE_SORT_OPTIONS"

    create_view_name = "employee_profile_create"
    resource_name = "email_address"


class EmployeeProfileCreateView(AdminResourceCreateView):
    """Configuration for Employee Profile sets create view."""

    name = "employee_profile_create"
    url = "/employee-profiles-admin/create"
    resource_config = "records_resource"
    pid_path = "id"
    api_endpoint = "/employee-profiles"
    title = "Create Employee Profile"

    list_view_name = "Employee Profiles"

    form_fields = {
        "email_address": {"text": "Set name", "order": 1},
        "search_pattern": {"text": "Search query", "order": 2},
        "created": {"text": "Created", "order": 3},
        "updated": {"text": "Updated", "order": 4},
    }


class EmployeeProfileEditView(AdminResourceEditView):
    """Configuration for OAI-PMH sets edit view."""

    name = "employee_profile_edit"
    url = "/employee-profiles-admin/<pid_value>/edit"
    resource_config = "records_resource"
    pid_path = "id"
    api_endpoint = "/employee-profiles"
    title = "Edit OAI-PMH set"

    list_view_name = "Employee Profiles"

    form_fields = {
        "email_address": {"text": "Set name", "order": 1},
        "search_pattern": {"text": "Search query", "order": 2},
        "created": {"text": "Created", "order": 3},
        "updated": {"text": "Updated", "order": 4},
    }


class EmployeeProfileDetailView(AdminResourceDetailView):
    """Configuration for OAI-PMH sets detail view."""

    url = "/employee-profiles-admin/<pid_value>"
    api_endpoint = "/employee-profiles"
    search_request_headers = {"Accept": "application/json"}
    name = "Employee Profile details"
    resource_config = "records_resource"
    title = "Employee Profile Details"

    # template = "invenio_rdm_records/oai-details.html"
    display_delete = True
    display_edit = True

    list_view_name = "Employee Profiles"
    pid_path = "id"

    item_field_list = {
        "email_address": {"text": "Set name", "order": 1},
        "search_pattern": {"text": "Search query", "order": 2},
        "created": {"text": "Created", "order": 3},
        "updated": {"text": "Updated", "order": 4},
    }