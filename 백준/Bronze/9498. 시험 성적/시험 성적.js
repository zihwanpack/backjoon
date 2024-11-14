const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const number = Number(input);

if (number > 89) {
  console.log('A');
} else if (number > 79) {
  console.log('B');
} else if (number > 69) {
  console.log('C');
} else if (number > 59) {
  console.log('D');
} else {
  console.log('F');
}
