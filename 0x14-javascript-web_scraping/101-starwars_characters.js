#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  if (!movie.characters || movie.characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError || charResponse.statusCode !== 200) {
        console.error('Error fetching character data:', charError);
        process.exit(1);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
