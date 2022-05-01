## https://leetcode.com/problems/product-of-array-except-self/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1 for _ in range(len(nums))]
        n = 1
        for i in range(len(nums)):
            answer[i] = n
            n *= nums[i]

        n = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= n
            n *= nums[i]

        return answer

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums))