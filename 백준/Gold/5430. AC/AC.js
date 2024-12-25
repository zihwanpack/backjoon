'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n');

const [T, ...testCase] = input;
const result = [];

for (let i = 0; i < T * 3; i += 3) {
  let isReverse = false;
  let isError = false;
  const p = testCase[i];
  const n = Number(testCase[i + 1]);
  let array = JSON?.parse(testCase[i + 2]);

  for (let command of p) {
    if (command === 'R') {
      isReverse = !isReverse;
    } else if (command === 'D') {
      if (array.length === 0) {
        isError = true;
        break;
      }
      isReverse ? array.pop() : array.shift();
    }
  }
  isError ? result.push('error') : result.push(JSON.stringify(isReverse ? array.reverse() : array));
}

console.log(result.join('\n'));
