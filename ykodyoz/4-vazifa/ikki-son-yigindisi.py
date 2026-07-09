def twoSum(nums: list, target: int) -> list:
    
    result = {}

    for index, n in enumerate(nums):
        need = target - n
        if need in result:
            return [result[need], index]
        
        result[n] = index
        
    return []


print(twoSum([2,7,11,15], target=9))
