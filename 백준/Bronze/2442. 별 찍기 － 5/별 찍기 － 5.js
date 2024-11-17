const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const number = Number(input);

for (let i = 1; i <= number; i++) {
  console.log(' '.repeat(number - i) + '*'.repeat(i * 2 - 1));
}
