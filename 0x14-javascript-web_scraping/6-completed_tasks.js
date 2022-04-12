#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const tasks = {};
    for (const index in data) {
      if (data[index].completed === true) {
        if (tasks[data[index].userId] === undefined) {
          tasks[data[index].userId] = 1;
        } else {
          tasks[data[index].userId]++;
        }
      }
    }
    console.log(tasks);
  }
});
