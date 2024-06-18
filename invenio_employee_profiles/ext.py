"""Extension for Employee Profile."""
from functools import cached_property

from .resources import (
    EmployeeProfileResourceConfig,
    EmployeeProfileResource,
    EmployeeProfileFileResourceConfig,
    EmployeeProfileFileResource
)
from .services import (
    EmployeeProfileService,
    EmployeeProfileServiceConfig,
    EmployeeProfileFileServiceConfig,
    EmployeeProfileFileService
)
from . import config


class EmployeeProfileExtension:
    """Employee Profile Extension Class."""

    def __init__(self, app=None):
        """Extension initialization."""
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Extension Initials when app is not None."""

        # in case the app is not passed in the constructor
        self.app = app

        self.init_config(app)
        self.init_services()
        self.init_resource()
        app.extensions["invenio-employee-profiles"] = self

    def init_services(self):
        """Extension initialization of Service."""
        self.records_service = EmployeeProfileService(
            config=self._service_config.record,
            files_service=EmployeeProfileFileService(self._service_config.file)
        )

    def init_resource(self):
        """Initialize resources."""
        self.records_resource = EmployeeProfileResource(
            config=self._resource_config.record,
            service=self.records_service,
        )

        # Record files resource
        self.files_resource = EmployeeProfileFileResource(
            config=self._resource_config.file,
            service=self.records_service.files,
        )

    # region Private Methods

    @cached_property
    def _service_config(self):
        """Extension initialization of Service configs."""

        class ServiceConfigs:
            record = EmployeeProfileServiceConfig.build(self.app)
            file = EmployeeProfileFileServiceConfig.build(self.app)

        return ServiceConfigs

    @cached_property
    def _resource_config(self):
        """Extension initialization of Resource configs."""
        class ResourceConfigs:
            record = EmployeeProfileResourceConfig.build(self.app)
            file = EmployeeProfileFileResourceConfig.build(self.app)

        return ResourceConfigs

    def init_config(self, app):
        """Setup Extension config."""
        # Override configuration variables with the values in this package.
        for k in dir(config):
            if k.startswith("EMPLOYEE_PROFILE_"):
                app.config.setdefault(k, getattr(config, k))

    # endregion
