def productExceptSelf(nums: list) -> list:
    _result_left = []
    _lastNum = 1
    for num in nums:
        _lastNum *= num
        _result_left.append(_lastNum)

    _result_right = []
    _lastNum = 1
    nums.reverse()
    for num in nums:
        _lastNum *= num
        _result_right.append(_lastNum)

    _result_right.reverse()

    nums.reverse()

    print("_result_left:  ", _result_left)
    print("_result_right: ", _result_right)

    for index, num in enumerate(nums):
        if index == 0:
            nums[index] = _result_right[0]
            continue
        
        if index == len(nums) - 1:
            nums[index] = _result_left[index - 1]
            continue
        
        nums[index] = _result_left[index-1] * _result_right[index+1]

    return nums








print("                [5, 4, 3, 2, 1]")
nums = productExceptSelf([5, 4, 3, 2, 1])
print("*"*10)
print("Right answer:  ", [24, 30, 40, 60, 120])

print("Calculated:    ", nums)