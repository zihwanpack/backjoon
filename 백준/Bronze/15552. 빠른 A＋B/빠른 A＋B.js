const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const count = Number(input[0]);
let result = '';

for (let i = 1; i < count + 1; i++) {
  let num = input[i].split(' ');
  result += Number(num[0]) + Number(num[1]) + '\n';
}
console.log(result);
