from invenio_i18n import lazy_gettext as _


#
# Employee Profile Search configuration
#
EMPLOYEE_PROFILE_FACETS = {}

EMPLOYEE_PROFILE_SORT_OPTIONS = {
    "name": dict(
        title=_("Set Email Address"),
        fields=["email_address"],
    ),
    # "spec": dict(
    #     title=_("Set spec"),
    #     fields=["spec"],
    # ),
    "created": dict(
        title=_("Created"),
        fields=["created"],
    ),
    "updated": dict(
        title=_("Updated"),
        fields=["updated"],
    ),
}
"""Definitions of available EMPLOYEE_PROFILE sort options. """

EMPLOYEE_PROFILE_SEARCH = {
    "facets": [],
    "sort": ["email_address", "created", "updated"],
}
"""Employee Profile search configuration."""