#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurs = 0;
  list.forEach(i => { if (i === searchElement) { occurs += 1; } });
  return occurs;
};
