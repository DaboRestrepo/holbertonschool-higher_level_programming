#!/usr/bin/node
const process = require('process');
const myNumber = Number(process.argv[2]);
if (!(myNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNumber; i++) {
    let row = '';
    for (let j = 0; j < myNumber; j++) {
      row += 'X';
    }
    console.log(row + '');
  }
}
