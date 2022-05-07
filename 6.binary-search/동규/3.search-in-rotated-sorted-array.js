// https://leetcode.com/problems/search-in-rotated-sorted-array/

var search = function (nums, target) {
  let left = 0,
    right = nums.length - 1;
  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;
    // When middle element is less than the last element
    if (nums[mid] < nums[right]) {
      if (target > nums[mid] && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    // When middle element is greater than the last element
    else {
      if (target > nums[mid] || target < nums[left]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
  }
  return left;
};
