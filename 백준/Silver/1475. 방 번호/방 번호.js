const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const set = Array(10).fill(0);

const number = input.split('').map(Number);

number.forEach((el) => {
  set[el]++;
});



set[6] = Math.ceil((set[6] + set[9]) / 2);
set[9] = 0;

const max = Math.max(...set);

console.log(max);
