// https://leetcode.com/problems/search-a-2d-matrix/

var searchMatrix = function (matrix, target) {
  var n = matrix.length;
  var m = (matrix[0] || []).length;
  var left = 0;
  var right = n * m - 1;
  var mid = 0;
  var tmp = 0;
  while (left <= right) {
    mid = left + Math.floor((right - left) / 2);
    tmp = matrix[Math.floor(mid / m)][mid % m];
    if (tmp === target) {
      return true;
    } else if (tmp > target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return false;
};
