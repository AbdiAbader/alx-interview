#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
const req = require('request');
const { promisify } = require('util');
const urls = 'https://swapi-api.alx-tools.com/api/' + process.argv[2];

(async () => {
  try {
    const res = await promisify(req)(urls);
    const { characters } = JSON.parse(res.body);

    const characterPromises = characters.map(url => promisify(res)(url));
    const reses = await Promise.all(characterPromises);

    const cnames = reses.map(response => JSON.parse(response.body).name);
    console.log(cnames.join('\n'));
  } catch (error) {
    console.error(error);
  }
})();
