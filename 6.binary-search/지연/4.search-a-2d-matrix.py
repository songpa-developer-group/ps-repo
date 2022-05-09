# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx, col_idx = len(matrix), len(matrix[0])
        start, end = 0, (row_idx * col_idx) - 1

        while start <= end:
            mid = (start + end) // 2
            cur_idx = matrix[mid//col_idx][mid % col_idx]

            if (cur_idx == target):
                return True

            if (cur_idx < target):
                start = mid + 1
            else:
                end = mid - 1
        return False


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
