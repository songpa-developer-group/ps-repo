from typing import List
import copy
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _nums = copy.deepcopy(nums)


        return nums

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().nextPermutation(nums))