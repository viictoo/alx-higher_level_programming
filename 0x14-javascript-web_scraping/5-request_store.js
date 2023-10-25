#!/usr/bin/node
// request and fetch API

const request = require('request');
const fs = require('fs');

const av = process.argv;

request(av[2], (err, response, body) => {
  if (err) { console.log(err); } else {
    fs.writeFile(av[3], body, 'utf-8', (err) => { if (err) { console.log(err); }
    });
  }
});
