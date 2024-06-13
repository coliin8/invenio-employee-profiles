from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from ..records.models import EmployeeProfileModel


class EmployeeProfileFileModel(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for Employee Profile File metadata."""

    __tablename__ = "employee_profiles_file_metadata"
    __record_model_cls__ = EmployeeProfileModel
