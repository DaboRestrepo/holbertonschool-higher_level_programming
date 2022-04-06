#!/usr/bin/node
function factorial (a) {
  if (!(a)) {
    return 1;
  } else {
    if (a === 0) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
}
const process = require('process');
console.log(factorial(Number(process.argv[2])));
