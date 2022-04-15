# 1 <= m, n <= 25
# 1 is live , 0 is dead
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        LIFE, DEAD = 1, 0
        DY, DX = [1, 1, 1, -1, -1, -1, 0, 0], [1, 0, -1, 1, 0, -1, 1, -1]
        R, C = len(board), len(board[0])
        next_board = [[DEAD for _ in range(C)] for _ in range(R)]
        for y in range(R):
            for x in range(C):
                cnt = 0
                for i in range(8):
                    n_y, n_x = y + DY[i], x + DX[i]
                    if 0 <= n_y < R and 0 <= n_x < C and board[n_y][n_x] == LIFE:
                        cnt += 1
                if board[y][x] == LIFE:
                    if cnt < 2:
                        next_board[y][x] = DEAD
                    elif cnt == 2 or cnt == 3:
                        next_board[y][x] = LIFE
                    else:
                        next_board[y][x] = DEAD
                else:
                    if cnt == 3:
                        next_board[y][x] = LIFE
        for y in range(R):
            for x in range(C):
                board[y][x] = next_board[y][x]
