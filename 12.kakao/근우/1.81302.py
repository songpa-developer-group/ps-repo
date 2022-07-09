## https://programmers.co.kr/learn/courses/30/lessons/81302/

def solution(places):
    assert len(places[0]) == len(places) == 5
    def _check_keep_distance(place):
        def _check_near_P(y,x,depth,is_visit):
            if depth == 3:
                return False
            if depth>0 and place[y][x] == 'P':
                return True
            for dy ,dx in zip([1,-1,0,0],[0,0,1,-1]):
                ny ,nx = y +dy, x + dx
                if ny < 0 or ny >=5 or nx < 0 or nx >=5 or is_visit[ny][nx] or place[ny][nx] == 'X':
                    continue
                is_visit[ny][nx] = True
                if _check_near_P(ny,nx,depth+1,is_visit):
                    return True
                is_visit[ny][nx] = False
            return False
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    is_visit = [[False for _ in range(5)] for _ in range(5)]
                    is_visit[y][x] = True
                    if _check_near_P(y,x,0,is_visit):
                        return 0
        return 1
    return [_check_keep_distance(p) for p in places]

assert solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]) == [1,0,1,1,1]