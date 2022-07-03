## https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def find(matrix, mid, length):
            _row = 0
            _col = length - 1
            cnt = 0

            while _row < length and _col >= 0:
                if matrix[_row][_col] <= mid:
                    _row += 1
                    cnt += (_col + 1)
                else:
                    _col -= 1
            return cnt

        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        while start <= end:
            mid = (start + end) // 2
            count = find(matrix, mid, n)
            if count < k:
                start = mid + 1
            else:
                end = mid - 1
        return start


if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,19]]
    k = 8
    print(Solution().kthSmallest(matrix, k))
