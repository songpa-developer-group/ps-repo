# https://leetcode.com/problems/network-delay-time/

import collections
import heapq
from typing import List

# FIXME!


class Solution:
    def networkDelayTime(self, times: List[List[int]], end_point: int, start_point: int) -> int:
        dicts = collections.defaultdict(dict)
        for curr_node, next_node, distance in times:
            dicts[curr_node][next_node] = distance

        # Min-heap to store minimum weight edge at top.
        heap = [(0, start_point)]

        # Track nodes which are included in MST.
        visited = [False] * end_point

        mst_cnt = len(times)

        while heap:
            distance, idx = heapq.heappop(heap)
            if idx == end_point:
                return distance

            if visited[idx]:
                continue
            visited[idx] = True
            for curr_node, dict_distance in dicts[idx].items():
                heapq.heappush(
                    heap, (distance + dict_distance, curr_node))
            mst_cnt - 1
        return -1


print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
# print(Solution().networkDelayTime([[1, 2, 1]], 2, 2))
# print(Solution().networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))
# print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))
