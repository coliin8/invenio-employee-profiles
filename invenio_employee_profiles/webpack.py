# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2022 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JS/CSS bundles for employee profiles.

You include one of the bundles in a page like the example below (using
``employee profiles`` bundle as an example):

.. code-block:: html

    {{ webpack['communities.js']}}

"""

from invenio_assets.webpack import WebpackThemeBundle

employee_profiles = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "invenio-employee-profiles-search": "./js/invenio_employee_profiles/search.js"
            },
            dependencies={
                "@semantic-ui-react/css-patch": "^1.0.0",
                "react-router-dom": "^6.3.0",
                "react-invenio-forms": "^3.0.0",
                "axios": "^0.21.0",
                "formik": "^2.1.0",
                "i18next": "^20.3.0",
                "@tinymce/tinymce-react": "^4.3.0",
                "i18next-browser-languagedetector": "^6.1.0",
                "lodash": "^4.17.0",
                "luxon": "^1.23.0",
                "path": "^0.12.0",
                "prop-types": "^15.7.0",
                "qs": "^6.9.0",
                "react": "^16.13.0",
                "react-dom": "^16.13.0",
                "react-i18next": "^11.11.0",
                "react-redux": "^7.2.0",
                "react-searchkit": "^2.0.0",
                "redux": "^4.0.0",
                "redux-thunk": "^2.3.0",
                "semantic-ui-css": "^2.4.0",
                "semantic-ui-react": "^2.1.0",
                "tinymce": "^6.7.2",
                "yup": "^0.32.11",
            },
            aliases={
                # Define Semantic-UI theme configuration needed by
                # Invenio-Theme in order to build Semantic UI (in theme.js
                # entry point). theme.config itself is provided by
                # cookiecutter-invenio-rdm.
                "@js/invenio_employee_profiles": "js/invenio_employee_profiles",
                "@translations/invenio_employee_profiles": "translations/invenio_employee_profiles",
            },
        ),
    },
)
