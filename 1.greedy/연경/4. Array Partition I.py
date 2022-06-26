## 4. [array-partition-i](https://leetcode.com/problems/array-partition-i/)
def arrayPairSum(nums):

    answer = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        num = nums[i]
        answer += num
    return answer

if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    print(arrayPairSum(nums))