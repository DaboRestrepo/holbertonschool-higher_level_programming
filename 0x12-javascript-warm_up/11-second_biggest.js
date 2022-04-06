#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort((a, b) => a - b);
  console.log(list.reverse()[1]);
}
