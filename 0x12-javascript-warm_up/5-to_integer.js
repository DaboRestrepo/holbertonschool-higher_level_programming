#!/usr/bin/node
const process = require('process');
const myNumber = Number(process.argv[2]);
if (!(myNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNumber);
}
