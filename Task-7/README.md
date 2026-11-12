# Task 7: Day-4 Design Challenge

## Selected Program
Task-4: Building Long Text (+ vs join()).

## 1. Problem Identification
The original program uses repeated string concatenation with the + operator. Repeatedly creating new strings can reduce performance when processing large amounts of text.

## 2. Original Design
The original design uses a loop and the += operator to combine strings.

## 3. Redesigned Solution
The redesigned program uses the join() method to combine multiple strings efficiently.

## 4. Experimental Method
The original and redesigned methods are tested using 1,000, 5,000, 10,000, 20,000 and 50,000 strings.

Execution time is measured using time.perf_counter().

## 5. Correctness Verification
Both methods are compared to confirm that they produce identical output.

## 6. Performance Analysis
The execution times are printed for each input size. The results help compare the performance of the original and redesigned implementations.

## 7. Conclusion
The redesigned solution uses join() to combine multiple strings. It is generally a more efficient approach for building large strings and produces the same output as the original method.