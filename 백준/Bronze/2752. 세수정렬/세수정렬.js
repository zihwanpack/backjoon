const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const numbers = input
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
console.log(numbers.join(' '));
