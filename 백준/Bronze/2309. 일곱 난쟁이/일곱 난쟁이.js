const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const numbers = input.map(Number);
const total = numbers.reduce((acc, cur) => (acc += cur), 0);
const target = total - 100;

for (let i = 0; i < numbers.length; i++) {
  for (let j = i + 1; j < numbers.length; j++) {
    if (numbers[i] + numbers[j] === target) {
      const result = numbers.filter((_, idx) => idx !== i && idx !== j).sort((a, b) => a - b);
      result.forEach((num) => console.log(num));
      return;
    }
  }
}
