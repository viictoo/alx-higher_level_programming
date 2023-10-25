#!/usr/bin/node
// request and fetch API

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const results = JSON.parse(body).results;
    const count = results.reduce((total, film) => {
	//console.log(total)
	 //   console.log(film)

      const characters = film.characters;
	   // console.log(characters)
      const matchingCharacters = characters.filter(character => character.includes('/18/'));
	 //   console.log(total)
	return total + matchingCharacters.length;
    }, 0);

    console.log(count);
  }
});
