# Task 4: Building Long Text (+ vs join())

## Objective
To compare the execution time of string concatenation using the `+` operator and the `join()` method.

## Concepts Used
- String concatenation
- String immutability
- `join()` method
- `time.perf_counter()`
- Performance analysis

## Procedure
1. Create a list containing repeated strings.
2. Measure the time taken using the `+` operator.
3. Measure the time taken using `join()`.
4. Repeat the experiment with different input sizes.
5. Compare the execution times.

## Experimental Input Sizes
- 1,000 strings
- 5,000 strings
- 10,000 strings
- 20,000 strings

## Observation
The program measures and displays the execution time of both methods for each input size. Actual execution times depend on the computer and Python implementation.

## Conclusion
The `join()` method is generally preferred when combining many strings because it avoids repeatedly constructing intermediate strings. Both methods produce the same combined text.