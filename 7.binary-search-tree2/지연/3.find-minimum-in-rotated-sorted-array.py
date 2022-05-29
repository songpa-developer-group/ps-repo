# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
