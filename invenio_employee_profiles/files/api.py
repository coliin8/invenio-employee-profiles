from invenio_records_resources.records.api import FileRecord
# from invenio_records_resources.records.systemfields import IndexField

from ..files.models import EmployeeProfileFileModel


class EmployeeProfileFile(FileRecord):

    model_cls = EmployeeProfileFileModel

    record_cls = None  # is defined inside the parent record