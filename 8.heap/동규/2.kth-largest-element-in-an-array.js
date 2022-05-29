// https://leetcode.com/problems/kth-largest-element-in-an-array/

//sol 1
var findKthLargest = (nums, k) => {
  nums.sort((a, b) => b - a);
  return nums[k - 1];
};

//sol 2
var findKthLargest = function (nums, k) {
  nums = buildHeap(nums);
  for (let i = 1; i < k; i++) {
    nums[0] = nums[nums.length - 1];
    nums.pop();
    nums = heapify(0, nums);
  }
  return nums[0];
};

function buildHeap(nums) {
  for (let i = Math.floor(nums.length / 2); i >= 0; i--) {
    nums = heapify(i, nums);
  }
  return nums;
}

function heapify(i, nums) {
  let l = Left(i);
  let r = Right(i);
  let largest;

  if (l < nums.length && nums[l] > nums[i]) {
    largest = l;
  } else {
    largest = i;
  }

  if (r < nums.length && nums[r] > nums[largest]) {
    largest = r;
  }

  if (largest != i) {
    let temp = nums[i];
    nums[i] = nums[largest];
    nums[largest] = temp;

    return heapify(largest, nums);
  }

  return nums;
}

function Left(i, nums) {
  return i * 2 + 1;
}
function Right(i, nums) {
  return i * 2 + 2;
}
