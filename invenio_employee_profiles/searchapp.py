# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 CERN.
#
# Invenio-App-RDM is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Configuration helper for React-SearchKit."""

from functools import partial

from flask import current_app
from invenio_search_ui.searchconfig import search_app_config


def search_app_context():
    """Search app context processor."""
    return {
        "search_app_employee_profile_records_config": partial(
            search_app_config,
            config_name="EMPLOYEE_PROFILE_SEARCH",
            available_facets=current_app.config["EMPLOYEE_PROFILE_FACETS"],
            sort_options=current_app.config["EMPLOYEE_PROFILE_SORT_OPTIONS"],
            headers={"Accept": "application/json"},
            pagination_options=(10, 20),
            endpoint="/api/employee-profiles",
        ),
    }