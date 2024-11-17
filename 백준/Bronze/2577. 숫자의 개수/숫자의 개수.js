const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const array = Array(10).fill(0);

const [A, B, C] = input.map(Number);
const multipleResult = A * B * C;

const splitArr = [...String(multipleResult)].map(Number);
splitArr.forEach((el) => array[el]++);

array.forEach((el) => console.log(el));
