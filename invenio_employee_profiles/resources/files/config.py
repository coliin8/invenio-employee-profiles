# import importlib_metadata
# from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin


class EmployeeProfileFileResourceConfig(FileResourceConfig, ConfiguratorMixin):
    """EmployeeProfileFile resource config."""

    blueprint_name = "employee-profiles-files"
    url_prefix = "/employee-profiles-files/<pid_value>"