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

from invenio_records_resources.services.records import RecordService


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
