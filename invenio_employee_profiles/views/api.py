def create_record_blueprint(app):
    blueprint = app.extensions['invenio-employee-profiles'].records_resource.as_blueprint()
    return blueprint


def create_file_blueprint(app):
    return app.extensions['invenio-employee-profiles'].files_resource.as_blueprint()
