# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq


def solution(jobs):
    answer, now, cnt = 0, 0, 0
    start = -1
    heap = []

    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            cnt += 1
        else:
            now += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [4, 3], [10, 3]]))
print(solution([[0, 10], [2, 3], [9, 3]]))
