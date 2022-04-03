def findDuplicate(nums):

    answer = -1
    count = [0 for _ in range(1, max(nums)+1)]
    for num in nums:
        count[num-1] += 1
        if count[num-1] > 1:
            answer = num
            break
    return answer


if __name__ == "__main__":
    nums = [2,2,2,2,2]
    print(findDuplicate(nums))
