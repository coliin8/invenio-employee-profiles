import { InvenioSearchPagination } from "@js/invenio_search_ui/components";
import React from "react";
import { ResultsList } from "react-searchkit";
import { Grid } from "semantic-ui-react";
import PropTypes from "prop-types";

export const EmployeeProfilesResults = ({ paginationOptions, currentResultsState }) => {
  const { total } = currentResultsState.data;
  return (
    total && (
      <Grid>
        <Grid.Row>
          <Grid.Column>
            <ResultsList />
          </Grid.Column>
        </Grid.Row>

        <InvenioSearchPagination total={total} paginationOptions={paginationOptions} />
      </Grid>
    )
  );
};

EmployeeProfilesResults.propTypes = {
  paginationOptions: PropTypes.object.isRequired,
  currentResultsState: PropTypes.object.isRequired,
};
