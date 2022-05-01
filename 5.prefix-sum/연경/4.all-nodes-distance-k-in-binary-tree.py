## https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import List
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        answer = []
        graph = defaultdict(list)
        

        return answer



if __name__ == "__main__":
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    target = 5
    k = 2
    print(Solution().distanceK(root, target, k))