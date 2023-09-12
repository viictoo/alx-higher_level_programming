#!/usr/bin/node
// a script that checks if a value exists in an dict array if not adds it
// process
// import dict with values
// exports.dict = { 89: 1, 90: 2, 91: 1, 92: 3, 93: 1, 94: 2 };
// Check if newObj[object[key]] is already an array, if not
// Initialize as an array with the new value

const object = require('./101-data').dict;

const newObj = {};
for (const key in object) {
  if (Object.hasOwnProperty.call(newObj, object[key])) {
    if (!Array.isArray(newObj[object[key]])) {
      newObj[object[key]] = [newObj[object[key]]];
    }
    newObj[object[key]].push(key);
  } else {
    newObj[object[key]] = [key];
  }
}
console.log(newObj);
