    const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n');

const [N, ...commands] = input;

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.length = 0;
    this.front = null;
    this.rear = null;
  }

  isEmpty() {
    return this.length === 0;
  }

  enqueue(value) {
    const newNode = new Node(value);
    if (this.isEmpty()) {
      this.front = this.rear = newNode;
    } else {
      this.rear.next = newNode;
      this.rear = newNode;
    }
    this.length++;
  }

  dequeue() {
    if (this.isEmpty()) return -1;

    const dequeuedValue = this.front.value;
    this.front = this.front.next;
    if (!this.front) this.rear = null;
    this.length--;
    return dequeuedValue;
  }

  size() {
    return this.length;
  }

  empty() {
    return this.isEmpty() ? 1 : 0;
  }

  frontValue() {
    return this.isEmpty() ? -1 : this.front.value;
  }

  backValue() {
    return this.isEmpty() ? -1 : this.rear.value;
  }
}

const queue = new Queue();
const results = []; // 결과를 저장할 배열

commands.forEach((commandLine) => {
  const [command, value] = commandLine.split(' ');

  switch (command) {
    case 'push':
      queue.enqueue(value);
      break;
    case 'pop':
      results.push(queue.dequeue());
      break;
    case 'size':
      results.push(queue.size());
      break;
    case 'empty':
      results.push(queue.empty());
      break;
    case 'front':
      results.push(queue.frontValue());
      break;
    case 'back':
      results.push(queue.backValue());
      break;
  }
});

// 결과를 한 번에 출력
console.log(results.join('\n'));
