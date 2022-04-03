class Solution:
    def findDuplicate(self, nums):
        # case 1 -> Status: Time Limit Exceeded O(N^N)
        # for i in nums:
        #     if(nums.count(i) > 1):
        #         return i

        # case 2 -> Status: Time Limit Exceeded O(N^2)
        # is_duplicated = []
        # for i in nums: #list 탐색은 기본적으로 O(N)
        #     if (i in is_duplicated): #한번 더 탐색하면 O(N^2)
        #         return i
        #     else:
        #         is_duplicated.append(i)

        # case 3 -> Status: Accepted but must solve the problem without modifying the array O(NLogN)
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]

        # case 4 -> log2N
        no_duplicated_nums = set()
        for i in nums:
            if (i in no_duplicated_nums):
                return i
            else:
                no_duplicated_nums.add(i)


print(Solution().findDuplicate([3, 1, 3, 4, 2]))
