from typing import List

'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result = []
        size = len(nums)
        for i in range(size - 2):
            l, r = i+1, size - 1
            while l < r:
                if nums[l] + nums[r] == nums[i] * (-1):
                    tmp = [nums[l], nums[r], nums[i]]
                    if tmp not in result:
                        result.append(tmp)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < nums[i] * (-1):
                    l += 1
                elif nums[l] + nums[r] > nums[i] * (-1):
                    r -= 1
        return result
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum > 0:
                    r -= 1
                elif _sum < 0:
                    l += 1
                else:
                    answer.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    r -= 1
                    l += 1

        return answer

if __name__ == "__main__":
    nums = [0]
    print(Solution().threeSum(nums))