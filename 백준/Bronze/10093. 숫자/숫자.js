const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split(' ');

const [A, B] = input.map(Number).sort((a, b) => a - b);

if (A === B || A + 1 === B) {
  console.log(0);
  return;
}

console.log(B - A - 1);
const arr = [];
for (let i = A + 1; i < B; i++) {
  arr.push(i);
}

console.log(...arr.map(Number));
