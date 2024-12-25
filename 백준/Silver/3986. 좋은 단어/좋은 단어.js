'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const [N, ...words] = input;

let result = 0;

for (let i = 0; i < N; i++) {
  const word = words[i];
  if (word.length % 2 === 0) {
    const stack = [];
    for (let char of word) {
      stack[stack.length - 1] === char ? stack.pop() : stack.push(char);
    }
    stack.length === 0 && result++;
  }
}

console.log(result);
