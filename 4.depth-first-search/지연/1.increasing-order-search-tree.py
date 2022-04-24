# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree = TreeNode()
        node = tree

        def inorder(root):
            nonlocal node
            if root:
                inorder(root.left)
                node.right = TreeNode(root.val)
                node = node.right
                inorder(root.right)
        inorder(root)
        return tree.right
