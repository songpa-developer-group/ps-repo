## https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import heapq


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = defaultdict(int)
        for i in nums:
            counter_map[i] += 1
        min_hq = []
        for num, cnt in counter_map.items():
            heapq.heappush(min_hq, (cnt, num))
            if len(min_hq) == k + 1:
                heapq.heappop(min_hq)
        res = []
        while min_hq:
            res.append(heapq.heappop(min_hq)[1])
        return res

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
