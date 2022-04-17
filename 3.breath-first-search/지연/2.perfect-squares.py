from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        squared_list = [k * k for k in range(101)]
        is_visit = [False for _ in range(10 ** 4)]
        que = deque([(0, 0)])
        while que:
            count, cur_num = que.popleft()
            if cur_num == n:
                return count
            else:
                for sqrt in squared_list:
                    next_num = cur_num + sqrt
                    if next_num > n:
                        break
                    else:
                        if is_visit[next_num]:
                            continue
                        is_visit[next_num] = True
                        que.append((count + 1, next_num))


print(Solution().numSquares(12))
