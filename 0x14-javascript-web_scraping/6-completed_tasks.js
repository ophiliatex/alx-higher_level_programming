#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    // pass
  }
  const tasks = JSON.parse(body);
  const dic = {};

  for (const task of tasks) {
    if (task.dic && dic[task.userId] === undefined) {
      dic[task.userId] = 1;
    } else if (task.dic) {
      dic[task.userId]++;
    }
  }

  console.log(dic);
});
