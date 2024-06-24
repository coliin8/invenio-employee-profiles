import React from "react";
import PropTypes from "prop-types";

import { EmployeeProfileItemComputer } from "./EmployeeProfileItemComputer";
import { EmployeeProfileItemMobile } from "./EmployeeProfileItemMobile";

export function EmployeeProfileItem({ result }) {
  return (
    <>
      <EmployeeProfileItemComputer result={result} />
      <EmployeeProfileItemMobile result={result} />
    </>
  );
}

EmployeeProfileItem.propTypes = {
  result: PropTypes.object.isRequired,
};
