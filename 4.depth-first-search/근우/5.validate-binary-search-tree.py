## https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
from collections import deque
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower_bound, upper_bound,node):
            if not node:
                return True
            if lower_bound<node.val<upper_bound:
                return all([dfs(lower_bound,node.val,node.left),dfs(node.val,upper_bound,node.right)])    
            return False
        return dfs(-sys.maxsize,sys.maxsize,root) 
    