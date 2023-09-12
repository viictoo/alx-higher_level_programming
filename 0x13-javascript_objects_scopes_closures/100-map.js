#!/usr/bin/node
// array.map() takes a callback function as an argument
// and applies that function to each element of the array

const array = require('./100-data').list;
console.log(array);
const nuArray = array.map((elem, idx) => elem * idx);
console.log(nuArray);
