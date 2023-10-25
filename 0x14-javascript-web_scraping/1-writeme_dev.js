#!/usr/bin/node
// request and fetch API
const fs = require('fs');
const process = require('process');
const av = process.argv;


if ((av).length >= 4) {
  fs.writeFile(av[2], av[3], (err) => {
    if (err) { return console.error(err); }
  });
}
