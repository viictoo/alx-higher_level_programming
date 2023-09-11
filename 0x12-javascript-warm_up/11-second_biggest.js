#!/usr/bin/node

let num = 0;
let max = process.argv[2];

for (let i = 3; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > max) {
    num = max;
    max = process.argv[i];
  } else if (parseInt(process.argv[i]) > num || max < num) {
    num = process.argv[i];
  }
}
console.log(num);
console.log(max);
