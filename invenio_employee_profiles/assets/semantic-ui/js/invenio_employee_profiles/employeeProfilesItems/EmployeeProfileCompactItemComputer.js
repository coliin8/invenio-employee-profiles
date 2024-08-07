// This file is part of InvenioRDM
// Copyright (C) 2023 CERN.
//
// InvenioRDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import PropTypes from "prop-types";
import _truncate from "lodash/truncate";

import { Image } from "react-invenio-forms";
import { Item } from "semantic-ui-react";

export const EmployeeProfileCompactItemComputer = ({
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
    <Item
      key={id}
      className={`community-item tablet computer only display-grid auto-column-grid no-wrap ${itemClassName}`}
    >
      <div className="flex align-items-center">
        <Image
          wrapped
          size="tiny"
          src={links.logo}
          alt=""
          className="community-image rel-mr-2"
        />
        <div>
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
          {biography && (
            <p className="truncate-lines-1 text size small text-muted mt-5 rel-mb-1">
              {_truncate(biography, { length: 50 })}
            </p>
          )}

        </div>
      </div>
    </Item>
  );
};

EmployeeProfileCompactItemComputer.propTypes = {
  result: PropTypes.object.isRequired,
  actions: PropTypes.node,
  extraLabels: PropTypes.node,
  itemClassName: PropTypes.string,
  showPermissionLabel: PropTypes.bool,
  detailUrl: PropTypes.string,
  isCommunityDefault: PropTypes.bool.isRequired,
};

EmployeeProfileCompactItemComputer.defaultProps = {
  actions: undefined,
  extraLabels: undefined,
  itemClassName: "",
  showPermissionLabel: false,
  detailUrl: undefined,
};
