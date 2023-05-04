#!/usr/bin/node
// starwars_characters.js
// starwars_characters is a Node script that prints all characters of a Star Wars movies.

const request = require('request');
const { promisify } = require('util');

const filmURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

(async () => {
  try {
    const res = await promisify(request)(filmURL);
    const { characters } = JSON.parse(res.body);

    const characterPromises = characters.map(url => promisify(request)(url));
    const characterResponses = await Promise.all(characterPromises);

    const characterNames = characterResponses.map(response => JSON.parse(response.body).name);
    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error(error);
  }
})();
