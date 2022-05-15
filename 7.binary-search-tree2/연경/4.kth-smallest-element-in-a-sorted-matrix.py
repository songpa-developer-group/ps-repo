## https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        row, col = len(matrix), len(matrix[0])
        start, end = 0, row * col - 1
        answer = end
        while start <= end:
            mid = (start + end) // 2
            r, c = mid // col, mid % col

        return


if __name__ == "__main__":
    matrix = [[1, 5, 9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8
    print(Solution().kthSmallest(matrix, k))
