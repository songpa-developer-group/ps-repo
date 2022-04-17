from collections import deque
from typing import List

'''
class Solution:
    
    def dfs(self, grid: List[List[str]], i, j):

        if i < 0 or i >= len(grid) \
          or j < 0 or j >= len(grid[0]) \
              or grid[i][j] != "1" :
          return

        grid[i][j] = 0
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
          return 0

        count = 0
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if grid[i][j] == "1":
              self.dfs(grid, i, j)
              count += 1

        return count
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        # row(y), col(x)
        row, col = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if visited[i][j]:
                    continue
                if grid[i][j] == '0':
                    continue
                count += 1
                visited[i][j] = True
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= nx < col and 0 <= ny < row and grid[ny][nx] == '1' and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((ny, nx))
        return count

if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))