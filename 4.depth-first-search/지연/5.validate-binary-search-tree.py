# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list = []

        def inorder(root, list):
            if root:
                inorder(root.left, list)
                list.append(root.val)
                inorder(root.right, list)
        inorder(root, list)

        for i in range(1, len(list)):
            if list[i-1] >= list[i]:
                return False
        return True
