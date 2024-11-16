const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const oddNums = [];
let sum = 0;
const numbers = input.map(Number);

numbers.forEach((number) => {
  if (number % 2 === 1) {
    sum += number;
    oddNums.push(number);
  }
});

if (sum === 0) {
  console.log(-1);
} else {
  console.log(sum);
  console.log(Math.min(...oddNums));
}
