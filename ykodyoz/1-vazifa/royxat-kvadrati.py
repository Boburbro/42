def sortedSquares(nums: list) -> list:
    for index, num in enumerate(nums): 
        nums[index] = num ** 2
    
    return sorted(nums)

print(sortedSquares([-4,-1,0,3,10]))