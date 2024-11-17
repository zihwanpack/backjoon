const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const arr = Array(26).fill(0);

for (let i = 0; i < input.length; i++) {
  arr[input.charCodeAt(i) - 97]++;
}
console.log(...arr);
