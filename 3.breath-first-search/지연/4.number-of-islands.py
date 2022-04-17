from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        ROW_IDX = len(grid)
        COL_IDX = len(grid[0])

        DY = [0, 0, 1, -1]
        DX = [1, -1, 0, 0]

        visited = [[False for _ in range(COL_IDX)]for _ in range(ROW_IDX)]
        land_nums = 0

        for row in range(ROW_IDX):
            for col in range(COL_IDX):

                if(grid[row][col] == LAND and visited[row][col] == False):
                    visited[row][col] = True
                    que = deque([(row, col)])
                    land_nums += 1

                    while que:
                        y, x = que.popleft()
                        for i in range(4):
                            ny, nx = y + DY[i], x + DX[i]
                            if (
                                0 <= ny < ROW_IDX and
                                0 <= nx < COL_IDX and
                                visited[ny][nx] == False and
                                grid[ny][nx] == LAND
                            ):
                                que.append((ny, nx))
                                visited[ny][nx] = True

        return land_nums


print(Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
