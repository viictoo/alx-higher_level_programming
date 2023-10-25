#!/usr/bin/node
// request and fetch API
// ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) { console.error("error") }
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (completed[todo.userId] === undefined && todo.completed) {
        completed[todo.userId] = 1;
      } else if (todo.completed) { completed[todo.userId] += 1; }
    });
    console.log(completed);
});
