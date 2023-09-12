#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  // unshift(Inserts new elements at the start of an array, and returns the new length of the array.)
  list.forEach(element => { reverse.unshift(element); });
  // for (const item of list) { reverse.unshift(item); }
  return reverse;
};
