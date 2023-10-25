#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];

request(apiURL, (err, response, body) => {
  if (err) console.error(err);

  const todosList = JSON.parse(body);
	//console.log(todosList);
  const output = {};
  todosList.forEach((todo) => {
      //console.log(todo.completed);
      if (todo.completed === true) {
	 // console.log(output[todo.userId] || 0)
      	//output[todo.userId] = (output[todo.userId] || 0) + 1
	 if (output[todo.userId] === undefined) {output[todo.userId] = 1}
	 else {
      	output[todo.userId] = (output[todo.userId] + 1)}
  }})
  console.log(output);
});
