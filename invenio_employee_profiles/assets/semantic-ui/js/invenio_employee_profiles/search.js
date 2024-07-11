/*
 * This file is part of Invenio.
 * Copyright (C) 2016-2021 CERN.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

import { createSearchAppInit } from "@js/invenio_search_ui";
import {
  ContribBucketAggregationElement,
  ContribBucketAggregationValuesElement,
  ContribSearchAppFacets,
} from "@js/invenio_search_ui/components";
import { overrideStore, parametrize } from "react-overridable";
import {
  EmployeeProfilesResults,
  EmployeeProfilesSearchBarElement,
  EmployeeProfilesSearchLayout,
  EmployeeProfileItem,
  ResultsGridItemTemplate,
} from "./";

const appName = "InvenioEmployeeProfiles.Search";

const ContribSearchAppFacetsWithConfig = parametrize(ContribSearchAppFacets, {
  help: false,
});

const EmployeeProfilesSearchLayoutConfig = parametrize(EmployeeProfilesSearchLayout, {
  appName: appName,
});

export const defaultComponents = {
  [`${appName}.BucketAggregation.element`]: ContribBucketAggregationElement,
  [`${appName}.BucketAggregationValues.element`]: ContribBucketAggregationValuesElement,
  [`${appName}.SearchApp.facets`]: ContribSearchAppFacetsWithConfig,
  [`${appName}.ResultsList.item`]: EmployeeProfileItem,
  [`${appName}.ResultsGrid.item`]: ResultsGridItemTemplate,
  [`${appName}.SearchApp.layout`]: EmployeeProfilesSearchLayoutConfig,
  [`${appName}.SearchBar.element`]: EmployeeProfilesSearchBarElement,
  [`${appName}.SearchApp.results`]: EmployeeProfilesResults,
};

const overriddenComponents = overrideStore.getAll();

// Auto-initialize search app
createSearchAppInit(
  { ...defaultComponents, ...overriddenComponents },
  true,
  "invenio-search-config",
  true
);
