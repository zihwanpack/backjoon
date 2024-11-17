const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split(/\s+/).map(Number);

const usage = input.slice(1);

const calculateYCost = (cost) => Math.floor(cost / 30) * 10 + 10;
const calculateMCost = (cost) => Math.floor(cost / 60) * 15 + 15;

let yCost = 0;
let mCost = 0;

usage.forEach((cost) => {
  yCost += calculateYCost(cost);
  mCost += calculateMCost(cost);
});

if (yCost < mCost) console.log('Y', yCost);
else if (yCost > mCost) console.log('M', mCost);
else console.log('Y M', yCost);
