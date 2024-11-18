const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');
const [n, arr, targetData] = input;

const numArr = arr
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

let count = 0;
const target = Number(targetData);

numArr.forEach((num) => {
  if (num === target) count++;
});

console.log(count);
