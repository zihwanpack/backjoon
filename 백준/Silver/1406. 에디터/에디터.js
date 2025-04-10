'use strict';
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(path).toString().trim().split('\n');
const str = input[0];
const N = Number(input[1]);
const list = input.slice(2).map((str) => str.split(' '));

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

const head = new Node(null);
let cursor = head;

for (let i = 0; i < str.length; i++) {
  cursor = insertAfter(cursor, str[i]);
}

for (let j = 0; j < N; j++) {
  const [cmd, data] = list[j];
  if (cmd === 'P') {
    cursor = insertAfter(cursor, data);
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

let result = [];
let currentNode = head.next;
while (currentNode) {
  result.push(currentNode.value);
  currentNode = currentNode.next;
}
console.log(result.join(''));
