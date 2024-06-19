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
    "version": dict(
        title=_("Version"),
        fields=["-versions.index"],
    ),
    "updated-desc": dict(
        title=_("Recently updated"),
        fields=["-updated"],
    ),
    "updated-asc": dict(
        title=_("Least recently updated"),
        fields=["updated"],
    ),
}
"""Definitions of available record sort options."""


EMPLOYEE_PROFILE_SEARCH = {
    "facets": [],
    "sort": ["email_address", "created", "updated"],
}
"""Employee Profile search configuration."""
