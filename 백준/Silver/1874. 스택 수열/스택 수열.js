const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n').map(Number);

const [n, ...sequence] = input;
const stack = [];
let result = '';
let count = 1;

// n번 반복문
for (let i = 0; i < n; i++) {
  while (count <= sequence[i]) {
    stack.push(count);
    result += '+';
    count++;
  }
  let number = stack.pop();
  if (number !== sequence[i]) {
    result = 'NO';
    break;
  }
  result += '-';
}

if (result === 'NO') return console.log('NO');

console.log(result.split('').join('\n'));
