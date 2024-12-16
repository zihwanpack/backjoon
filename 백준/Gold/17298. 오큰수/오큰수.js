const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split(/\s+/).map(Number);

const [N, ...numbers] = input;

const stack = [];
const result = Array(N).fill(-1);

for (let i = 0; i < N; i++) {
  const currentNumber = numbers[i];
  // 아직 오큰수 못찾은 경우
  while (stack.length > 0 && numbers[stack[stack.length - 1]] < currentNumber) {
    // 오큰수 할당
    result[stack.pop()] = currentNumber;
  }
  stack.push(i);
}
console.log(result.join(' '));
