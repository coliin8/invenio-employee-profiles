"""Resources for users employee profiles."""

from .resource import EmployeeProfileResource
from .files.resource import EmployeeProfileFileResource
from .config import EmployeeProfileResourceConfig
from .files.config import EmployeeProfileFileResourceConfig

__all__ = (
    "EmployeeProfileResource",
    "EmployeeProfileFileResource",
    "EmployeeProfileResourceConfig",
    "EmployeeProfileFileResourceConfig",
)
