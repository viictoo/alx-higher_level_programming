#!/usr/bin/node

// a = 12
// console.log(a.toString(2)); / 1100
exports.converter = function (base) { return (num) => { return num.toString(base); }; };
