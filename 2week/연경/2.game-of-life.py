from typing import List
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        _board = copy.deepcopy(board)
        r = len(_board)
        c = len(_board[0])
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, -1, -1, -1, 0, 1, 1, 1]

        for i in range(r):
            for j in range(c):

                live, die = 0, 0
                for k in range(8):
                    _x = j + dx[k]
                    _y = i + dy[k]

                    if 0 <= _x < c and 0 <= _y < r:
                        if _board[_y][_x] == 1:
                            live += 1
                        else:
                            die += 1

                if _board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1

        return board

if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print(Solution().gameOfLife(board))