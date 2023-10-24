#!/usr/bin/node
// request and fetch API

const fs = require('fs');
// const request = require('request');
const process = require('process');

const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) { return console.error(err); } else { console.log(data); }
});
