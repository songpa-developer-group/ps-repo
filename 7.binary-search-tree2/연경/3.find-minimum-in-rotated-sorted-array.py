## https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        answer = 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[left]:
                right -= 1
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    answer = nums[mid + 1]
                elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                    answer = nums[mid]
            else:
                left += 1
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    answer = nums[mid + 1]
                elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                    answer = nums[mid]
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(Solution().findMin(nums))
