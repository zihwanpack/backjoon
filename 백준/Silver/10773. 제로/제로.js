const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n').map(Number);

input.shift();

const stack = [];

input.forEach((num) => {
  num !== 0 ? stack.push(num) : stack.pop();
});

console.log(stack.reduce((acc, cur) => acc + cur, 0));
