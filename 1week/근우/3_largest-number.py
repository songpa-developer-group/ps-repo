from typing import List

# 1 <= nums.length <= 100
from functools import cmp_to_key, reduce


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def _cmp(x, y):
            return int(y + x) - int(x + y)

        nums = map(str, nums)
        ## versoin 1 and version 2 is same
        sorted_list = list(sorted(nums, key=cmp_to_key(_cmp)))  ## version 1
        sorted_list = list(
            sorted(nums, key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        )  ## version 2

        return str(int(reduce(lambda a, b: a + b, sorted_list)))


print(Solution().largestNumber([34323, 3432]))  # "343234323"
print(Solution().largestNumber([134, 13]))  ## 13413
print(Solution().largestNumber([3, 30, 34, 5, 9]))  # 9534330
print(Solution().largestNumber([432, 43243]))  # 43243 432
print(Solution().largestNumber([0, 0]))  # 43243 432
