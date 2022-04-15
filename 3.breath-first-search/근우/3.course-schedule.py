from collections import deque
from typing import List

# 1 <= numCourses <= 10**5
# 0 <= prerequisites.length <= 5000
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        is_already_completed = [False for _ in range(numCourses)]
        precourses_by_course = {}
        for c, p in prerequisites:
            if c not in precourses_by_course:
                precourses_by_course[c] = []
            precourses_by_course[c].append(p)

        num = 0
        while True:
            next_num = num
            for n in range(numCourses):
                if is_already_completed[n]:
                    continue
                if not n in precourses_by_course or all(
                    [is_already_completed[c] for c in precourses_by_course[n]]
                ):
                    is_already_completed[n] = True
                    next_num += 1
            if num == next_num:
                break
            num = next_num
        return num == numCourses


Solution().canFinish(2, [[1, 0], [0, 1]])
