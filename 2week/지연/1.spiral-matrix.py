from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        row_start_idx = 0
        row_end_idx = len(matrix) - 1     # 2

        col_start_idx = 0
        col_end_idx = len(matrix[0]) - 1  # 3

        while (row_start_idx <= row_end_idx and col_start_idx <= col_end_idx):
            for i in range(col_start_idx, col_end_idx + 1):        # 0, 4
                result.append(matrix[row_start_idx][i])            # 1, 2, 3, 4
            row_start_idx += 1                                     # 1

            for i in range(row_start_idx, row_end_idx + 1):        # 1, 3
                result.append(matrix[i][col_end_idx])              # 8, 12
            col_end_idx -= 1                                       # 2

            if (row_start_idx <= row_end_idx):                       # 1 <= 2
                for i in range(col_end_idx, col_start_idx - 1, -1):  # 2, 1, 0
                    result.append(matrix[row_end_idx][i])           # 11, 10, 9
                row_end_idx -= 1                                    # 1

            if (col_start_idx <= col_end_idx):                       # 0 <= 2
                for i in range(row_end_idx, row_start_idx - 1, -1):  # 1, 0
                    result.append(matrix[i][col_start_idx])          # 5
                col_start_idx += 1                                   # 1

        return result


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
