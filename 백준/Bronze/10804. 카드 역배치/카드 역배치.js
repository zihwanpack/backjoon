const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const array = Array.from({ length: 20 }, (_, i) => i + 1);

const changeArr = (A, B) => {
  const partialArr = array.slice(A - 1, B).reverse();
  array.splice(A - 1, B - A + 1, ...partialArr);
};

input.forEach((el) => {
  const [A, B] = el.split(' ').map(Number);
  changeArr(A, B);
});

console.log(...array);
