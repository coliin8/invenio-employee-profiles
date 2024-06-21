from invenio_i18n import lazy_gettext as _


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
