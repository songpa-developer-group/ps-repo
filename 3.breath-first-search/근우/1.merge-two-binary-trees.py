# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        merged_node_root = TreeNode(0)
        if not root1 and not root2:
            return None
        que = deque([])
        que.append([merged_node_root, root1, root2])
        while que:
            root, node1, node2 = que.popleft()
            root.val = (node1.val if node1 else 0) + (node2.val if node2 else 0)

            node_1_left = node1.left if node1 and node1.left else None
            node_1_right = node1.right if node1 and node1.right else None
            node_2_left = node2.left if node2 and node2.left else None
            node_2_right = node2.right if node2 and node2.right else None

            l_node = TreeNode() if node_1_left or node_2_left else None
            r_node = TreeNode() if node_1_right or node_2_right else None

            if l_node:
                root.left = l_node
                que.append([l_node, node_1_left, node_2_left])
            if r_node:
                root.right = r_node
                que.append([r_node, node_1_right, node_2_right])
        return merged_node_root
