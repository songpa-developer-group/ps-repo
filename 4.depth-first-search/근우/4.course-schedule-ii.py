# ## https://leetcode.com/problems/course-schedule-ii/
# # 1 <= numCourses <= 2000
# # 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# # prerequisites[i].length == 2
# # a1, b1 b1 is prerequisite of a1
# # Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# # Output: [0, 2, 1, 3]
# # 선행조건들 나열
# # 현재 들을 수 있는 과목들 담기
# # 현재 과목을 들으면서 들을 수 있는 과목들 담기
from collections import defaultdict, deque
from email.policy import default
from functools import reduce
from re import A
from typing import List


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_bits_by_course = defaultdict(int)
        can_not_listen_courses = set()
        
        for a, b in prerequisites:
            pre_bits_by_course[a] |= 1 << b
            can_not_listen_courses.add(a)

        can_listens = list(
            filter(
                lambda a: pre_bits_by_course[a] == 0,
                [i for i in range(numCourses)],
            )
        )
        can_listens_bits = reduce(
            lambda a, b: a + (1 << b),
            can_listens,
            0,
        )

        while True:
            next_can_not_listen_courses = set()
            for c in can_not_listen_courses:
                cur = pre_bits_by_course[c]
                if cur & can_listens_bits == cur:
                    can_listens_bits |= (1 << c)
                    can_listens.append(c)
                else:
                    next_can_not_listen_courses.add(c)
            if next_can_not_listen_courses == can_not_listen_courses:
                break
            can_not_listen_courses = next_can_not_listen_courses
        return can_listens if len(can_listens) == numCourses else []


from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []