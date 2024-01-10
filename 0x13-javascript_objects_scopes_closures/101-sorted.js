#!/usr/bin/node
const arg = require('./101-data').dict;
const arg1 = {};
for (const key in arg) {
  if (arg1[arg[key]] === undefined) {
    arg1[arg[key]] = [key];
  } else {
    arg1[arg[key]].push(key);
  }
}
console.log(arg1);
