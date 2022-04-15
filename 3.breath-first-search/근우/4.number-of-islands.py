from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        DY, DX = [0, 0, 1, -1], [1, -1, 0, 0]
        WATER, LAND = "0", "1"
        cnt = 0
        is_visit = [[False for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == WATER or is_visit[r][c]:
                    continue
                is_visit[r][c] = True
                cnt += 1
                que = deque([(r, c)])
                while que:
                    y, x = que.popleft()
                    for i in range(4):
                        ny, nx = y + DY[i], x + DX[i]
                        if (
                            0 <= ny < R
                            and 0 <= nx < C
                            and grid[ny][nx] == LAND
                            and not is_visit[ny][nx]
                        ):
                            is_visit[ny][nx] = True
                            que.append((ny, nx))

        return cnt


Solution().numIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)
