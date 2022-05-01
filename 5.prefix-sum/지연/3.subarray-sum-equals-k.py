# https://leetcode.com/problems/subarray-sum-equals-k/\

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], sums: int) -> int:
        cnt = 0
        prefix_sum = 0
        dict = {0: 1}

        for num in nums:
            prefix_sum = prefix_sum + num

            if prefix_sum-sums in dict:
                cnt = cnt + dict[prefix_sum-sums]

            if prefix_sum not in dict:
                dict[prefix_sum] = 1
            else:
                dict[prefix_sum] = dict[prefix_sum]+1

        return cnt


print(Solution().subarraySum([1, 2, 3], 3))
