#!/usr/bin/node
const { argv } = require('process');
let num = 0;
let max = argv[2];

for (let i = 3; i < argv.length; i++) {
  if (parseInt(argv[i]) > max) {
    num = max;
    max = process.argv[i];
  } else if (parseInt(argv[i]) > num && parseInt(argv[i]) < max) {
    num = argv[i];
  }
}
console.log(num);
