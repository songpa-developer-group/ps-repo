# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #         left, right = 0, len(nums) - 1
        #         ans = []

        #         while left <= right:
        #             mid = (left + right) // 2
        #             if nums[mid] == target:
        #                 ans.append(mid)
        #             else:
        #                 if nums[mid] < target:
        #                     left = mid + 1
        #                 else:
        #                     right = mid - 1
        #         return ans

        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        if len(ans) == 0:
            return [-1, -1]
        if(len(ans)) == 1:
            return [ans[0], ans[0]]
        if(len(ans)) > 2:
            return [ans[0], ans[len(ans) - 1]]
        return ans
