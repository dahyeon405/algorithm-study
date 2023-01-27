class Minheap {
  constructor() {
    this.heap = [];
  }
  add(n) {
    this.heap.push(n);
    let i = this.heap.length - 1;

    while (i > 0) {
      let par = Math.floor((i - 1) / 2);
      if (this.heap[par] > n) {
        this.heap[i] = this.heap[par];
        i = par;
      } else break;
    }
    this.heap[i] = n;
  }

  pop() {
    if (this.empty()) return false;
    const popped = this.heap[0];
    if (this.heap.length === 1) {
      this.heap = [];
      return popped;
    }

    const lastEl = this.heap.pop();

    let i = 0;
    while (2 * i + 1 < this.heap.length) {
      let child_1 = 2 * i + 1;
      if (2 * i + 2 < this.heap.length && this.heap[2 * i + 2] < this.heap[child_1]) {
        child_1 = 2 * i + 2;
      }
      if (lastEl > this.heap[child_1]) {
        this.heap[i] = this.heap[child_1];
        i = child_1;
      } else break;
    }
    this.heap[i] = lastEl;

    return popped;
  }

  empty() {
    if (this.heap.length === 0) return true;
    return false;
  }

  top() {
    return this.heap[0];
  }
}

class Maxheap {
  constructor() {
    this.heap = [];
  }
  add(n) {
    this.heap.push(n);
    let i = this.heap.length - 1;

    while (i > 0) {
      let par = Math.floor((i - 1) / 2);
      if (this.heap[par] < n) {
        this.heap[i] = this.heap[par];
        i = par;
      } else break;
    }
    this.heap[i] = n;
  }

  pop() {
    if (this.empty()) return false;
    const popped = this.heap[0];
    if (this.heap.length === 1) {
      this.heap = [];
      return popped;
    }
    const lastEl = this.heap.pop();

    let i = 0;
    while (2 * i + 1 < this.heap.length) {
      let child_1 = 2 * i + 1;
      if (2 * i + 2 < this.heap.length && this.heap[2 * i + 2] > this.heap[child_1]) {
        child_1 = 2 * i + 2;
      }
      if (lastEl < this.heap[child_1]) {
        this.heap[i] = this.heap[child_1];
        i = child_1;
      } else break;
    }
    this.heap[i] = lastEl;

    return popped;
  }

  empty() {
    if (this.heap.length === 0) return true;
    return false;
  }

  top() {
    return this.heap[0];
  }
}

function solution(operations) {
  const minHeap = new Minheap();
  const maxHeap = new Maxheap();
  const numbers = {};

  operations.forEach((op) => {
    let [o, num] = op.split(" ");
    const n = Number(num);
    if (o === "I") {
      minHeap.add(n);
      maxHeap.add(n);
      if (numbers[n]) numbers[n]++;
      else numbers[n] = 1;
    } else if (num === "-1") {
      while (!minHeap.empty() && numbers[minHeap.top()] === 0) minHeap.pop();
      let popped = minHeap.pop();
      numbers[popped]--;
    } else if (num === "1") {
      while (!maxHeap.empty() && numbers[maxHeap.top()] === 0) maxHeap.pop();
      let popped = maxHeap.pop();
      numbers[popped]--;
    }
  });

  while (!maxHeap.empty() && numbers[maxHeap.top()] === 0) maxHeap.pop();
  const max = maxHeap.empty() ? 0 : maxHeap.pop();

  while (!minHeap.empty() && numbers[minHeap.top()] === 0) minHeap.pop();
  const min = minHeap.empty() ? 0 : minHeap.pop();

  return [max, min];
}
