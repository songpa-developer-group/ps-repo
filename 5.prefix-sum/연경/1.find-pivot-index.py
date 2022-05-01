## https://leetcode.com/problems/find-pivot-index/
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        answer = -1
        sum_f = [0 for _ in range(len(nums))]
        sum_b = [0 for _ in range(len(nums))]

        size = len(nums)
        for i in range(size-1, -1, -1):
            sum_b[i] = nums[i] + (sum_b[i+1] if i+1 < size else 0)
        for i in range(size):
            sum_f[i] = nums[i] + (sum_f[i-1] if i > 0 else 0)
            if sum_f[i] == sum_b[i]:
                answer = i
                break
        return answer

if __name__ == "__main__":
    nums = [2, 1, -1]
    print(Solution().pivotIndex(nums))