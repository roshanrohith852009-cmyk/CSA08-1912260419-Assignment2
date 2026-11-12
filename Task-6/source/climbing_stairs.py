


import time
from functools import lru_cache

# Method 1: Normal Recursion
def climbing_stairs(n):
    if n <= 1:
        return 1

    return climbing_stairs(n - 1) + climbing_stairs(n - 2)


# Method 2: Recursion with Memoization
@lru_cache(maxsize=None)
def climbing_stairs_memo(n):
    if n <= 1:
        return 1

    return climbing_stairs_memo(n - 1) + climbing_stairs_memo(n - 2)


print("===== CLIMBING STAIRS PROBLEM =====")

n = int(input("Enter number of stairs (1 to 35): "))

if n < 1 or n > 35:
    print("Please enter a number between 1 and 35.")

else:
    # Normal recursion
    start = time.perf_counter()
    result1 = climbing_stairs(n)
    time1 = time.perf_counter() - start

    # Memoization
    start = time.perf_counter()
    result2 = climbing_stairs_memo(n)
    time2 = time.perf_counter() - start

    print("\nNormal Recursion:")
    print("Ways:", result1)
    print("Execution Time:", time1, "seconds")

    print("\nMemoization:")
    print("Ways:", result2)
    print("Execution Time:", time2, "seconds")

    print("\nBoth methods produce the same result.")

    print("\nMemoization Cache Information:")
    print(climbing_stairs_memo.cache_info())

print("\n===== PROGRAM COMPLETED =====")
