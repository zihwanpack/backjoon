const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(path)
  .toString()
  .trim()
  .split('\n')
  .map((data) => data.split(' ').map(Number));

const [_, target] = input.shift();
let answer = 0;

const room = Array.from({ length: 6 }, () => [0, 0]);

input.forEach((student) => {
  const [gender, grade] = student;
  room[grade - 1][gender]++;
});

room.forEach((data) => {
  const numOfGirl = data[0];
  const numOfBoy = data[1];
  answer += Math.ceil(numOfGirl / target);
  answer += Math.ceil(numOfBoy / target);
});
console.log(answer);
