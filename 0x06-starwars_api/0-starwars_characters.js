#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
'use strict';

const request = require('request');

function getCharactersArray() {
    const movieId = process.argv[2];
    const apiLink = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    request(apiLink, { json: true }, (error, response, body) => {
        if (error) {
            return console.error('Error:', error);
        }
        if (response.statusCode !== 200) {
            return console.error('Failed to retrieve movie:', response.statusCode);
        }
        const characterArray = body.characters;
        printCharacterNames(characterArray, 0);
    });
}

// Fetch and print all movie character names recursively
function printCharacterNames(characterArray, index) {
    if (index >= characterArray.length) {
        return;
    }

    const characterLink = characterArray[index];
    request(characterLink, { json: true }, (error, response, body) => {
        if (error) {
            return console.error('Error:', error);
        }
        if (response.statusCode !== 200) {
            return console.error('Failed to retrieve character:', response.statusCode);
        }
        console.log(body.name);
        printCharacterNames(characterArray, index + 1);
    });
}

getCharactersArray();
