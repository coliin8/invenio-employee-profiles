# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology
# Copyright (C) 2022 TU Wien.
# Copyright (C) 2022 European Union.
# Copyright (C) 2022 CERN.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""User Employee Profile Services."""
from flask import current_app

from invenio_records_resources.services.uow import (
    RecordCommitOp,
    unit_of_work,
)
from invenio_records_resources.services.records import RecordService

from invenio_employee_profiles.errors import (
    LogoSizeLimitError,
)


class EmployeeProfileService(RecordService):
    """Employee Profile Service class."""

    def __init__(self, config, files_service=None):
        """Constructor for RecordService."""
        super().__init__(config)
        self._files = files_service

    #
    # Subservices
    #
    @property
    def files(self):
        """Record files service."""
        return self._files

    def read_logo(self, identity, id_):
        """Read the community's logo."""
        record = self.record_cls.pid.resolve(id_)
        self.require_permission(identity, "read", record=record)
        logo_file = record.files.get("logo")
        if logo_file is None:
            raise FileNotFoundError()
        return self.files.file_result_item(
            self.files,
            identity,
            logo_file,
            record,
            links_tpl=self.files.file_links_item_tpl(id_),
        )

    @unit_of_work()
    def update_logo(self, identity, id_, stream, content_length=None, uow=None):
        """Update the community's logo."""
        record = self.record_cls.pid.resolve(id_)
        self.require_permission(identity, "update", record=record)

        logo_size_limit = 10**6
        max_size = current_app.config["EMPLOYEE_PROFILE_LOGO_MAX_FILE_SIZE"]
        if type(max_size) is int and max_size > 0:
            logo_size_limit = max_size

        if content_length and content_length > logo_size_limit:
            raise LogoSizeLimitError(logo_size_limit, content_length)

        record.files["logo"] = stream
        uow.register(RecordCommitOp(record))

        return self.files.file_result_item(
            self.files,
            identity,
            record.files["logo"],
            record,
            links_tpl=self.files.file_links_item_tpl(id_),
        )

    @unit_of_work()
    def delete_logo(self, identity, id_, uow=None):
        """Delete the community's logo."""
        record = self.record_cls.pid.resolve(id_)
        # update permission on community is required to be able to remove logo.
        self.require_permission(identity, "update", record=record)
        deleted_file = record.files.pop("logo", None)
        if deleted_file is None:
            raise FileNotFoundError()

        uow.register(RecordCommitOp(record))

        return self.files.file_result_item(
            self.files,
            identity,
            deleted_file,
            record,
            links_tpl=self.files.file_links_item_tpl(id_),
        )
