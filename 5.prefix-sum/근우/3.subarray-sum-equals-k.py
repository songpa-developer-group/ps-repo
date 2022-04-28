## https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
from email.policy import default


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sum_map = defaultdict(int)
        cur_sum = 0
        for num in nums:
            cur_sum +=num
            if cur_sum == k:
                cnt+=1
            cnt += sum_map[cur_sum - k]
            sum_map[cur_sum] += 1
        return cnt