# https://www.acmicpc.net/problem/14500
from collections import dequeœ

import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if idx == 3:
        ans = max(ans, total)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
            visit[nr][nc] = 1
            dfs(nr, nc, idx + 1, total + arr[nr][nc])
            visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)