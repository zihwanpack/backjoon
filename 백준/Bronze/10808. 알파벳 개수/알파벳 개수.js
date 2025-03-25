'use strict';
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const outputPath = './output.txt';
let input = require('fs').readFileSync(path).toString().trim();
// let output = require('fs').readFileSync(outputPath, { encoding: 'utf8' });
const arr = Array.from({ length: 26 }, () => 0);

const alphabetInput = input.split('');
alphabetInput.forEach((alphabet) => {
  arr[alphabet.charCodeAt() - 97]++;
});

console.log(arr.join(' '));
