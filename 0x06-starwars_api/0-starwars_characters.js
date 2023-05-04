#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
const req = require('request');

// dealing command line arguments
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js [film_id]');
  process.exit(1);
} else {
  const urls = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  req.get(urls, (err, res, body) => {
    if (err) {
      console.log(err);
    } else if (res.statusCode !== 200) {
      console.error('Error:', response.statusCode, response.statusMessage);
    } else {
      character = JSON.parse(body).characters;
      for (let i = 0; i < character.length; i++) {
        req.get(character[i], (err, res, body) => {
          if (err) {
            console.log(err);
          } else if (res.statusCode !== 200) {
            console.error('Error:', response.statusCode, response.statusMessage);
          } else {
            console.log(JSON.parse(body).name);
          }
        }
        );
      }
    }
  });
}
