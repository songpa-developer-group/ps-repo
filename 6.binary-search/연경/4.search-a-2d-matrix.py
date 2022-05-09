## https://leetcode.com/problems/search-a-2d-matrix/
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        s, e = 0, row * col - 1

        while s <= e:
            m = (s + e) // 2

            val = matrix[m // col][m % col]
            if val == target:
                return True
            elif val < target:
                s = m + 1
            elif val > target:
                e = m - 1

        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(Solution().searchMatrix(matrix, target))