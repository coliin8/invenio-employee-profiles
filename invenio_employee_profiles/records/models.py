# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Employee Profile models."""

import uuid

from invenio_accounts.models import User
from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records.models import FileRecordModelMixin
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types import UUIDType


class EmployeeProfileModel(db.Model, RecordMetadataBase):
    __tablename__ = "employee_profiles"

    @declared_attr
    def user_id(cls):
        """Foreign key to the related user."""
        return db.Column(
            db.Integer(),
            db.ForeignKey(User.id, ondelete="RESTRICT"),
            # must be nullable because record service at first creates/commits an empty record and then fills it in
            nullable=True,
        )
    user = db.relationship(User, backref="employee_profiles")

    # kept here for easy searching
    active = db.Column(db.Boolean(name="active"))
    """Flag to say if the Employee Profile is active or not ."""
