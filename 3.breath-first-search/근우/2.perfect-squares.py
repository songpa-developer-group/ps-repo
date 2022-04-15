from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        is_visit = [False for _ in range(10 ** 4)]
        is_visit[n] = True
        squared_list = [k * k for k in range(1, 101)]
        que = deque([[0, n]])  ## count, cur_number
        while que:
            cnt, num = que.popleft()
            if num == 0:
                return cnt
            for c in squared_list:
                next_num = num - c
                if next_num < 0:
                    break
                if is_visit[next_num]:
                    continue
                is_visit[next_num] = True
                que.append([cnt + 1, next_num])
