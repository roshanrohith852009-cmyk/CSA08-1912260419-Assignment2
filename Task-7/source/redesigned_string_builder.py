
import time

def build_using_plus(data):
    result = ""

    for item in data:
        result += item

    return result


def build_using_join(data):
    return "".join(data)


print("===== STRING BUILDER REDESIGN =====")

sizes = [1000, 5000, 10000, 20000, 50000]

print("\nPerformance Comparison\n")

for n in sizes:

    data = ["Python Programming "] * n

    # Original design
    start = time.perf_counter()
    original_result = build_using_plus(data)
    original_time = time.perf_counter() - start

    # Redesigned solution
    start = time.perf_counter()
    redesigned_result = build_using_join(data)
    redesigned_time = time.perf_counter() - start

    print("Number of strings:", n)
    print("Original (+) time:", round(original_time, 6), "seconds")
    print("Redesigned (join) time:", round(redesigned_time, 6), "seconds")

    if original_result == redesigned_result:
        print("Output verification: SUCCESS")
    else:
        print("Output verification: FAILED")

    if redesigned_time < original_time:
        print("Result: Redesigned solution is faster.")
    else:
        print("Result: Original solution was faster in this run.")

    print("-" * 45)


print("\n===== DESIGN ANALYSIS =====")
print("Problem: Repeated string concatenation.")
print("Redesign: Using the join() method.")
print("Benefit: Efficiently combines multiple strings.")
print("Correctness: Both methods produce identical output.")

print("\n===== PROGRAM COMPLETED =====")
