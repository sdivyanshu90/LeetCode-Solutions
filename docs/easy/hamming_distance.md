# Hamming Distance — Explanation, Approach, Complexity

Problem summary

- Given two integers `x` and `y`, return the Hamming distance between them.
- The Hamming distance is the number of positions at which the corresponding bits are different.
- Example: x = 1 (binary 0001), y = 4 (binary 0100) → Hamming distance = 2 (bits differ at positions 0 and 2).

Approach (XOR + bit counting)

- Compute the XOR of x and y: `x ^ y`.
  - XOR produces 1 in positions where bits differ, and 0 where they are the same.
- Convert the XOR result to a binary string using `bin()`.
- Count the number of '1' characters in the binary string using `.count("1")`.
- Return the count.

Why this works (bitwise insight)

- XOR (exclusive OR) operation: `a ^ b` returns 1 if bits differ, 0 if they match.
- Example: 1 (0001) ^ 4 (0100) = 5 (0101). Binary 0101 has two 1s → Hamming distance = 2.
- Counting '1's in the XOR result directly gives the number of differing bit positions.

Time and space complexity

- Time: O(log max(x, y)) — XOR is O(1), converting to binary string is O(k) where k = number of bits ≈ log(max(x, y)), counting '1's is O(k).
- Space: O(log max(x, y)) for the binary string representation. Auxiliary space for computation is O(1).

Alternative approaches

**Approach 1: Brian Kernighan's algorithm (bit manipulation)**

```python
def hammingDistance(self, x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        count += 1
        xor &= xor - 1  # removes the rightmost set bit
    return count
```

- Time: O(k) where k = number of set bits (Hamming distance). More efficient for small distances.
- Space: O(1) — no string conversion.

**Approach 2: Built-in bit count (Python 3.10+)**

```python
def hammingDistance(self, x: int, y: int) -> int:
    return (x ^ y).bit_count()
```

- Most concise and efficient (native implementation in C).
- Available in Python 3.10+.

**Approach 3: Manual bit shifting**

```python
def hammingDistance(self, x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count
```

- Time: O(log max(x, y)) — checks all bits.
- Space: O(1).

Edge cases

- Both numbers equal (x == y) → Hamming distance = 0 (XOR = 0, no differing bits).
- One number is 0 → Hamming distance = number of set bits in the other number.
- Large numbers (up to 2³¹ - 1) → algorithm handles efficiently.
- Negative numbers: problem typically assumes non-negative integers; XOR works for negative integers but interpretation depends on representation.

Example testcases (from repository)

- x = 1, y = 4 → 2 (binary: 0001 vs 0100, differ at positions 0 and 2)
- x = 3, y = 1 → 1 (binary: 011 vs 001, differ at position 1)
- x = 0, y = 0 → 0 (identical)
- x = 15, y = 0 → 4 (binary: 1111 vs 0000, all 4 bits differ)
- x = 7, y = 14 → 2 (binary: 0111 vs 1110, differ at positions 0 and 3)

Mathematical properties

- Hamming distance is a metric: satisfies non-negativity, symmetry (d(x,y) = d(y,x)), and triangle inequality.
- Used in error detection/correction codes, DNA sequence analysis, and information theory.

Thought process / design choices

- The current implementation using `bin(x ^ y).count("1")` is concise and readable.
- For Python 3.10+, `.bit_count()` is the most idiomatic and efficient.
- For older Python versions or performance-critical code, Brian Kernighan's algorithm is optimal.
- String conversion adds minor overhead but is acceptable for typical problem constraints.

Common pitfalls

- Forgetting to XOR first → counting bits in x or y separately doesn't give the distance.
- Using `bin()` but not removing the '0b' prefix correctly → `.count("1")` works because it only counts '1' characters.
- Confusing Hamming distance with edit distance → Hamming distance requires equal-length sequences and only counts substitutions.

Performance comparison

- Current approach (string): ~O(k) where k = bit length, simple and readable.
- Brian Kernighan: O(hamming_distance), optimal for sparse differences.
- bit_count() (Python 3.10+): fastest, native C implementation.

Recommendation

- **Use `.bit_count()` if Python 3.10+** for best performance and readability.
- **Use current approach** for older Python versions and simplicity.
- **Use Brian Kernighan's** for understanding bit manipulation techniques or performance tuning.

Notes

- This problem is a classic introduction to bitwise operations.
- XOR is fundamental to many bit manipulation problems and error detection algorithms.
- The solution is optimal and demonstrates the power of bitwise operations.
