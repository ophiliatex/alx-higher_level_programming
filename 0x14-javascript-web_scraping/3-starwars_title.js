#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
