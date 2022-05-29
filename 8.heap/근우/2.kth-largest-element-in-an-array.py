## https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heapify
import heapq


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        limit_heap_size = len(nums) - k + 1
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) == limit_heap_size + 1:
                heapq.heappop(max_heap)

        return - max_heap[0]
