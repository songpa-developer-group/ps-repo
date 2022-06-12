# https://leetcode.com/problems/cheapest-flights-within-k-stops/

import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n, flights, start_point, end_point, stops):
        dicts = collections.defaultdict(dict)
        for curr_node, next_node, price in flights:
            dicts[curr_node][next_node] = price

        # Min-heap to store minimum weight edge at top.
        heap = [(0, start_point, stops + 1)]

        # Track nodes which are included in MST.
        visited = [0] * n

        while heap:
            price, idx, stops = heapq.heappop(heap)
            if idx == end_point:
                return price
            if visited[idx] >= stops:
                continue
            visited[idx] = stops
            for curr_stops, dict_price in dicts[idx].items():
                heapq.heappush(
                    heap, (price + dict_price, curr_stops, stops - 1))
        return -1


print(Solution().findCheapestPrice(4,
                                   [[0, 1, 100], [1, 2, 100], [2, 0, 100],
                                    [1, 3, 600], [2, 3, 200]],
                                   0,
                                   3,
                                   1))
