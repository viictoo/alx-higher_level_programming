#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

function check (num) {
  if (num !== 0 && !num) {
    console.log('NaN');
    return (0);
  }
  return (1);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (check(a) && check(b)) {
  console.log(add(a, b));
}
