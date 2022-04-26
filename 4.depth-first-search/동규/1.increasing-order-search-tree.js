// https://leetcode.com/problems/increasing-order-search-tree/
function increasingBST(root) {
  let ans = new TreeNode(0);
  let cur = ans;
  function inorder(node) {
    if (node === null) return;
    inorder(node.left);
    node.left = null;
    cur.right = node;
    cur = node;
    inorder(node.right);
  }
  inorder(root);
  return ans.right;
}
