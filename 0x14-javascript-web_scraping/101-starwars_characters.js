#!/usr/bin/node
// request and fetch API
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    sprinter(characters, 0);
  }
});

function sprinter (chars, index) {
  request(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) { sprinter(chars, index + 1); }
    }
  });
}
