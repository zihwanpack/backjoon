'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n');

const [queueInfo, idxArr] = input;

const [N, M] = queueInfo.split(' ').map(Number);
const numIndexArr = idxArr.split(' ').map(Number);
const ringBuffer = Array.from({ length: N }).map((_, i) => i + 1);
let result = 0;

for (let num of numIndexArr) {
  if (ringBuffer[0] === num) {
    ringBuffer.shift();
    // num 건너뛰기
    continue;
  } else if (ringBuffer.indexOf(num) > ringBuffer.length / 2) {
    while (ringBuffer[0] !== num) {
      ringBuffer.unshift(ringBuffer.pop());
      result++;
    }
    ringBuffer.shift();
  } else {
    while (ringBuffer[0] !== num) {
      ringBuffer.push(ringBuffer.shift());
      result++;
    }
    ringBuffer.shift();
  }
}

console.log(result);
