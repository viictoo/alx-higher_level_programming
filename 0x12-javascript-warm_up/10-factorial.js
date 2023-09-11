#!/usr/bin/node

let factor = parseInt(process.argv[2]);

function factorial (num) {
  if (!num || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

factor = factorial(factor);
console.log(factor);
