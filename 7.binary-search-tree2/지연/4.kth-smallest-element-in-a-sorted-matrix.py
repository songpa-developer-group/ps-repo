# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row_len, col_len = len(matrix), len(matrix[0])
        new_list = []

        if(len(matrix) <= 1):
            return matrix[0][0]
        for row in range(row_len):
            for col in range(col_len):
                new_list.append(matrix[row][col])

        new_list.sort()
        return new_list[k - 1]
