const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const [N, X] = input[0].split(' ').map(Number);
const numArr = input[1].split(' ').map(Number);
const result = numArr.filter((num) => num < X);

console.log(result.join(' '));
