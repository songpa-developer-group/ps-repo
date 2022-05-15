## https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        _left = right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                _left = min(_left, mid)
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        left, right = 0, len(nums) - 1
        _right = left
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                _right = max(_right, mid)
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if _left == len(nums) - 1 and nums[_left] != target:
            _left = -1
        if _right == 0 and nums[_right] != target:
            _right = -1
        return [_left, _right]


if __name__ == "__main__":
    nums = []
    target = 0
    print(Solution().searchRange(nums, target))
