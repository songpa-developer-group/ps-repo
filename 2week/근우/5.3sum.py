from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def _find_lower_idx(l, r, target):
            while l < r:
                m = (l + r) >> 1
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        ans = []
        visit_l = set()
        nums.sort()
        for l in range(len(nums) - 2):
            if nums[l] in visit_l:
                continue
            visit_l.add(nums[l])
            visit_r = set()
            for r in range(l + 1, len(nums) - 1):
                if nums[r] in visit_r:
                    continue
                visit_r.add(nums[r])
                t = -(nums[l] + nums[r])
                idx = _find_lower_idx(r + 1, len(nums) - 1, t)
                if t == nums[idx]:
                    ans.append([nums[l], nums[r], t])
        return ans
