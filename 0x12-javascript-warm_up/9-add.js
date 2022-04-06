#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const process = require('process');
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
