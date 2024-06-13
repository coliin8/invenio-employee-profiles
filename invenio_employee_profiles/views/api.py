def create_record_blueprint(app):
    blueprint = app.extensions['invenio-employee-profiles'].records_resource.as_blueprint()
    blueprint.record_once(init)
    return blueprint


def create_file_blueprint(app):
    return app.extensions['invenio-employee-profiles'].files_resource.as_blueprint()


def init(state):
    app = state.app
    ext = app.extensions["invenio-employee-profiles"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(
        ext.records_service, service_id=ext.records_service.config.service_id
    )

    # Register indexer
    if hasattr(ext.records_service, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(
            ext.records_service.indexer,
            indexer_id=ext.records_service.config.service_id,
        )
