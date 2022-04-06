#!/usr/bin/node
const process = require('process');
if ((process.argv).length <= 3) {
  console.log('0');
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
