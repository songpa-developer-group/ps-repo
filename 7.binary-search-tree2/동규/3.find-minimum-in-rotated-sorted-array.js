// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

// sol 1
var findMin = function (nums) {
  nums.sort((a, b) => a - b);
  return nums[0];
};

// sol 2
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);

    if (nums[right] >= nums[mid]) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return nums[left];
};
