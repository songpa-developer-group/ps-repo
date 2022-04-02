from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits = 0
        for n in nums:
            bit_n = 1 << n
            if bits & bit_n == bit_n:
                return n
            bits |= bit_n
