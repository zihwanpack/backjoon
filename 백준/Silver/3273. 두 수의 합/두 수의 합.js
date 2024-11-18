const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');
const [n, arr, targetData] = input;

const numArr = arr
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

let count = 0;

const twoSum = (arr, target) => {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === target) {
      count++;
      left++;
      right--;
    } else if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
};

const target = Number(targetData);

twoSum(numArr, target);

console.log(count);
