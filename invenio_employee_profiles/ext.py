"""Extension for Employee Profile."""
from functools import cached_property

from flask_menu import current_menu

from invenio_i18n import lazy_gettext as _
from invenio_records_resources.services import FileService
# from invenio_records_resources.resources import FileResource

from .resources import (
    EmployeeProfileResourceConfig,
    EmployeeProfileResource,
    # EmployeeProfileFileResourceConfig
)
from .services import (
    EmployeeProfileService,
    EmployeeProfileServiceConfig,
    EmployeeProfileFileServiceConfig
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
            files_service=FileService(self._service_config.file)
        )

    def init_resource(self):
        """Initialize resources."""
        self.records_resource = EmployeeProfileResource(
            config=self._resource_config.record,
            service=self.records_service,
        )

        # # Record files resource
        # self.files_resource = FileResource(
        #     config=self._resource_config.file,
        #     service=self.records_service.files,
        # )

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
            # file = EmployeeProfileFileResourceConfig.build(self.app)

        return ResourceConfigs

    def init_config(self, app):
        """Setup Extension config."""
        # Override configuration variables with the values in this package.
        for k in dir(config):
            if k.startswith("EMPLOYEE_PROFILE_"):
                app.config.setdefault(k, getattr(config, k))

    # endregion


def finalize_app(app):
    """Finalize app.

    NOTE: replace former @record_once decorator
    """
    init(app)
    register_menus(app)


def register_menus(app):
    """Register community menu items."""
    current_menu.submenu("main.employeeprofiles").register(
        endpoint="invenio_employee_profiles.employee_profiles_search",
        text=_("Employee Profiles"),
        order=1,
    )


def api_finalize_app(app):
    """Finalize app for api.

    NOTE: replace former @record_once decorator
    """
    init(app)


def init(app):
    ext = app.extensions["invenio-employee-profiles"]
    service_id = ext.records_service.config.service_id
    file_service_id = ext.records_service.files.config.service_id

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(
        ext.records_service, service_id=service_id
    )
    sregistry.register(
        ext.records_service.files, service_id=file_service_id
    )
    # Register indexers
    iregistry = app.extensions["invenio-indexer"].registry
    iregistry.register(ext.records_service.indexer, indexer_id=service_id)
