#!/usr/bin/node
const process = require('process');
const myNumber = Number(process.argv[2]);
if (!(myNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < myNumber; index++) {
    console.log('C is fun');
  }
}
