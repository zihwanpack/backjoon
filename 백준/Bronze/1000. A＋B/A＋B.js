const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim();

const [A, B] = input.split(' ').map(Number);
const result = A + B;

console.log(result);
