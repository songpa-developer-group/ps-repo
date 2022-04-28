## https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r_sum = sum(nums)
        l_sum = 0
        for i in range(0,len(nums)):
            if i>0:
                l_sum += nums[i-1]
            r_sum -= nums[i]
            if(l_sum == r_sum):
                return i
        return -1

[1,2,3]
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # 접두사 합(Prefix Sum) 배열 계산
        sum_value = 0
        prefix_sum = [0]

        for i in nums:
            sum_value += i
            prefix_sum.append(sum_value) # 1, 1+2, 1+2+3

        # 구간 합 계산
        for i in range(len(nums)):
            if(prefix_sum[-i-1] == prefix_sum[i]):
                return i
        return -1
