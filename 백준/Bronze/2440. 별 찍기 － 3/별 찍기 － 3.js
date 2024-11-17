const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const number = Number(input);

for (let i = number; i > 0; i--) {
  console.log('*'.repeat(i));
}
