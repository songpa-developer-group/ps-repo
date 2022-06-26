# https://leetcode.com/problems/top-k-frequent-elements/

import collections
import heapq
from typing import List


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        frequent_nums = collections.Counter(nums).most_common(k)
        return [f[0] for f in frequent_nums]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        freq_nums = collections.Counter(nums)
        freq_heap = []

        for f in freq_nums:
            heapq.heappush(freq_heap, (-(freq_nums[f]), f))

        return [heapq.heappop(freq_heap)[1] for _ in range(k)]


print(Solution().topKFrequent1([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent2([1, 1, 1, 2, 2, 3, 3, 3, 3, 4], 2))
