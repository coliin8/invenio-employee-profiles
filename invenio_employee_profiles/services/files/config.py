from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from invenio_records_resources.services.base.config import ConfiguratorMixin

from ...records.api import EmployeeProfile
# from theses.services.files.schema import ThesesFileSchema
from ...services.permissions import EmployeeProfilePermissionPolicy


class EmployeeProfileFileServiceConfig(FileServiceConfig, ConfiguratorMixin):
    """ThesesRecord service config."""

    url_prefix = "/employee-profiles/<pid_value>"

    permission_policy_cls = EmployeeProfilePermissionPolicy

    record_cls = EmployeeProfile

    service_id = "employee-profiles-files"

    components = [
        # *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/employee-profiles/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/employee-profiles/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/employee-profiles/{id}/files/{key}/content"),
            "self": FileLink("{+api}/employee-profiles/{id}/files/{key}"),
        }
