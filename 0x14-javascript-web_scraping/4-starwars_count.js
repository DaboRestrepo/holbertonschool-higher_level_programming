#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const result = JSON.parse(body).results;
    for (const data in result) {
      const character = result[data].characters;
      for (const char in character) {
        if (character[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
