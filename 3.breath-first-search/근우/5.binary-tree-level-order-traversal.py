# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        root.depth = 0
        que = deque([root])
        nodes = [root]
        while que:
            c = que.popleft()
            if c.left:
                c.left.depth = c.depth + 1
                nodes.append(c.left)
                que.append(c.left)
            if c.right:
                c.right.depth = c.depth + 1
                nodes.append(c.right)
                que.append(c.right)
        max_depth = nodes[-1].depth
        res = [[] for _ in range(max_depth + 1)]
        for n in nodes:
            res[n.depth].append(n.val)
        return res
