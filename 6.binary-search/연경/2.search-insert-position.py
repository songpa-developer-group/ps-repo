## https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))

