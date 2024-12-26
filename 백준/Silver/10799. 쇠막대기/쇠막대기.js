'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const brackets = input.join('');
let result = 0;

const stack = [];
for (let i = 0; i < brackets.length; i++) {
  if (brackets[i] === '(') {
    stack.push(brackets[i]);
  } else {
    stack.pop();
    if (brackets[i - 1] === '(') {
      // 레이저인 경우
      result += stack.length;
    } else {
      // ))인 경우
      result++;
    }
  }
}

console.log(result);
