class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
    }

    add(value) {
        this.heap.push(value);
        this.bubbleUp();
    }

    poll() {
        if (this.size() === 0) return undefined;
        if (this.size() === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.bubbleDown();
        return min;
    }

    bubbleUp() {
        let idx = this.size() - 1;
        let parentIdx = Math.floor((idx - 1) / 2);

        while (idx > 0 && this.heap[idx] < this.heap[parentIdx]) {
            this.swap(idx, parentIdx);
            idx = parentIdx;
            parentIdx = Math.floor((idx - 1) / 2);
        }
    }

    bubbleDown() {
        let idx = 0;
        let leftChildIdx, rightChildIdx, smallerChildIdx;

        while (true) {
            leftChildIdx = 2 * idx + 1;
            rightChildIdx = 2 * idx + 2;
            smallerChildIdx = leftChildIdx;

            if (rightChildIdx < this.size() && this.heap[rightChildIdx] < this.heap[leftChildIdx]) {
                smallerChildIdx = rightChildIdx;
            }

            if (smallerChildIdx >= this.size() || this.heap[idx] <= this.heap[smallerChildIdx]) break;

            this.swap(idx, smallerChildIdx);
            idx = smallerChildIdx;
        }
    }

    peek() {
        return this.heap[0];
    }
}

function solution(scoville, K) {
    let answer = 0;
    const minHeap = new MinHeap();

    for (let num of scoville) {
        minHeap.add(num);
    }

    while (minHeap.size() >= 2 && minHeap.peek() < K) {
        const first = minHeap.poll();
        const second = minHeap.poll();
        const mixedScov = first + second * 2;
        minHeap.add(mixedScov);
        answer++;
    }

    return minHeap.peek() < K ? -1 : answer;
}
