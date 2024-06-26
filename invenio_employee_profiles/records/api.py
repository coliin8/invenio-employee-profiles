from invenio_records.dumpers import SearchDumper
from invenio_records.dumpers.indexedat import IndexedAtDumperExt
from invenio_records.dumpers.relations import RelationDumperExt
from invenio_records.systemfields import ModelRelation, RelationsField, ModelField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField, FilesField
from invenio_users_resources.records.api import UserAggregate

from invenio_employee_profiles.files.api import EmployeeProfileFile

from .models import EmployeeProfileModel


class GetRecordResolver(object):
    """Resolver that simply uses get record."""

    def __init__(self, record_cls):
        """Initialize resolver."""
        self._record_cls = record_cls

    def resolve(self, pid_value, registered_only=False):
        """Simply get the record."""
        _ = registered_only
        return self._record_cls.get_record(pid_value)


class DirectIdPID:
    """Helper emulate a PID field."""

    def __init__(self, id_field="id"):
        """Constructor."""
        self._id_field = id_field

    def __get__(self, record, owner=None):
        """Evaluate the property."""
        if record is None:
            return GetRecordResolver(owner)
        return DirectIdPID(getattr(record, self._id_field))


class EmployeeProfile(Record):

    model_cls = EmployeeProfileModel

    dumper = SearchDumper(
        extensions=[
            RelationDumperExt("relations"),
            IndexedAtDumperExt(),
        ]
    )

    # Systemfields
    index = IndexField(
        "employeeprofiles-employeeprofile-v1.0.0",
        search_alias="employeeprofiles",
    )

    pid = DirectIdPID()

    active = ModelField("active")

    user_id = ModelField("user_id")

    # Employee Profile File related fields
    files = FilesField(file_cls=EmployeeProfileFile, store=False)
    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)
    media_bucket_id = ModelField(dump=False)
    media_bucket = ModelField(dump=False)

    # Relationships to other models
    relations = RelationsField(
        user=ModelRelation(
            UserAggregate,
            "user_id",
            "user",
            attrs=[
                "email",
                "username",
                "profile",
                "preferences",
                "active",
                "confirmed",
                "verified_at",
            ],
        )
    )


EmployeeProfileFile.record_cls = EmployeeProfile
