## https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
from re import T


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = TreeNode()
        cursor = res
        def _inorderTraversal(root):
            nonlocal cursor
            if root:
                _inorderTraversal(root.left)
                cursor.right = TreeNode(root.val)
                cursor = cursor.right
                _inorderTraversal(root.right)

        _inorderTraversal(root)
        return res.right