'use strict';
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const outputPath = './output.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n').map(Number);
// let output = require('fs').readFileSync(outputPath, { encoding: 'utf8' });
const arr = Array.from({ length: 10 }, () => 0);
let product = 1;

// 곱연산
for (let i = 0; i < input.length; i++) {
  product *= input[i];
}

const productArr = product.toString().split('').map(Number);
for (let j = 0; j < productArr.length; j++) {
  arr[productArr[j]]++;
}

console.log(arr.join('\n'));
