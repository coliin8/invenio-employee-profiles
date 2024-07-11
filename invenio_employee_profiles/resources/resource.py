"""Resource for Employee Profile."""

from flask import g
from flask_resources import (
    resource_requestctx,
    response_handler,
    route,
)

from invenio_records_resources.resources.files.resource import request_stream
from invenio_records_resources.resources.records.resource import (
    RecordResource,
    request_view_args,
)

from invenio_employee_profiles.proxies import current_profiles


#
# Resource
#
class EmployeeProfileResource(RecordResource):
    """Employee Profile Resource class."""

    def create_url_rules(self):
        """Create the URL rules for the record resource."""
        routes = self.config.routes
        return [
            route("GET", routes["list"], self.search),
            route("POST", routes["list"], self.create),
            route("GET", routes["item"], self.read),
            route("PUT", routes["item"], self.update),
            route("DELETE", routes["item"], self.delete),
            route("GET", routes["logo"], self.read_logo),
            route("PUT", routes["logo"], self.update_logo),
            route("DELETE", routes["logo"], self.delete_logo),
        ]

    @request_view_args
    def read_logo(self):
        """Read logo's content."""
        ep_pid = resource_requestctx.view_args["pid_value"]
        item = self.service.read_logo(
            g.identity,
            ep_pid,
        )
        return item.send_file(restricted=False)

    @request_view_args
    @request_stream
    @response_handler()
    def update_logo(self):
        """Upload logo content."""
        item = self.service.update_logo(
            g.identity,
            resource_requestctx.view_args["pid_value"],
            resource_requestctx.data["request_stream"],
            content_length=resource_requestctx.data["request_content_length"],
        )
        return item.to_dict(), 200

    @request_view_args
    def delete_logo(self):
        """Delete logo."""
        self.service.delete_logo(
            g.identity,
            resource_requestctx.view_args["pid_value"],
        )
        return "", 204
