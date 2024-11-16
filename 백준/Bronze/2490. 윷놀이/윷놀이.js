const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const dataArr = input.map((el) =>
  el
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b)
);

const resultArr = [];

dataArr.forEach((data) => {
  let bellyCount = 0;
  let backCount = 0;
  data.forEach((datum) => {
    if (datum === 0) bellyCount++;
    else if (datum === 1) backCount++;
  });

  if (bellyCount === 1) resultArr.push('A');
  else if (bellyCount === 2) resultArr.push('B');
  else if (bellyCount === 3) resultArr.push('C');
  else if (bellyCount === 4) resultArr.push('D');
  else if (backCount === 4) resultArr.push('E');
});

resultArr.forEach((result) => {
  console.log(result);
});
