
# Task 4: String Performance Analysis

import time

sizes = [1000, 5000, 10000, 20000]

print("===== STRING PERFORMANCE ANALYSIS =====")
print("Comparing + operator and join() method\n")

for n in sizes:

    data = ["Python Programming "] * n

    # Using + operator
    start = time.perf_counter()

    result1 = ""
    for item in data:
        result1 += item

    plus_time = time.perf_counter() - start

    # Using join()
    start = time.perf_counter()

    result2 = "".join(data)

    join_time = time.perf_counter() - start

    print("Number of strings:", n)
    print("+ operator time:", round(plus_time, 6), "seconds")
    print("join() time:", round(join_time, 6), "seconds")
    print("-" * 40)

print("\nConclusion:")
print("join() is generally more efficient for combining")
print("a large number of strings.")

print("\n===== PROGRAM COMPLETED =====")
