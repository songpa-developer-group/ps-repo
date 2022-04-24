# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order_by_depth = []

        if not root:
            return order_by_depth

        que = deque([root])
        while que:
            current_depth_nodes = []

            while que:
                current_depth_nodes.append(que.popleft())

            order_by_depth.append(
                [node.val for node in current_depth_nodes]
            )

            for cur_node in current_depth_nodes:
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

        return order_by_depth
