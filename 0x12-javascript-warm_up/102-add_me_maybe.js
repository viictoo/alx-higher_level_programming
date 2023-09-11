#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  x += 1;
  theFunction(x);
};
