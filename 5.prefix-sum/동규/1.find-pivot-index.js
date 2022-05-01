// https://leetcode.com/problems/find-pivot-index/

var pivotIndex = function (nums) {
  var sum,
    count = 0;
  if (nums === null) return -1;
  sum = nums.reduce((a, b) => a + b);

  for (let i = 0; i < nums.length; i++) {
    if (!nums[i - 1]) nums[i - 1] = 0;
    count += nums[i - 1];
    sum -= nums[i];
    if (sum === count) return i;
  }
  return -1;
};
