from math import ceil

from invenio_i18n import gettext as _


class EmployeeProfileError(Exception):
    """Base exception for community errors."""


class LogoSizeLimitError(EmployeeProfileError):
    """The provided logo size exceeds limit."""

    def __init__(self, limit, file_size):
        """Initialise error."""
        super().__init__(
            _(
                "Logo size limit exceeded. Limit: {limit} bytes Given: {file_size} bytes".format(
                    limit=ceil(limit), file_size=ceil(file_size)
                )
            )
        )
