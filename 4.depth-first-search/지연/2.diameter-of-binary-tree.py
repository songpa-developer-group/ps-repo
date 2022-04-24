# https://leetcode.com/problems/diameter-of-binary-tree/


from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        if not root:
            return 0

        def treeLength(root):
            tree_left = treeLength(root.left)
            tree_right = treeLength(root.right)
            self.length = max(self.length, tree_left + tree_right)
            return max(tree_left, tree_right) + 1

        treeLength(root)
        return self.length
