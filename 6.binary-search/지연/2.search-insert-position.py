# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left == right and nums[left] < target:
            return left + 1
        else:
            return left


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


print(Solution1().searchInsert([1, 3, 5, 6, 8, 10], 12))
