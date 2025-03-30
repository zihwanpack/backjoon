const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

let input = require('fs').readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());

function checkStrfry(str1, str2) {
  return str1.split('').sort().join('') === str2.split('').sort().join('')
    ? console.log('Possible')
    : console.log('Impossible');
}

for (let i = 0; i < N; i++) {
  const [firstStr, secondStr] = input[i].split(' ');
  checkStrfry(firstStr, secondStr);
}
