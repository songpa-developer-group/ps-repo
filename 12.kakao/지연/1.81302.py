# https://programmers.co.kr/learn/courses/30/lessons/81302/

def solution(places):
    LIMIT = 2
    MAX = len(places)

    def check_distance(place):
        def check_places(col, row, depth, visited):
            if depth > LIMIT:
                return False
            if depth > 0 and places[row][col] == 'P':
                return True
            for dy, dx in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                ny, nx = col + dy, row + dx
                if ny < 0 or nx < 0 or ny <= MAX or nx <= MAX or visited[col][row] or places[col][row] == 'X':
                    continue
                visited[ny][nx] = True
                if check_places(ny, nx, depth + 1, visited):
                    return True
                visited[ny][nx] = False
            return False
        for col in range(MAX):
            for row in range(MAX):
                if place[col][row] == 'P':
                    depth = 0
                    visited = [[False for _ in range(5)] for _ in range(5)]
                    visited[col][row] = True
                    if check_places(col, row, depth, visited):
                        return 0
        return 1
    return [check_distance(place) for place in places]


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
         "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
