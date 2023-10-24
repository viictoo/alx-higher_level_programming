#!/usr/bin/node
// request and fetch API
const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
