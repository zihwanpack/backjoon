const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

let average = 0;
const numbers = input.map(Number);

average = numbers.reduce((acc, cur) => (acc += cur / numbers.length), 0);

const sortedNum = numbers.sort((a, b) => a - b);

console.log(average);
console.log(sortedNum[2]);
