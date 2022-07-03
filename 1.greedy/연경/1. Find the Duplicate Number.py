## 1. [find-the-duplicate-number](https://leetcode.com/problems/find-the-duplicate-number/)
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer = -1

        count = [0 for _ in range(max(nums) + 1)]
        for num in nums:
            count[num] += 1
        # print(count)
        for i, c in enumerate(count):
            if c > 1:
                return i
        return answer


if __name__ == "__main__":
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))
