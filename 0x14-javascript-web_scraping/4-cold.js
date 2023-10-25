#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
	//-1 remove title
  const count = body.split('/people/18/').length - 1;
//	console.log(body.split('/people/18/'))
  console.log(count);
});
