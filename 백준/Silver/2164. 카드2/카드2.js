const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim();

const N = Number(input);

const queue = Array(N)
  .fill()
  .map((v, i) => i + 1);

let front = 0;
while (queue.length - front > 1) {
  front++;
  queue.push(queue[front]);
  front++;
}

console.log(queue[front]);
