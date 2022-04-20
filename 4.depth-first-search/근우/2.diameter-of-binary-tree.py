## https://leetcode.com/problems/diameter-of-binary-tree/
# depth가 가장 깊은 노드에서 다른노드까지 탐색 그리디하게 접근
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        ## node.depth 추가
        def get_depth(node):
            if not node:
                return 0
            if not node.left and not node.right:
                node.depth = 0
            else:
                node.depth = 1 + max(get_depth(node.left), get_depth(node.right))
            return node.depth

        ## diameter구하기
        def get_max_diameter(node):
            nonlocal answer
            left_depth = 1 + node.left.depth if node.left else 0
            right_depth = 1 + node.right.depth if node.right else 0
            if node.left:
                get_max_diameter(node.left)
            if node.right:
                get_max_diameter(node.right)
            answer = max(answer, left_depth + right_depth)

        get_depth(root)
        get_max_diameter(root)
        return answer


class Solution2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter
