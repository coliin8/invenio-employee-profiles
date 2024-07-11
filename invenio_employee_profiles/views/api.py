from flask import Blueprint

blueprint = Blueprint(
    "invenio_employee_profiles_ext",
    __name__,
    template_folder="../templates",
)


def create_record_blueprint(app):
    blueprint = app.extensions['invenio-employee-profiles'].records_resource.as_blueprint()
    return blueprint
