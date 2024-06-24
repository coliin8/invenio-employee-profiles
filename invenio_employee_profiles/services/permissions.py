"""Permissions for Employeee Profile service functions."""

from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import AnyUser, SystemProcess, AuthenticatedUser

from invenio_records_resources.services.files.generators import AnyUserIfFileIsLocal


class EmployeeProfilePermissionPolicy(RecordPermissionPolicy):
    """Employee Profile Permission Policy class."""

    can_search = [AnyUser(), SystemProcess()]
    can_create = [AuthenticatedUser(), SystemProcess()]
    can_update = [AuthenticatedUser(), SystemProcess()]
    can_delete = [AuthenticatedUser(), SystemProcess()]
    can_read = [AnyUser(), SystemProcess()]
    can_create_files = [AnyUser(), SystemProcess()]
    can_set_content_files = [AnyUserIfFileIsLocal(), SystemProcess()]
    can_get_content_files = [AnyUserIfFileIsLocal(), SystemProcess()]
    can_commit_files = [AnyUserIfFileIsLocal(), SystemProcess()]
    can_read_files = [AnyUser(), SystemProcess()]
    can_update_files = [AnyUser(), SystemProcess()]
    can_delete_files = [AnyUser(), SystemProcess()]
