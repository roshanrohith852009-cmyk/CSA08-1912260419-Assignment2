# Task 6: Recursion and Its Limits

## Objective
To solve the climbing stairs problem using normal recursion and memoization.

## Concepts Used
- Recursion
- Memoization
- lru_cache
- Time complexity
- Recursion limits

## Algorithm
1. Accept the number of stairs.
2. Calculate the number of ways using normal recursion.
3. Calculate the number of ways using memoization.
4. Measure both execution times.
5. Compare the results.

## Experimental Results

Input: 30 stairs

| Method | Execution Time |
|---|---:|
| Normal Recursion | 0.2304429 seconds |
| Memoization | 0.0001264 seconds |

Number of ways: 1346269

## Conclusion
Memoization significantly reduces repeated calculations and improves execution speed. Normal recursive solutions can become very slow for larger inputs. Memoization improves efficiency, although recursion depth is still limited by Python's recursion limit.