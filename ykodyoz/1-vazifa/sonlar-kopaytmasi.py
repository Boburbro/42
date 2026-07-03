def productExceptSelf(nums: list) -> list:
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [1]

    _result_left = []
    _lastNum = 1
    for num in nums:
        _lastNum *= num
        _result_left.append(_lastNum)

    _lastNum = 1
    _result_right = []
    index = len(nums) - 1
    while index >= 0:

        _lastNum *= nums[index]
        _result_right.append(_lastNum)
        index -= 1

    _result_right.reverse()

    print(_result_left)
    print(_result_right)

    for index, num in enumerate(nums):
        if index == 0:
            nums[index] = _result_right[1]
            continue
        
        if index == len(nums) - 1:
            nums[index] = _result_left[index - 1]
            continue
        
        nums[index] = _result_left[index-1] * _result_right[index+1]

    return nums








nums = productExceptSelf([0])
# nums = productExceptSelf([1, 2, 3, 4])
# print([24, 30, 40, 60, 120])
print(nums)