// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

// sol 1
var kthSmallest = function (matrix, k) {
  const arr = matrix.reduce((acc, cur) => {
    return acc.concat(cur);
  });
  arr.sort((a, b) => a - b);
  return arr[k - 1];
};

// var kthSmallest = function (matrix, k) {
//   let left = matrix[0][0];
//   let right = matrix[matrix.length - 1][matrix.length - 1];

//   while (left <= right) {
//     const middle = (left + right) / 2 + left;
//     const potentialMatch = matrix[middle];
//     if (k === potentialMatch) {
//       return middle;
//     } else if (k < potentialMatch) {
//       right = middle - 1;
//     } else {
//       left = middle + 1;
//     }
//   }
//   return left;
// };
