def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def rotate2(nums: list, k: int) -> list:
    if k == 0: return nums
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

    return nums


def rotate1(nums: list, k: int) -> list:
	for num in range(k):
		nums.insert(0, nums.pop())

	return nums

print(rotate1([1,2,3,4,5,6,7], 3))
print(rotate2([1,2,3,4,5,6,7], 3))

def measure_memory(func):
    import tracemalloc
    
    tracemalloc.start()
    
    func()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak



m1 = measure_memory(lambda: rotate1([1,2,3,4,5,6,7], 3))
m2 = measure_memory(lambda: rotate2([1,2,3,4,5,6,7], 3))

print(f"func1: {m1 / 1024:.2f} KB")
print(f"func2: {m2 / 1024:.2f} KB")

import timeit

time1 = timeit.timeit(lambda:  rotate1([1,2,3,4,5,6,7], 3), number=1)
time2 = timeit.timeit(lambda:  rotate2([1,2,3,4,5,6,7], 3), number=1)

print(f"func1: {time1 * 1000:.4f} ms")
print(f"func2: {time2 * 1000:.4f} ms")