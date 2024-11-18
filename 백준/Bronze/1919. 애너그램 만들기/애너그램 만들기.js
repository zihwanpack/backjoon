const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(path)
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(''));

const [x, y] = input;
let count = 0;

while (x.length > 0) {
  const target = x.shift();
  const index = y.findIndex((el) => el === target);
  index >= 0 ? y.splice(index, 1) : count++;
}

count += y.length;
console.log(count);
