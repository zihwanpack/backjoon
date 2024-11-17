const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split(' ');

const [F, S, T] = input.map(Number).sort((a, b) => a - b);

if (F === S && S === T) {
  console.log(10000 + F * 1000);
} else if (F === S || S === T) {
  console.log(1000 + S * 100);
} else console.log(T * 100);
