// https://leetcode.com/problems/binary-tree-right-side-view/

var rightSideView = function (root) {
  if (!root) return [];
  var array = [];
  search(root, 1);

  function search(root, level) {
    if (root) {
      if (array.length < level) {
        array.push(root.val);
      }
      search(root.right, level + 1);
      search(root.left, level + 1);
    } else {
      return;
    }
  }
  return array;
};
