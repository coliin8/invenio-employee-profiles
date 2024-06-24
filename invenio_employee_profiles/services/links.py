from invenio_records_resources.services.base.links import Link


class EPLink(Link):
    """Short cut for writing record links."""

    @staticmethod
    def vars(record, vars):
        """Variables for the URI template."""
        # Some records don't have record.pid.pid_value yet (e.g. drafts)
        pid_value = getattr(record, "pid", None)
        if pid_value:
            vars.update({"id": record.id})
