def largestNumber(nums):

    if sum(nums) == 0:
        return '0'

    _nums = list(map(str, nums))
    def swap(x, y):
        return True if x + y < y + x else False

    for i in range(0, len(_nums)-1):
        for j in range(i, len(_nums)):
            if swap(_nums[i], _nums[j]):
                _nums[i], _nums[j] = _nums[j], _nums[i]

    return ''.join(_nums)

if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(largestNumber(nums))