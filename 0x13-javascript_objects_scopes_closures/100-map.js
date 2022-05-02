#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newArr = list.map((element, index) => element * index);
console.log(newArr);
