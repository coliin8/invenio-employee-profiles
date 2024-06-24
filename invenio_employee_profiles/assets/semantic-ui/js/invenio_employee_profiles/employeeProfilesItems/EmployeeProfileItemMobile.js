// This file is part of InvenioRDM
// Copyright (C) 2022 CERN.
//
// Invenio App RDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import { Image } from "react-invenio-forms";
import { Grid } from "semantic-ui-react";
import PropTypes from "prop-types";

export const EmployeeProfileItemMobile = ({ result, index }) => {
  return (
    <Grid className="mobile only item community-item">
      <Grid.Row>
        <Grid.Column
          width={16}
          verticalAlign="middle"
          className="pl-0 pr-0"
        >
          <div className="flex align-items-center">
            <Image
              wrapped
              src={result.links.logo}
              size="mini"
              className="community-image rel-mr-1"
              alt=""
            />
            <div>
              <a
                className="truncate-lines-2 ui medium header m-0"
                href={result.links.self_html}
              >
                {result.email_address}
              </a>
            </div>
          </div>
        </Grid.Column>
      </Grid.Row>

      {result.biography && (
        <Grid.Row className="pt-0">
          <Grid.Column width={16} className="pl-0 pr-0">
            <p className="truncate-lines-1 text size small text-muted mt-5">
              {result.biography}
            </p>
          </Grid.Column>
        </Grid.Row>
      )}
    </Grid>
  );
};

CommunityItemMobile.propTypes = {
  result: PropTypes.object.isRequired,
  index: PropTypes.string,
};

CommunityItemMobile.defaultProps = {
  index: null,
};
