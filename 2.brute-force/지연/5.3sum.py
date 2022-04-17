from typing import List

# 이진 탐색


class Solution:
    def threeSum(self, nums: List[List[int]]) -> List[int]:
        result = []

        nums.sort()
        for i in range(len(nums)):
            start_idx = i + 1
            end_idx = len(nums) - 1

            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            while start_idx < end_idx:
                cur_nums = nums[i] + nums[start_idx] + nums[end_idx]
                if cur_nums == 0:
                    if([nums[i], nums[start_idx], nums[end_idx]] not in result):
                        result.append(
                            [nums[i], nums[start_idx], nums[end_idx]]
                        )
                    start_idx += 1
                    end_idx -= 1
                elif cur_nums < 0:
                    start_idx += 1
                elif cur_nums > 0:
                    end_idx -= 1
        return result


print(Solution().threeSum([-2, 0, 0, 2, 2]))
print(Solution().threeSum([-4, -1, -1, 0, 1, 2]))
