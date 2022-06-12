# https://leetcode.com/problems/last-stone-weight/

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) <= 1):
            return stones[0]

        heap = []

        for num in stones:
            heapq.heappush(heap, (-num, num))

        print(heap)  # stones array => max_heap

        while len(heap) > 1:
            s1 = heapq.heappop(heap)[1]
            s2 = heapq.heappop(heap)[1]
            if s1 - s2 == 0:
                if len(heap) > 0:
                    continue
                else:
                    return 0
            heapq.heappush(heap, (-(s1 - s2), s1 - s2))

        return heapq.heappop(heap)[1]


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
