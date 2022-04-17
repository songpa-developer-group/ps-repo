from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [0 for _ in range(numCourses)]
        dic = {}
        for x, y in prerequisites:
            if x not in dic:
                dic[x] = []
            dic[x].append(y)

        def dfs(k):

            if visited[k] == 1:
                return True
            elif visited[k] == -1:
                return False

            # 방문 중
            visited[k] = -1

            if k in dic:
                for j in dic[k]:
                    if not dfs(j):
                        return False

            visited[k] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))
