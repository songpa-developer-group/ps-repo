// https://leetcode.com/problems/last-stone-weight/

//sol 1
var lastStoneWeight = function (stones) {
  while (stones.length > 1) {
    let s1 = Math.max(...stones);
    stones.splice(stones.indexOf(s1), 1);
    let s2 = Math.max(...stones);
    stones.splice(stones.indexOf(s2), 1);
    if (s1 != s2) {
      stones.push(s1 - s2);
    }
  }
  return stones.length > 0 ? stones[0] : 0;
};

//sol 2
function lastStoneWeight(stones) {
  const heap = new MaxHeap();
  heap.build(stones);
  while (heap.size() > 1) {
    const top1 = heap.removeTop(),
      top2 = heap.removeTop();
    heap.add(top1 - top2);
  }
  return heap.top();
}
class Heap {
  constructor() {
    this.data = [];
    this.property = "MAX";
  }
  build(arr) {
    // O(n)
    this.data = [...arr];
    const n = this.size();
    for (let i = Math.floor(n / 2) - 1; i >= 0; --i) {
      this.heapifyTopToBottom(i);
    }
  }
  heapifyTopToBottom(idx) {
    // O(logn)
    const l = 2 * idx + 1,
      r = 2 * idx + 2;
    let p = idx;
    if (l < this.size() && this.compare(l, p)) {
      p = l;
    }
    if (r < this.size() && this.compare(r, p)) {
      p = r;
    }
    if (p !== idx) {
      [this.data[idx], this.data[p]] = [this.data[p], this.data[idx]];
      this.heapifyTopToBottom(p);
    }
  }
  heapifyBottomToTop(idx) {
    // O(logn)
    const parent = Math.floor((idx - 1) / 2);
    if (this.compare(idx, parent)) {
      [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
      this.heapifyBottomToTop(parent);
    }
  }
  compare(idx1, idx2) {
    switch (this.property) {
      case "MAX":
        return this.data[idx1] > this.data[idx2];
      case "MIN":
        return this.data[idx1] < this.data[idx2];
    }
  }
  size() {
    return this.data.length;
  }
  top() {
    return this.data[0];
  }
  removeTop() {
    // O(logn)
    [this.data[0], this.data[this.size() - 1]] = [
      this.data[this.size() - 1],
      this.data[0],
    ];
    const top = this.data.pop();
    this.heapifyTopToBottom(0);
    return top;
  }
  add(value) {
    // O(logn)
    this.data.push(value);
    this.heapifyBottomToTop(this.size() - 1);
  }
}
class MaxHeap extends Heap {
  constructor() {
    super("MAX");
  }
}
