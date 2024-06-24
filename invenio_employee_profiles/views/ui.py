# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2024 CERN.
# Copyright (C) 2023-2024 Graz University of Technology.
# Copyright (C) 2023 KTH Royal Institute of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Communities UI views."""

from datetime import datetime

from babel.dates import format_datetime
from flask import Blueprint, current_app, g, render_template, request, url_for
from flask_login import current_user
from invenio_pidstore.errors import PIDDeletedError, PIDDoesNotExistError
# from invenio_records_resources.proxies import current_service_registry
from invenio_records_resources.services.errors import PermissionDeniedError

# from invenio_communities.communities.resources.serializer import (
#     UICommunityJSONSerializer,
# )
# from invenio_communities.proxies import current_communities

from ..searchapp import search_app_context
from .employee_profiles import (
    employee_profiles_search,
)


#
# Error handlers
#
def not_found_error(error):
    """Handler for 'Not Found' errors."""
    return render_template(current_app.config["THEME_404_TEMPLATE"]), 404


# def record_tombstone_error(error):
#     """Tombstone page."""
#     record = getattr(error, "record", None)
#     if (record_ui := getattr(error, "result_item", None)) is not None:
#         if record is None:
#             record = record_ui._record
#         record_ui = UICommunityJSONSerializer().dump_obj(record_ui.to_dict())

#     # render a 404 page if the tombstone isn't visible
#     if not record.tombstone.is_visible:
#         return not_found_error(error)

#     # we only render a tombstone page if there is a record with a visible tombstone
#     return (
#         render_template(
#             "invenio_communities/tombstone.html",
#             record=record_ui,
#         ),
#         410,
#     )


def record_permission_denied_error(error):
    """Handle permission denier error on record views."""
    if not current_user.is_authenticated:
        # trigger the flask-login unauthorized handler
        return current_app.login_manager.unauthorized()
    return render_template(current_app.config["THEME_403_TEMPLATE"]), 403


#
# Registration
#
def create_ui_blueprint(app):
    """Register blueprint routes on app."""
    routes = app.config.get("EMPLOYEE_PROFILE_ROUTES")

    blueprint = Blueprint(
        "invenio_communities",
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    # Communities URL rules
    blueprint.add_url_rule(
        routes["search"],
        view_func=employee_profiles_search,
        strict_slashes=False,
    )

    # theme injection view
    # blueprint.add_url_rule(
    #     "/communities/<pid_value>/community-theme-<revision>.css",
    #     view_func=community_theme_css_config,
    # )

    # Register error handlers
    blueprint.register_error_handler(
        PermissionDeniedError, record_permission_denied_error
    )
    blueprint.register_error_handler(PIDDoesNotExistError, not_found_error)

    # Register context processor
    blueprint.app_context_processor(search_app_context)

    # Template filters
    @blueprint.app_template_filter()
    def invenio_format_datetime(value):
        date = datetime.fromisoformat(value)
        locale_value = current_app.config.get("BABEL_DEFAULT_LOCALE")
        return format_datetime(date, locale=locale_value)

    return blueprint
