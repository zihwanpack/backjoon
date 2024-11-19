class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

function insertAfter(node, value) {
  const newNode = new Node(value);
  newNode.prev = node;
  newNode.next = node.next;
  if (node.next) {
    node.next.prev = newNode;
  }
  node.next = newNode;
  return newNode;
}

function deleteNode(node) {
  if (node.prev) {
    node.prev.next = node.next;
  }
  if (node.next) {
    node.next.prev = node.prev;
  }
}

const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');
const str = input[0];
const n = Number(input[1]);
const list = input.slice(2).map((el) => el.split(' '));

// 연결 리스트 초기화
const head = new Node(null);
let cursor = head;

// 초기 문자열 넣기
for (let i = 0; i < str.length; i++) {
  cursor = insertAfter(cursor, str[i]);
}

// 명령 처리
for (let i = 0; i < n; i++) {
  const [cmd, char] = list[i];
  if (cmd === 'P') {
    cursor = insertAfter(cursor, char);
  } else if (cmd === 'L' && cursor.prev) {
    cursor = cursor.prev;
  } else if (cmd === 'D' && cursor.next) {
    cursor = cursor.next;
  } else if (cmd === 'B' && cursor.prev) {
    const prevNode = cursor.prev;
    deleteNode(cursor);
    cursor = prevNode;
  }
}

// 결과 출력
let result = [];
let currentNode = head.next;
while (currentNode) {
  result.push(currentNode.value);
  currentNode = currentNode.next;
}
console.log(result.join(''));
