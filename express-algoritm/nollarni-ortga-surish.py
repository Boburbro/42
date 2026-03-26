def moveZeroes(nums: list) -> list:

  new_list = nums.copy()

  null_count = 0

  while 0 in new_list:
    new_list.remove(0)
    null_count += 1

  new_list.extend([0 for i in range(null_count)])

  return new_list

def moveZeroes2(nums: list) -> list:
    
    count = 0

    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            continue

        nums[i], nums[i - count] = nums[i - count], nums[i]
    
    return nums

def measure_memory(func):
    import tracemalloc
    
    tracemalloc.start()
    
    func()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak



import timeit
test = [0,1,0,3,12] * 100_000

print(len(test))

time1 = timeit.timeit(lambda: moveZeroes(test.copy()), number=1)
time2 = timeit.timeit(lambda: moveZeroes2(test.copy()), number=1)

print(f"func1: {time1 * 1000:.4f} ms")
print(f"func2: {time2 * 1000:.4f} ms")

print(f"func1: {time1 * 1_000_000:.2f} µs")
print(f"func2: {time2 * 1_000_000:.2f} µs")

m1 = measure_memory(lambda: moveZeroes(test.copy()))
m2 = measure_memory(lambda: moveZeroes2(test.copy()))

print(f"func1: {m1 / 1024:.2f} KB")
print(f"func2: {m2 / 1024:.2f} KB")

