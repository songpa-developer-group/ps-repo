## https://leetcode.com/problems/binary-search/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = ((r-l) // 2) + l
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m+1

        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))