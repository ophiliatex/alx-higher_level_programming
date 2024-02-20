#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status Code:', response.statusCode);
    } else {
      const film = JSON.parse(body);
      film.characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Status Code:', charResponse.statusCode);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    }
  });
}

// Check if the movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);

