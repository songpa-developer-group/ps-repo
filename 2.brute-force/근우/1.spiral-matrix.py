from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        DY = [0, 1, 0, -1]
        DX = [1, 0, -1, 0]
        is_visit = [[False for _ in range(C)] for _ in range(R)]
        ans = [matrix[0][0]]
        is_visit[0][0] = True
        st = [[0, 0, 0]]  # y, x ,cur_dir
        while st:
            c_y, c_x, c_dir = st.pop()
            for i in range(4):
                n_dir = (c_dir + i) % 4
                n_y, n_x = c_y + DY[n_dir], c_x + DX[n_dir]
                if 0 <= n_y < R and 0 <= n_x < C and not is_visit[n_y][n_x]:
                    is_visit[n_y][n_x] = True
                    ans.append(matrix[n_y][n_x])
                    st.append([n_y, n_x, n_dir])
                    break
        return ans
