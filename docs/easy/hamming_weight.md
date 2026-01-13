# Number of 1 Bits (Hamming Weight)

## Problem Summary

- Given a positive integer `n`, return the number of set bits (1s) in its binary representation.
- Also known as the Hamming Weight or population count.
- Example: n = 11 (binary 1011) → 3 set bits.

Approach (Brian Kernighan's algorithm)

- Use bitwise operation `n &= (n - 1)` to clear the rightmost set bit in each iteration.
- Count how many times this operation is performed until `n` becomes 0.
- Each iteration removes exactly one set bit.

Why this works (bitwise insight)

- The operation `n - 1` flips all bits after the rightmost set bit (including the rightmost set bit itself).
- Example: n = 12 (binary 1100)
  - n - 1 = 11 (binary 1011)
  - n & (n - 1) = 1100 & 1011 = 1000 (removes rightmost 1)
- By ANDing n with (n-1), we turn off the rightmost 1 bit.
- Repeat until all 1 bits are cleared (n becomes 0).

Time and space complexity

- Time: O(k) where k = number of set bits (Hamming weight). Best case: O(1) for powers of 2; worst case: O(log n) for numbers with all bits set.
- Space: O(1) — only a counter variable used.

Why Brian Kernighan's algorithm is optimal

- It only iterates once per set bit (not once per total bit).
- For sparse bit patterns (few 1s), it's much faster than checking every bit position.
- Example: n = 2^30 (only one set bit) → only 1 iteration, not 31.

Alternative approaches

**Approach 1: String conversion (commented out in code)**

```python
def hammingWeight(self, n: int) -> int:
    return bin(n).count("1")
```

- Time: O(log n) — converts to binary string and counts '1's.
- Space: O(log n) — binary string representation.
- Simple and readable but less efficient due to string allocation.

**Approach 2: Built-in bit count (Python 3.10+)**

```python
def hammingWeight(self, n: int) -> int:
    return n.bit_count()
```

- Most concise and efficient (native C implementation).
- Available only in Python 3.10+.

**Approach 3: Manual bit shifting**

```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

- Time: O(log n) — checks all bit positions.
- Space: O(1).
- More straightforward but slower than Brian Kernighan's for sparse bits.

**Approach 4: Lookup table (for very large datasets)**

- Precompute counts for all 8-bit or 16-bit values.
- Break n into chunks and sum their counts.
- Time: O(1) per query after O(2^k) preprocessing.
- Space: O(2^k) for the table.

Edge cases

- n = 0 → 0 set bits (loop never executes).
- n = 1 → 1 set bit (single iteration).
- Powers of 2 (e.g., 128 = 2^7) → 1 set bit (single iteration).
- All bits set (e.g., 2^32 - 1 = 4294967295) → 32 set bits (32 iterations).
- Large numbers (up to 2^32 - 1) → handled efficiently.

Example testcases (from repository)

- n = 11 (binary 1011) → 3
- n = 0 → 0
- n = 1 → 1
- n = 128 (binary 10000000) → 1
- n = 15 (binary 1111) → 4
- n = 170 (binary 10101010) → 4
- n = 12345 (binary 11000000111001) → 6
- n = 1073741824 (2^30) → 1
- n = 4294967295 (2^32 - 1, all bits set) → 32
- n = 4294967294 (2^32 - 2) → 31

Step-by-step example (n = 11)

- n = 11 (binary 1011), count = 0
- Iteration 1: n &= n-1 → 1011 & 1010 = 1010 (10), count = 1
- Iteration 2: n &= n-1 → 1010 & 1001 = 1000 (8), count = 2
- Iteration 3: n &= n-1 → 1000 & 0111 = 0000 (0), count = 3
- n = 0, return 3

Thought process / design choices

- Brian Kernighan's algorithm is the gold standard for this problem.
- It's more efficient than naive bit-by-bit checking because it only iterates on set bits.
- The approach demonstrates deep understanding of bitwise operations.
- For production code in Python 3.10+, use `.bit_count()` for best performance and readability.

Common pitfalls

- Using bit shifting through all 32 positions → wastes time when there are few set bits.
- Forgetting that `n & (n-1)` modifies n → must use compound assignment `n &= (n-1)` or reassign.
- Confusing this with counting total bits (log n) vs. set bits (k).

Performance comparison

- Brian Kernighan's: O(k) where k = number of set bits — optimal for sparse bits.
- Bit shifting: O(log n) — checks all bits regardless of how many are set.
- String conversion: O(log n) — additional overhead for string allocation.
- bit_count(): O(1) or O(log n) depending on CPU instruction support — fastest in practice.

Applications

- Network programming (calculating subnet masks, packet checksums)
- Error detection/correction codes
- DNA sequence analysis (counting mismatches)
- Cryptography and hashing algorithms
- Graphics programming (transparency masks)

Notes

- This problem is a classic introduction to bit manipulation.
- Brian Kernighan's algorithm is elegant and efficient — worth memorizing.
- The solution demonstrates the power of low-level bitwise operations.
- Also known as "popcount" (population count) in computer science literature.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def hammingWeight(self, n: int) -> int:
    return bin(n).count("1")
```

### How It Works

Problem summary

- Given a positive integer `n`, return the number of set bits (1s) in its binary representation.
- Also known as the Hamming Weight or population count.
- Example: n = 11 (binary 1011) → 3 set bits.

Approach (Brian Kernighan's algorithm)

- Use bitwise operation `n &= (n - 1)` to clear the rightmost set bit in each iteration.
- Count how many times this operation is performed until `n` becomes 0.
- Each iteration removes exactly one set bit.

Why this works (bitwise insight)

- The operation `n - 1` flips all bits after the rightmost set bit (including the rightmost set bit itself).
- Example: n = 12 (binary 1100)
  - n - 1 = 11 (binary 1011)
  - n & (n - 1) = 1100 & 1011 = 1000 (removes rightmost 1)
- By ANDing n with (n-1), we turn off the rightmost 1 bit.
- Repeat until all 1 bits are cleared (n becomes 0).

Time and space complexity

- Time: O(k) where k = number of set bits (Hamming weight). Best case: O(1) for powers of 2; worst case: O(log n) for numbers with all bits set.
- Space: O(1) — only a counter variable used.

Why Brian Kernighan's algorithm is optimal

- It only iterates once per set bit (not once per total bit).
- For sparse bit patterns (few 1s), it's much faster than checking every bit position.
- Example: n = 2^30 (only one set bit) → only 1 iteration, not 31.

Alternative approaches

**Approach 1: String conversion (commented out in code)**

```python
def hammingWeight(self, n: int) -> int:
    return bin(n).count("1")
```

- Time: O(log n) — converts to binary string and counts '1's.
- Space: O(log n) — binary string representation.
- Simple and readable but less efficient due to string allocation.

**Approach 2: Built-in bit count (Python 3.10+)**

```python
def hammingWeight(self, n: int) -> int:
    return n.bit_count()
```

- Most concise and efficient (native C implementation).
- Available only in Python 3.10+.

**Approach 3: Manual bit shifting**

```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

- Time: O(log n) — checks all bit positions.
- Space: O(1).
- More straightforward but slower than Brian Kernighan's for sparse bits.

**Approach 4: Lookup table (for very large datasets)**

- Precompute counts for all 8-bit or 16-bit values.
- Break n into chunks and sum their counts.
- Time: O(1) per query after O(2^k) preprocessing.
- Space: O(2^k) for the table.

Edge cases

- n = 0 → 0 set bits (loop never executes).
- n = 1 → 1 set bit (single iteration).
- Powers of 2 (e.g., 128 = 2^7) → 1 set bit (single iteration).
- All bits set (e.g., 2^32 - 1 = 4294967295) → 32 set bits (32 iterations).
- Large numbers (up to 2^32 - 1) → handled efficiently.

Example testcases (from repository)

- n = 11 (binary 1011) → 3
- n = 0 → 0
- n = 1 → 1
- n = 128 (binary 10000000) → 1
- n = 15 (binary 1111) → 4
- n = 170 (binary 10101010) → 4
- n = 12345 (binary 11000000111001) → 6
- n = 1073741824 (2^30) → 1
- n = 4294967295 (2^32 - 1, all bits set) → 32
- n = 4294967294 (2^32 - 2) → 31

Step-by-step example (n = 11)

- n = 11 (binary 1011), count = 0
- Iteration 1: n &= n-1 → 1011 & 1010 = 1010 (10), count = 1
- Iteration 2: n &= n-1 → 1010 & 1001 = 1000 (8), count = 2
- Iteration 3: n &= n-1 → 1000 & 0111 = 0000 (0), count = 3
- n = 0, return 3

Thought process / design choices

- Brian Kernighan's algorithm is the gold standard for this problem.
- It's more efficient than naive bit-by-bit checking because it only iterates on set bits.
- The approach demonstrates deep understanding of bitwise operations.
- For production code in Python 3.10+, use `.bit_count()` for best performance and readability.

Common pitfalls

- Using bit shifting through all 32 positions → wastes time when there are few set bits.
- Forgetting that `n & (n-1)` modifies n → must use compound assignment `n &= (n-1)` or reassign.
- Confusing this with counting total bits (log n) vs. set bits (k).

Performance comparison

- Brian Kernighan's: O(k) where k = number of set bits — optimal for sparse bits.
- Bit shifting: O(log n) — checks all bits regardless of how many are set.
- String conversion: O(log n) — additional overhead for string allocation.
- bit_count(): O(1) or O(log n) depending on CPU instruction support — fastest in practice.

Applications

- Network programming (calculating subnet masks, packet checksums)
- Error detection/correction codes
- DNA sequence analysis (counting mismatches)
- Cryptography and hashing algorithms
- Graphics programming (transparency masks)

Notes

- This problem is a classic introduction to bit manipulation.
- Brian Kernighan's algorithm is elegant and efficient — worth memorizing.
- The solution demonstrates the power of low-level bitwise operations.
- Also known as "popcount" (population count) in computer science literature.

### Why Iteration Works

- The operation `n - 1` flips all bits after the rightmost set bit (including the rightmost set bit itself).
- Example: n = 12 (binary 1100)
  - n - 1 = 11 (binary 1011)
  - n & (n - 1) = 1100 & 1011 = 1000 (removes rightmost 1)
- By ANDing n with (n-1), we turn off the rightmost 1 bit.
- Repeat until all 1 bits are cleared (n becomes 0).

Time and space complexity

- Time: O(k) where k = number of set bits (Hamming weight). Best case: O(1) for powers of 2; worst case: O(log n) for numbers with all bits set.
- Space: O(1) — only a counter variable used.

Why Brian Kernighan's algorithm is optimal

- It only iterates once per set bit (not once per total bit).
- For sparse bit patterns (few 1s), it's much faster than checking every bit position.
- Example: n = 2^30 (only one set bit) → only 1 iteration, not 31.

Alternative approaches

**Approach 1: String conversion (commented out in code)**

```python
def hammingWeight(self, n: int) -> int:
    return bin(n).count("1")
```

- Time: O(log n) — converts to binary string and counts '1's.
- Space: O(log n) — binary string representation.
- Simple and readable but less efficient due to string allocation.

**Approach 2: Built-in bit count (Python 3.10+)**

```python
def hammingWeight(self, n: int) -> int:
    return n.bit_count()
```

- Most concise and efficient (native C implementation).
- Available only in Python 3.10+.

**Approach 3: Manual bit shifting**

```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

- Time: O(log n) — checks all bit positions.
- Space: O(1).
- More straightforward but slower than Brian Kernighan's for sparse bits.

**Approach 4: Lookup table (for very large datasets)**

- Precompute counts for all 8-bit or 16-bit values.
- Break n into chunks and sum their counts.
- Time: O(1) per query after O(2^k) preprocessing.
- Space: O(2^k) for the table.

Edge cases

- n = 0 → 0 set bits (loop never executes).
- n = 1 → 1 set bit (single iteration).
- Powers of 2 (e.g., 128 = 2^7) → 1 set bit (single iteration).
- All bits set (e.g., 2^32 - 1 = 4294967295) → 32 set bits (32 iterations).
- Large numbers (up to 2^32 - 1) → handled efficiently.

Example testcases (from repository)

- n = 11 (binary 1011) → 3
- n = 0 → 0
- n = 1 → 1
- n = 128 (binary 10000000) → 1
- n = 15 (binary 1111) → 4
- n = 170 (binary 10101010) → 4
- n = 12345 (binary 11000000111001) → 6
- n = 1073741824 (2^30) → 1
- n = 4294967295 (2^32 - 1, all bits set) → 32
- n = 4294967294 (2^32 - 2) → 31

Step-by-step example (n = 11)

- n = 11 (binary 1011), count = 0
- Iteration 1: n &= n-1 → 1011 & 1010 = 1010 (10), count = 1
- Iteration 2: n &= n-1 → 1010 & 1001 = 1000 (8), count = 2
- Iteration 3: n &= n-1 → 1000 & 0111 = 0000 (0), count = 3
- n = 0, return 3

Thought process / design choices

- Brian Kernighan's algorithm is the gold standard for this problem.
- It's more efficient than naive bit-by-bit checking because it only iterates on set bits.
- The approach demonstrates deep understanding of bitwise operations.
- For production code in Python 3.10+, use `.bit_count()` for best performance and readability.

Common pitfalls

- Using bit shifting through all 32 positions → wastes time when there are few set bits.
- Forgetting that `n & (n-1)` modifies n → must use compound assignment `n &= (n-1)` or reassign.
- Confusing this with counting total bits (log n) vs. set bits (k).

Performance comparison

- Brian Kernighan's: O(k) where k = number of set bits — optimal for sparse bits.
- Bit shifting: O(log n) — checks all bits regardless of how many are set.
- String conversion: O(log n) — additional overhead for string allocation.
- bit_count(): O(1) or O(log n) depending on CPU instruction support — fastest in practice.

Applications

- Network programming (calculating subnet masks, packet checksums)
- Error detection/correction codes
- DNA sequence analysis (counting mismatches)
- Cryptography and hashing algorithms
- Graphics programming (transparency masks)

Notes

- This problem is a classic introduction to bit manipulation.
- Brian Kernighan's algorithm is elegant and efficient — worth memorizing.
- The solution demonstrates the power of low-level bitwise operations.
- Also known as "popcount" (population count) in computer science literature.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(k) where k = number of set bits (Hamming weight). Best case: O(1) for powers of 2; worst case: O(log n) for numbers with all bits set. - Space: O(1) — only a counter variable used. Why Brian Kernighan's algorithm is optimal - It only iterates once per set bit (not once per total bit). - For sparse bit patterns (few 1s), it's much faster than checking every bit position. - Example: n = 2^30 (only one set bit) → only 1 iteration, not 31. Alternative approaches **Approach 1: String conversion (commented out in code)** ```python def hammingWeight(self, n: int) -> int:     return bin(n).count("1") ``` - Time: O(log n) — converts to binary string and counts '1's. - Space: O(log n) — binary string representation. - Simple and readable but less efficient due to string allocation. **Approach 2: Built-in bit count (Python 3.10+)** ```python def hammingWeight(self, n: int) -> int:     return n.bit_count() ``` - Most concise and efficient (native C implementation). - Available only in Python 3.10+. **Approach 3: Manual bit shifting** ```python def hammingWeight(self, n: int) -> int:     count = 0     while n:         count += n & 1         n >>= 1     return count ``` - Time: O(log n) — checks all bit positions. - Space: O(1). - More straightforward but slower than Brian Kernighan's for sparse bits. **Approach 4: Lookup table (for very large datasets)** - Precompute counts for all 8-bit or 16-bit values. - Break n into chunks and sum their counts. - Time: O(1) per query after O(2^k) preprocessing. - Space: O(2^k) for the table. Edge cases - n = 0 → 0 set bits (loop never executes). - n = 1 → 1 set bit (single iteration). - Powers of 2 (e.g., 128 = 2^7) → 1 set bit (single iteration). - All bits set (e.g., 2^32 - 1 = 4294967295) → 32 set bits (32 iterations). - Large numbers (up to 2^32 - 1) → handled efficiently. Example testcases (from repository) - n = 11 (binary 1011) → 3 - n = 0 → 0 - n = 1 → 1 - n = 128 (binary 10000000) → 1 - n = 15 (binary 1111) → 4 - n = 170 (binary 10101010) → 4 - n = 12345 (binary 11000000111001) → 6 - n = 1073741824 (2^30) → 1 - n = 4294967295 (2^32 - 1, all bits set) → 32 - n = 4294967294 (2^32 - 2) → 31 Step-by-step example (n = 11) - n = 11 (binary 1011), count = 0 - Iteration 1: n &= n-1 → 1011 & 1010 = 1010 (10), count = 1 - Iteration 2: n &= n-1 → 1010 & 1001 = 1000 (8), count = 2 - Iteration 3: n &= n-1 → 1000 & 0111 = 0000 (0), count = 3 - n = 0, return 3 Thought process / design choices - Brian Kernighan's algorithm is the gold standard for this problem. - It's more efficient than naive bit-by-bit checking because it only iterates on set bits. - The approach demonstrates deep understanding of bitwise operations. - For production code in Python 3.10+, use `.bit_count()` for best performance and readability. Common pitfalls - Using bit shifting through all 32 positions → wastes time when there are few set bits. - Forgetting that `n & (n-1)` modifies n → must use compound assignment `n &= (n-1)` or reassign. - Confusing this with counting total bits (log n) vs. set bits (k). Performance comparison - Brian Kernighan's: O(k) where k = number of set bits — optimal for sparse bits. - Bit shifting: O(log n) — checks all bits regardless of how many are set. - String conversion: O(log n) — additional overhead for string allocation. - bit_count(): O(1) or O(log n) depending on CPU instruction support — fastest in practice. Applications - Network programming (calculating subnet masks, packet checksums) - Error detection/correction codes - DNA sequence analysis (counting mismatches) - Cryptography and hashing algorithms - Graphics programming (transparency masks) Notes - This problem is a classic introduction to bit manipulation. - Brian Kernighan's algorithm is elegant and efficient — worth memorizing. - The solution demonstrates the power of low-level bitwise operations. - Also known as "popcount" (population count) in computer science literature.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
