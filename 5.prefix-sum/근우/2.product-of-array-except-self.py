## https://leetcode.com/problems/product-of-array-except-self/

from collections import Counter
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_num = Counter(nums)[0]
        prd_not_include_zero = prod(filter(lambda a: a!=0,nums)) if zero_num == 1 else 0
        prd = prod(nums)
        return [int(prd/num) if num != 0 else prd_not_include_zero for num in nums]
