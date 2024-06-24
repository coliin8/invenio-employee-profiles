from invenio_i18n import lazy_gettext as _

from invenio_employee_profiles.resources.config import (
    employee_profile_error_handlers
)


EMPLOYEE_PROFILE_ROUTES = {
    "search": "/employee-profiles/search",
}

#
# Employee Profile Search configuration
#
EMPLOYEE_PROFILE_FACETS = {}

EMPLOYEE_PROFILE_SORT_OPTIONS = {
    "bestmatch": dict(
        title=_("Best match"),
        fields=["_score"],  # ES defaults to desc on `_score` field
    ),
    "newest": dict(
        title=_("Newest"),
        fields=["-created"],
    ),
    "oldest": dict(
        title=_("Oldest"),
        fields=["created"],
    ),
}
"""Definitions of available record sort options."""


EMPLOYEE_PROFILE_SEARCH = {
    "facets": [],
    "sort": ["bestmatch", "newest", "oldest"],
}
"""Employee Profile search configuration."""


EMPLOYEE_PROFILE_LOGO_MAX_FILE_SIZE = 10**6
"""Employee Profile image logo size quota, in bytes."""

EMPLOYEE_PROFILE_ERROR_HANDLERS = {
    **employee_profile_error_handlers,
}
