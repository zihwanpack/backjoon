const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const year = require('fs').readFileSync(path).toString().trim();

year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0) ? console.log(1) : console.log(0);
