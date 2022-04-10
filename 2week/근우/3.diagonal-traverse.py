from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = [mat[0][0]]
        DY, DX = [-1, 1], [1, -1]
        R, C = len(mat), len(mat[0])
        MAX_COUNT = R * C
        UP_DIAGNOL_DIR, DOWN_DIAGNOL_DIR = 0, 1
        c_y, c_x, c_dir = 0, 0, UP_DIAGNOL_DIR
        while len(ans) != MAX_COUNT:
            n_y, n_x = c_y + DY[c_dir], c_x + DX[c_dir]
            if not (0 <= n_y < R and 0 <= n_x < C):
                if c_dir == UP_DIAGNOL_DIR:
                    if n_x < C:
                        n_y, n_x = c_y, c_x + 1
                    else:
                        n_y, n_x = c_y + 1, c_x
                else:
                    if n_y < R:
                        n_y, n_x = c_y + 1, c_x
                    else:
                        n_y, n_x = c_y, c_x + 1
                c_dir = (c_dir + 1) % 2
            c_y, c_x = n_y, n_x
            ans.append(mat[c_y][c_x])
        return ans


Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
