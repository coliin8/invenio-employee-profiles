// This file is part of InvenioRDM
// Copyright (C) 2022 CERN.
//
// Invenio App RDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import _truncate from "lodash/truncate";
import React from "react";
import { Image, InvenioPopup } from "react-invenio-forms";
import { Icon, Label } from "semantic-ui-react";
import PropTypes from "prop-types";

export const EmployeeProfileCompactItemMobile = ({
  result,
  actions,
  extraLabels,
  itemClassName,
  showPermissionLabel,
  detailUrl,
  isCommunityDefault,
}) => {
  const { biography, links, email_address, id } = result;
  return (
    <div key={id} className={`community-item mobile only ${itemClassName}`}>
      <div className="display-grid auto-column-grid no-wrap">
        <div className="flex align-items-center">
          <Image
            wrapped
            size="mini"
            src={links.logo}
            alt=""
            className="community-image rel-mr-1"
          />

          <div className="flex align-items-center rel-mb-1">
            <a
              href={links.self_html}
              className="ui small header truncate-lines-2 m-0 mr-5"
              target="_blank"
              rel="noreferrer"
              aria-label={`${email_address}`}
            >
              {email_address}
            </a>
            <i className="small icon external primary" aria-hidden="true" />
          </div>
        </div>
      </div>

      <div className="full-width">
        {biography && (
          <p className="truncate-lines-1 text size small text-muted mt-5 rel-mb-1">
            {_truncate(biography, { length: 50 })}
          </p>
        )}
      </div>
    </div>
  );
};

EmployeeProfileCompactItemMobile.propTypes = {
  result: PropTypes.object.isRequired,
  extraLabels: PropTypes.node,
  itemClassName: PropTypes.string,
  showPermissionLabel: PropTypes.bool,
  actions: PropTypes.node,
  detailUrl: PropTypes.string,
  isCommunityDefault: PropTypes.bool.isRequired,
};

EmployeeProfileCompactItemMobile.defaultProps = {
  actions: undefined,
  extraLabels: undefined,
  itemClassName: "",
  showPermissionLabel: false,
  detailUrl: undefined,
};
