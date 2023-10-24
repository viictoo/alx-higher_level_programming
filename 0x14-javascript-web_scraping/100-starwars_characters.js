#!/usr/bin/node
// request and fetch API
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const chars = data.characters;
  for (const c of chars) {
    request.get(c, function (error, response, body1) {
      if (error) { console.log(error); }
      const datax = JSON.parse(body1);
      console.log(datax.name);
    });
  }
});
