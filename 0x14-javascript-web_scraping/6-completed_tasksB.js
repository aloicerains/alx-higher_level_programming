#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = JSON.parse(body);
  const dict = {};
  let userId = 1;
  let noCompleted = 0;
  while (userId <= 10) {
    for (const task of tasks) {
      if (userId === task.userId) {
        if (task.completed === true) {
          noCompleted += 1;
        }
      }
    }
    dict[userId] = noCompleted;
    userId += 1;
    noCompleted = 0;
  }
  console.log(dict);
});
