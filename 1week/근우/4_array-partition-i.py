from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i in range(0, len(nums), 2):
            answer += nums[i]
        return answer


print(Solution().arrayPairSum([1, 4, 3, 2]))
