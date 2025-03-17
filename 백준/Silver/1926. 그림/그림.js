'use strict';
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs
  .readFileSync(path)
  .toString()
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

const [n, k] = input[0];
const arr = input.slice(1);
const dx = [0, 0, 1, -1]; // 상하좌우
const dy = [1, -1, 0, 0];

const visited = Array.from({ length: n }, () => Array(k).fill(false));
const BFS = (x, y) => {
  let queue = [[x, y]];
  visited[x][y] = true;
  let size = 1;
  while (queue.length !== 0) {
    const [curX, curY] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = curX + dx[i];
      const ny = curY + dy[i];
      if (nx >= 0 && nx < n && ny >= 0 && ny < k) {
        if (arr[nx][ny] === 1 && !visited[nx][ny]) {
          visited[nx][ny] = true;
          queue.push([nx, ny]);
          size++;
        }
      }
    }
  }
  return size;
};

let count = 0;
let maxSize = 0;

for (let i = 0; i < n; i++) {
  for (let j = 0; j < k; j++) {
    if (arr[i][j] === 1 && !visited[i][j]) {
      count++;
      maxSize = Math.max(maxSize, BFS(i, j));
    }
  }
}

console.log(count);
console.log(maxSize);
