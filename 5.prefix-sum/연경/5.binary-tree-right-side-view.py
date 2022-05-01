## https://leetcode.com/problems/binary-tree-right-side-view/
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        queue = deque()
        if root:
            queue.append(root)
        while queue:
            last = None
            for _ in range(len(queue)):
                n = queue.popleft()
                last = n
                if n.left != None:
                    queue.append(n.left)
                if n.right != None:
                    queue.append(n.right)
            answer.append(last.val)
        return answer

if __name__ == "__main__":
    root = [1, 2, 3, None, 5, None, 4]
    print(Solution().rightSideView(root))