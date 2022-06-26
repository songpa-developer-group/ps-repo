# https://www.acmicpc.net/problem/14500

import sys; input = sys.stdin.readline

def dfs(board, total):
    global ans
    if len(board) == 4:
        ans = max(ans, total)
        return
    for block in board:
        for dy,dx in zip([1,0],[0,1]):
            nblock = [block[0] + dy, block[1] + dx]
            if 0 <= nblock[0] < N and 0 <= nblock[1] < M and visit[nblock[0]][nblock[1]] == 0:
                visit[nblock[0]][nblock[1]] = 1
                dfs(board + [nblock], total + arr[nblock[0]][nblock[1]])
                visit[nblock[0]][nblock[1]] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs([[r, c]], arr[r][c])
        visit[r][c] = 0

print(ans)



# -*- coding: utf-8 -*-
# 시작시간 11시 07분
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
answer = 0
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(0,N):
    board[i] = list(map(int, readline().split()))
# 2 + 1+ 8 + 4 + 4 = 17개 17*2500
tetrominos = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],

    [[0, 0], [0, 1], [1, 0], [1, 1]],

    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[1, 0], [1, 1], [1, 2], [0, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],

    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[2, 0], [1, 0], [1, 1], [0, 1]],
    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],

    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 1], [1, 1], [2, 1], [1, 0]],
]

for tetromino in tetrominos:
    for y in range(N):
        for x in range(M):
            next_tetromino = tetromino.copy()
            for i in range(4):
                next_tetromino[i]=(tetromino[i][0]+y,tetromino[i][1]+x)
            if all([0 <= bar[0] < N and 0 <= bar[1] < M for bar in next_tetromino]):
                answer = max(answer, sum(
                    [board[bar[0]][bar[1]] for bar in next_tetromino]))
            else:
                break
print(answer)
