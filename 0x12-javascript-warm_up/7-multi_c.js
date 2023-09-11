#!/usr/bin/node

const num = parseInt(process.argv[2]);
let str = '';

if (num !== 0 && !num) {
  console.log('Missing number of occurrences');
} else {
  for (let y = 0; y < num; y++) {
    str += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(str);
  }
}
