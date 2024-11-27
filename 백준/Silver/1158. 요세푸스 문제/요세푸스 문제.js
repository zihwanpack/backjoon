function josephusProblem(N, K) {
  const people = Array.from({ length: N }, (_, i) => i + 1);
  const result = [];
  let index = 0;
  while (people.length) {
    index = (index + K - 1) % people.length;
    result.push(people.splice(index, 1)[0]);
  }
  return result;
}

const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(filePath).toString().trim().split(' ');
let [N, K] = input.map(Number);

const result = josephusProblem(N, K);
console.log(`<${result.join(', ')}>`);
