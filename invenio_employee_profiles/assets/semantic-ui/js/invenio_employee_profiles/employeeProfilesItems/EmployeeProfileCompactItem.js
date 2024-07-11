import React from "react";
import PropTypes from "prop-types";

import { EmployeeProfileCompactItemComputer } from "./EmployeeProfileCompactItemComputer";
import { EmployeeProfileCompactItemMobile } from "./EmployeeProfileCompactItemMobile";

export function EmployeeProfileCompactItem({
  result,
  actions,
  extraLabels,
  itemClassName,
  showPermissionLabel,
  detailUrl,
  isCommunityDefault,
}) {
  return (
    <>
      <EmployeeProfileCompactItemComputer
        result={result}
        actions={actions}
        extraLabels={extraLabels}
        itemClassName={itemClassName}
        showPermissionLabel={showPermissionLabel}
        detailUrl={detailUrl}
        isCommunityDefault={isCommunityDefault}
      />
      <EmployeeProfileCompactItemMobile
        result={result}
        actions={actions}
        extraLabels={extraLabels}
        itemClassName={itemClassName}
        showPermissionLabel={showPermissionLabel}
        detailUrl={detailUrl}
        isCommunityDefault={isCommunityDefault}
      />
    </>
  );
}

EmployeeProfileCompactItem.propTypes = {
  result: PropTypes.object.isRequired,
  actions: PropTypes.node,
  extraLabels: PropTypes.node,
  itemClassName: PropTypes.string,
  showPermissionLabel: PropTypes.bool,
  detailUrl: PropTypes.string,
  isCommunityDefault: PropTypes.bool.isRequired,
};

EmployeeProfileCompactItem.defaultProps = {
  actions: undefined,
  extraLabels: undefined,
  itemClassName: "",
  showPermissionLabel: false,
  detailUrl: undefined,
};
