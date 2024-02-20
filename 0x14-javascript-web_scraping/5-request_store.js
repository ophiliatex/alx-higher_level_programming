#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    // pass
  } else {
    fs.writeFile(path, body, 'utf-8', function (err) {
      if (err) {
        // pass
      }
    });
  }
});
