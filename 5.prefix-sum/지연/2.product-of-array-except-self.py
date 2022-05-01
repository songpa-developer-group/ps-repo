# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero = False
        multiply = 1
        product = []

        for i in range(len(nums)):
            if(nums[i] == 0 and zero == False):
                zero = True
                continue
            multiply = multiply*nums[i]

        for i in range(len(nums)):
            if zero:
                if(nums[i] == 0):
                    product.append(int(multiply))
                else:
                    product.append(0)
            else:
                product.append(int(multiply/nums[i]))

        return product


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]

        left = 1
        right = 1

        for idx in range(len(nums)):
            ans[idx] *= left
            ans[-1-idx] *= right
            left *= nums[idx]
            right *= nums[-1-idx]

        return ans
