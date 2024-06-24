import React from "react";
import PropTypes from "prop-types";

import { EmployeeProfileItemComputer } from "./EmployeeProfileItemComputer";
import { EmployeeProfileItemMobile } from "./EmployeeProfileItemMobile";

export function CommunityItem({ result }) {
  return (
    <>
      <EmployeeProfileItemComputer result={result} />
      <EmployeeProfileItemMobile result={result} />
    </>
  );
}

CommunityItem.propTypes = {
  result: PropTypes.object.isRequired,
};
