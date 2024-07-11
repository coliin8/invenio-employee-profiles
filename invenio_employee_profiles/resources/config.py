"""Config for Employee Profile Resource."""
from flask_resources import (
    HTTPJSONException,
    create_error_handler,
)

from invenio_records_resources.resources.records import RecordResourceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin, FromConfig

from ..errors import LogoSizeLimitError


employee_profile_error_handlers = RecordResourceConfig.error_handlers.copy()
employee_profile_error_handlers.update(
    {
        FileNotFoundError: create_error_handler(
            HTTPJSONException(
                code=404,
                description="No logo exists for this community.",
            )
        ),
        LogoSizeLimitError: create_error_handler(
            lambda e: HTTPJSONException(
                code=400,
                description=str(e),
            )
        ),
    }
)


class EmployeeProfileResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    """Blueprint configuration."""

    blueprint_name = "employee-profiles"
    url_prefix = "/employee-profiles"

    routes = {
        "list": "",
        "item": "/<pid_value>",
        "logo": "/<pid_value>/logo",
    }

    error_handlers = FromConfig(
        "EMPLOYEE_PROFILE_ERROR_HANDLERS",
        default=employee_profile_error_handlers
    )


# class EmployeeProfileFileResourceConfig(FileResourceConfig, ConfiguratorMixin):
#     """EmployeeProfileFile resource config."""

#     blueprint_name = "employee-profiles-files"
#     url_prefix = "/employee-profiles/<pid_value>"
