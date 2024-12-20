const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = require('fs').readFileSync(path).toString().trim().split('\n');

const [N, ...commands] = input;

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Deque {
  constructor() {
    this.length = 0;
    this.front = null;
    this.rear = null;
  }

  isEmpty() {
    return this.length === 0;
  }

  append(value) {
    const newNode = new Node(value);
    if (this.isEmpty()) {
      this.front = this.rear = newNode;
    } else {
      this.rear.next = newNode;
      this.rear = newNode;
    }
    this.length++;
  }

  appendLeft(value) {
    const newNode = new Node(value);
    if (this.isEmpty()) {
      this.front = this.rear = newNode;
    } else {
      newNode.next = this.front;
      this.front = newNode;
    }
    this.length++;
  }

  pop() {
    if (this.isEmpty()) return -1;

    // 노드가 하나일 때 처리
    if (this.front === this.rear) {
      const dequeuedValue = this.rear.value;
      this.front = this.rear = null;
      this.length--;
      return dequeuedValue;
    }

    // 두 개 이상일 때 처리
    let current = this.front;
    while (current.next !== this.rear) {
      current = current.next;
    }
    const dequeuedValue = this.rear.value;
    this.rear = current;
    this.rear.next = null;
    this.length--;
    return dequeuedValue;
  }

  popLeft() {
    if (this.isEmpty()) return -1;

    const dequeuedValue = this.front.value;
    this.front = this.front.next;
    // 큐에 노드 1개인 경우
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

const deque = new Deque();
const results = []; // 결과를 저장할 배열

commands.forEach((commandLine) => {
  const [command, value] = commandLine.split(' ');

  switch (command) {
    case 'push_front':
      deque.appendLeft(value);
      break;
    case 'push_back':
      deque.append(value);
      break;
    case 'pop_front':
      results.push(deque.popLeft());
      break;
    case 'pop_back':
      results.push(deque.pop());
      break;
    case 'size':
      results.push(deque.size());
      break;
    case 'empty':
      results.push(deque.empty());
      break;
    case 'front':
      results.push(deque.frontValue());
      break;
    case 'back':
      results.push(deque.backValue());
      break;
  }
});

// 결과를 한 번에 출력
console.log(results.join('\n'));
