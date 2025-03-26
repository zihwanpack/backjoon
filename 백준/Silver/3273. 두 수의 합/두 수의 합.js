'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n');

let n = Number(input[0]);
let arr = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
let x = Number(input[2]);

let p1 = 0;
let p2 = n - 1;
let result = 0;
while (p1 < p2) {
  const sum = arr[p1] + arr[p2];
  if (sum === x) {
    result++;
    p1++;
    p2--;
  } else if (sum < x) {
    p1++;
  } else {
    p2--;
  }
}
console.log(result);
