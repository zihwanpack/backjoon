const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

input.shift();

function stringSort(data) {
  return data.split('').sort().join('');
}

input.forEach((data) => {
  const [x, y] = data.split(' ');
  const sortedX = stringSort(x);
  const sortedY = stringSort(y);
  if (sortedX === sortedY) {
    console.log('Possible');
  } else {
    console.log('Impossible');
  }
});
