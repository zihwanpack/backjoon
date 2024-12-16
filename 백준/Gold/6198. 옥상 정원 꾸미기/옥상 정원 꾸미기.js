const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split(/\s+/).map(Number);

const [N, ...buildings] = input.map(Number);

const stack = [];
let result = 0;

for (let i = 0; i < N; i++) {
  let now = buildings[i];
  while (stack.length > 0 && stack[stack.length - 1] <= now) {
    stack.pop();
  }
  stack.push(now);
  result += stack.length - 1;
}
console.log(result);
