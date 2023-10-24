#!/usr/bin/node
// request and fetch API
const fs = require('fs');
const process = require('process');

if ((process.argv).length >= 4) {
  const filename = process.argv[2];
  const data = process.argv[3];

  fs.writeFile(filename, data, (err) => {
    if (err) { return console.error(err); }
  });
}
