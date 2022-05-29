# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, (-num, num))

        for _ in range(k):
            kth_max = heapq.heappop(heap)[1]
        return kth_max
