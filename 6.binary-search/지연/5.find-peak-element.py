# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = max(nums)
        return nums.index(max_num)


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1


print(Solution1().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(Solution2().findPeakElement([6, 5, 4, 3, 2, 3, 2]))
