from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        change_point = -1
        for c in range(len(nums) - 1, 0, -1):
            if nums[c] > nums[c - 1]:
                change_point = c - 1
                break
        if change_point != -1:
            for c in range(len(nums) - 1, 0, -1):
                if nums[change_point] < nums[c]:
                    nums[change_point], nums[c] = nums[c], nums[change_point]
                    break
            s, e = change_point + 1, len(nums) - 1
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
            return
        nums.reverse()
