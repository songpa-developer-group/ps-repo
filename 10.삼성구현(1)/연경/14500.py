# https://www.acmicpc.net/problem/14500

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

