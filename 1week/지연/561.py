# Minimum element gets add into the result in sacrifice of maximum element.

class Solution:
    def arrayPairSum(self, nums):
        pairSum = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            pairSum += nums[i]
        return pairSum


print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))
