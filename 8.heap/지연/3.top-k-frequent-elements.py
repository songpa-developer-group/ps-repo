# https://leetcode.com/problems/top-k-frequent-elements/

import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequent_nums = collections.Counter(nums).most_common(k)
        # return [f[0] for f in frequent_nums]

        freq_nums = collections.Counter(nums)
        freq_heap = []

        print(freq_nums)

        for f in freq_nums:
            heapq.heappush(freq_heap, (-(freq_nums[f]), f))

        print(freq_heap)

        return [heapq.heappop(freq_heap)[1] for _ in range(k)]
