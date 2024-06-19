# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TU Wien.
# Copyright (C) 2022 CERN.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Employee Profile service configuration."""

from sqlalchemy import asc, desc

from invenio_records_resources.services.records import RecordServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin

from .permissions import EmployeeProfilePermissionPolicy
from .schema import EmployeeProfileSchema
from ..records.api import EmployeeProfile

from invenio_records_resources.services.records.components import DataComponent, RelationsComponent
from .components import EmployeeProfileServiceComponent


class SearchOptions:
    """Search options."""

    sort_default = "created"
    sort_direction_default = "asc"

    sort_direction_options = {
        "asc": dict(
            title=_("Ascending"),
            fn=asc,
        ),
        "desc": dict(
            title=_("Descending"),
            fn=desc,
        ),
    }

    sort_options = {
        "email_address": dict(
            title=_("Email Address"),
            fields=["email_address"],
        ),
        "created": dict(
            title=_("Created"),
            fields=["created"],
        ),
        "updated": dict(
            title=_("Updated"),
            fields=["updated"],
        ),
    }
    pagination_options = {
        "default_results_per_page": 25,
    }


class EmployeeProfileServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    """Employee Profile Service configuration Class."""

    service_id = "employeeprofiles"

    # Record specific configuration
    record_cls = EmployeeProfile

    # Service schema
    schema = EmployeeProfileSchema

    # Search configuration
    search = SearchOptions

    # Common configuration
    permission_policy_cls = EmployeeProfilePermissionPolicy
    indexer_queue_name = "employeeprofiles"

    components = [
        DataComponent,
        RelationsComponent,
        EmployeeProfileServiceComponent,
    ]
