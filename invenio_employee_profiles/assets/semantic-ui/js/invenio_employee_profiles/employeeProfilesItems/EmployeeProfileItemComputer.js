// This file is part of InvenioRDM
// Copyright (C) 2022 CERN.
//
// Invenio App RDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import { Image } from "react-invenio-forms";
import { Grid } from "semantic-ui-react";
import PropTypes from "prop-types";

export const EmployeeProfileItemComputer = ({ result }) => {
  const { biography, links, email_address, id } = result;
  return (
    <Grid className="computer tablet only item community-item">
      <Grid.Column
        tablet={16}
        computer={13}
        verticalAlign="middle"
        className="pl-0"
      >
        <div className="flex align-items-center">
          <Image
            wrapped
            src={links.logo}
            size="tiny"
            className="community-image rel-mr-2"
            alt=""
          />
          <div>
            <a className="ui medium header mb-0" href={links.self_html}>
              {email_address}
            </a>
            {result.biography && (
              <p className="truncate-lines-1 text size small text-muted mt-5">
                {biography}
              </p>
            )}
          </div>
        </div>
      </Grid.Column>
    </Grid>
  );
};

EmployeeProfileItemComputer.propTypes = {
  result: PropTypes.object.isRequired,
};
