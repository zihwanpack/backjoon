'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const [N, ...brackets] = input;
let result = [];

for (let bracket of brackets) {
  const stack = [];
  let isBalanced = true;

  for (let char of bracket) {
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      if (stack.length > 0 && stack[stack.length - 1] === '(') {
        stack.pop();
      } else {
        isBalanced = false;
        break;
      }
    }
  }

  isBalanced && stack.length === 0 ? result.push('YES') : result.push('NO');
}

console.log(result.join('\n'));
