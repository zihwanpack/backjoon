'use strict';
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

let result = [];

for (let string of input) {
  if (string === '.') break; // 입력 종료 조건
  const stack = [];
  let isBalanced = true;

  for (let char of string) {
    if (char === '(' || char === '[') {
      stack.push(char); // 왼쪽 괄호를 스택에 추가
    } else if (char === ')') {
      if (stack.length > 0 && stack[stack.length - 1] === '(') {
        stack.pop(); // 짝이 맞는 경우 스택에서 제거
      } else {
        isBalanced = false; // 짝이 맞지 않는 경우
        break;
      }
    } else if (char === ']') {
      if (stack.length > 0 && stack[stack.length - 1] === '[') {
        stack.pop(); // 짝이 맞는 경우 스택에서 제거
      } else {
        isBalanced = false; // 짝이 맞지 않는 경우
        break;
      }
    }
  }

  // 스택이 비어 있고 균형이 맞는 경우
  if (isBalanced && stack.length === 0) {
    result.push('yes');
  } else {
    result.push('no');
  }
}

console.log(result.join('\n'));
