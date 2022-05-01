## https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        count = defaultdict(int)

        p = 0
        for num in nums:
            p += num
            if p == k:
                answer += 1

            if p-k in count:
                answer += count[p-k]
            count[p] += 1
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    print(Solution().subarraySum(nums, k))