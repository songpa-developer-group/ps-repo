// https://leetcode.com/problems/product-of-array-except-self/

var productExceptSelf = function (nums) {
  let result = [];
  let lp = 1,
    rp = 1;
  for (let i = 0; i < nums.length; i++) {
    result.push(lp);
    lp *= nums[i];
  }
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= rp;
    rp *= nums[i];
  }
  return result;
};
