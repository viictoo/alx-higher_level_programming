#!/usr/bin/node
// request and fetch API
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (completed[todo.userId] === undefined && todo.completed) {
        completed[todo.userId] = 1;
      } else if (todo.completed) { completed[todo.userId] += 1; }
    });
    console.log(completed);
  }
});
