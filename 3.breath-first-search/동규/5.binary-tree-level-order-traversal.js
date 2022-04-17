function levelOrder(root) {
  const res = [];
  if (root === null) return res;

  const queue = [];
  queue.push(root);
  while (queue.length !== 0) {
    let size = queue.length;
    let level = [];
    while (size--) {
      let cur = queue.shift();
      level.push(cur.val);
      if (cur.left) queue.push(cur.left);
      if (cur.right) queue.push(cur.right);
    }
    res.push(level.concat());
  }
  return res;
}

levelOrder([3, 9, 20, null, null, 15, 7]);
