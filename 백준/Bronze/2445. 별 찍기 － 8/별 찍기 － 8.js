const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const number = Number(input);

for (let i = 1; i <= number; i++) {
  console.log('*'.repeat(i) + ' '.repeat((number - i) * 2) + '*'.repeat(i));
}

for (let i = number - 1; i >= 1; i--) {
  console.log('*'.repeat(i) + ' '.repeat((number - i) * 2) + '*'.repeat(i));
}
