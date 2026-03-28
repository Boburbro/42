import timeit
import tracemalloc


def test_speed(func, number=1):
    """
    Ishlatish:
    from speed_tester import test_speed
    test_speed(lambda: my_func(...), number=100)
    """
    seconds = timeit.timeit(func, number=number)

    tracemalloc.start()
    func()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    result = {
        "seconds": seconds,
        "ms": seconds * 1000,
        "us": seconds * 1_000_000,
        "peak_kb": peak / 1024,
    }

    print("-" * 30)
    print(f"time: {result['ms']:.4f} ms")
    print(f"memory: {result['peak_kb']:.2f} KB")

    return result
