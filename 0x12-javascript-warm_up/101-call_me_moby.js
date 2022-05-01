#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i;
  for (i = 1; i <= x; i++) {
    theFunction();
  }
};
