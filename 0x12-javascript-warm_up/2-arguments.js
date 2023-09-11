#!/usr/bin/node

if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else if (process.argv[1]) {
  console.log('No argument');
}
