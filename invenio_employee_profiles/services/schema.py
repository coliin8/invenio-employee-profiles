import marshmallow as ma
from marshmallow_utils.fields import NestedAttribute, SanitizedUnicode
from marshmallow_utils.permissions import FieldPermissionsMixin

from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from invenio_users_resources.services.schemas import UserSchema


class FilesSchema(ma.Schema):
    """Basic files schema class."""

    enabled = ma.fields.Bool(missing=True)
    # allow unsetting
    default_preview = SanitizedUnicode(allow_none=True)

    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        value = getattr(obj, attr, default)

        if attr == "default_preview" and not value:
            return default

        return value


class EmployeeProfileSchema(InvenioBaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    email_address = ma.fields.Email()
    biography = ma.fields.String()
    profile_image = ma.fields.String()
    user = ma.fields.Nested(UserSchema, required=True)
    active = ma.fields.Boolean()
    files = NestedAttribute(FilesSchema)
