// https://leetcode.com/problems/diameter-of-binary-tree/
function diameterOfBinaryTree(root) {
  if (!root) return 0;
  let result = -1;
  let getH = function (node, h) {
    if (!node) return 0;
    let left_H = getH(node.left);
    let right_H = getH(node.right);
    result = Math.max(result, 1 + left_H + right_H);
    return 1 + Math.max(left_H, right_H);
  };
  getH(root);
  return result - 1;
}
