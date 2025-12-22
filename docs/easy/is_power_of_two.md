# Power of Two

## Problem Summary

Given an integer `n`, return `true` if it is a power of two (i.e., if there exists an integer `x` such that `n == 2^x`). Otherwise, return `false`.

**LeetCode Problem**: [231. Power of Two](https://leetcode.com/problems/power-of-two/)

## Approach 1: Bit Manipulation (Implemented)

### Strategy

The implemented solution uses an **elegant bit manipulation trick**:

1. Check if `n` is positive (powers of 2 are always > 0)
2. Use the property: `n & (n - 1) == 0` for powers of 2

**Code**:

```python
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    return (n & (n - 1)) == 0
```

### How It Works

Powers of 2 have **exactly one bit set** in their binary representation:

- 1 = 2⁰ = `0b1`
- 2 = 2¹ = `0b10`
- 4 = 2² = `0b100`
- 8 = 2³ = `0b1000`
- 16 = 2⁴ = `0b10000`

The trick: When you subtract 1 from a power of 2, all bits after the single set bit become 1:

- 8 = `0b1000`, 7 = `0b0111`
- 16 = `0b10000`, 15 = `0b01111`
- 32 = `0b100000`, 31 = `0b011111`

The AND operation `n & (n-1)` will be 0 **only** if n is a power of 2:

```
    1000  (8)          10000  (16)
  & 0111  (7)        & 01111  (15)
  ------             -------
    0000  ✓            00000  ✓

    1001  (9)          01010  (10)
  & 1000  (8)        & 01001  (9)
  ------             -------
    1000  ✗            01000  ✗
```

### Why This Works

For a power of 2 (single bit set):

- `n` has one bit as 1, rest as 0
- `n - 1` flips that bit to 0 and all lower bits to 1
- `n & (n - 1)` has no overlapping 1 bits → result is 0

For non-powers of 2 (multiple bits set):

- `n` has multiple bits as 1
- `n - 1` flips the rightmost 1 to 0 and sets lower bits to 1
- `n & (n - 1)` still has some 1 bits from the higher positions → result is non-zero

### Complexity Analysis

- **Time Complexity**: O(1) - Single bitwise operation
- **Space Complexity**: O(1) - No extra space

### Edge Cases Handled

- **Zero**: `n <= 0` check returns `False`
- **Negative numbers**: `n <= 0` check returns `False`
- **One**: 1 = 2⁰, and `1 & 0 = 0`, returns `True` ✓
- **Large powers**: Works for all 32-bit or 64-bit powers of 2

## Approach 2: Iterative Division

A traditional loop-based approach:

```python
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    return n == 1
```

### How It Works

- Keep dividing by 2 while the number is even
- If we end up with 1, it was a power of 2
- If we get stuck with an odd number > 1, it wasn't

### Examples

- `n = 16`: 16 → 8 → 4 → 2 → 1 ✓
- `n = 18`: 18 → 9 (odd, stop), 9 ≠ 1 ✗

### Complexity

- **Time**: O(log n) - Divide by 2 each iteration
- **Space**: O(1)

### When to Use

- When bit manipulation is not allowed or unclear
- For educational clarity
- When you need to understand the process step-by-step

## Approach 3: Count Set Bits

Count the number of 1 bits - should be exactly 1 for powers of 2:

```python
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    return bin(n).count('1') == 1
```

Or using Brian Kernighan's algorithm:

```python
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    count = 0
    while n:
        count += 1
        n &= (n - 1)  # Clear the rightmost set bit

    return count == 1
```

### Complexity

- **Time**: O(k) where k is the number of set bits, worst case O(log n)
- **Space**: O(1)

### Note

This is essentially doing more work than approach 1. The check `n & (n-1) == 0` already verifies there's exactly one bit set.

## Approach 4: Logarithmic

Use logarithms to check if log₂(n) is an integer:

```python
import math

def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    log_val = math.log2(n)
    return log_val == int(log_val)
```

### Complexity

- **Time**: O(1) - Single logarithm calculation
- **Space**: O(1)

### Caveats

- **Floating-point precision issues** for large numbers
- Should use epsilon comparison: `abs(log_val - round(log_val)) < 1e-10`
- Not recommended for production

## Approach 5: Maximum Power Division

Similar to the power of three solution, but less elegant for powers of 2:

```python
def isPowerOfTwo(self, n: int) -> bool:
    # Max power of 2 in 32-bit signed: 2^30 = 1073741824
    return n > 0 and 1073741824 % n == 0
```

### Why This is Less Ideal

- **Only works for specific bit sizes** (32-bit in this case)
- **2 is not as special as 3**:
  - For power of 3, it works because 3 is prime
  - For power of 2, many non-powers also divide the max power
  - Actually, this approach **still works** for powers of 2 because any divisor of 2^k must be 2^j where j ≤ k
- **Bit manipulation is clearer** for powers of 2

### Complexity

- **Time**: O(1) - Single modulo operation
- **Space**: O(1)

## Comparison of Approaches

| Approach           | Time     | Space | Pros                             | Cons                            |
| ------------------ | -------- | ----- | -------------------------------- | ------------------------------- |
| Bit Manipulation   | O(1)     | O(1)  | Fastest, most elegant, idiomatic | Requires bit knowledge          |
| Iterative Division | O(log n) | O(1)  | Clear, intuitive                 | Slower                          |
| Count Set Bits     | O(log n) | O(1)  | Straightforward logic            | Unnecessary overhead            |
| Logarithmic        | O(1)     | O(1)  | Mathematical                     | Floating-point precision issues |
| Max Power Division | O(1)     | O(1)  | O(1) time                        | Less clear, bit-size dependent  |

## Why Bit Manipulation is Standard for Powers of 2

The `n & (n-1) == 0` pattern is **the** canonical way to check for powers of 2 because:

1. **Performance**: Single bitwise operation (hardware-level, extremely fast)
2. **Clarity**: Once learned, immediately recognizable pattern
3. **Elegance**: One line captures the mathematical property perfectly
4. **Universality**: Works for any integer size without modification
5. **Interview Standard**: Expected solution in technical interviews

## Edge Cases & Considerations

1. **Zero**: Not a power of 2 (2^x is always ≥ 1 for x ≥ 0)

   - Correctly returns `False` via `n <= 0` check

2. **One**: Special case - 2⁰ = 1

   - Binary: `0b1`, has one bit set
   - `1 & 0 = 0` ✓ returns `True`

3. **Negative Numbers**: Cannot be powers of 2 (2^x is always positive)

   - Handled by `n <= 0` check

4. **Maximum Powers**:

   - 32-bit signed: 2³⁰ = 1,073,741,824
   - 32-bit unsigned: 2³¹ = 2,147,483,648
   - 64-bit signed: 2⁶² = 4,611,686,018,427,387,904

5. **Numbers Close to Powers**:
   - 2ⁿ - 1: e.g., 15 (0b1111) - many bits set ✗
   - 2ⁿ + 1: e.g., 17 (0b10001) - multiple bits set ✗

## Common Pitfalls

1. **Forgetting the Positive Check**:

   ```python
   # WRONG: returns True for 0 and negative numbers with specific bit patterns
   return (n & (n - 1)) == 0

   # CORRECT: must verify n > 0
   return n > 0 and (n & (n - 1)) == 0
   ```

2. **Off-by-One with n = 1**:

   - 1 = 2⁰, it IS a power of 2
   - Don't exclude it

3. **Using `n <= 0` vs `n < 1`**:

   - Both work for integers
   - `n <= 0` is clearer for this problem

4. **Confusing with Bit Count**:

   - Don't count bits when you can just check `n & (n-1) == 0`
   - Counting is slower and unnecessary

5. **Float Precision in Log Approach**:
   - Never use exact equality with logarithms
   - Always use epsilon comparison

## Bit Manipulation Deep Dive

### Understanding `n & (n - 1)`

This operation has a special property: **it clears the rightmost set bit**.

Examples:

```
12 = 0b1100
11 = 0b1011
12 & 11 = 0b1000  (cleared rightmost 1)

10 = 0b1010
9  = 0b1001
10 & 9 = 0b1000  (cleared rightmost 1)

8 = 0b1000
7 = 0b0111
8 & 7 = 0b0000  (cleared the ONLY 1)
```

### Why It Works for a Single Bit

When n has only one bit set (power of 2):

- Subtracting 1 flips that bit and all bits to its right
- AND-ing gives 0 because there's no overlap

When n has multiple bits set:

- Subtracting 1 only affects bits up to the rightmost 1
- AND-ing preserves the higher 1 bits
- Result is non-zero

### Related Bit Tricks

- **Clear rightmost bit**: `n & (n - 1)`
- **Isolate rightmost bit**: `n & (-n)`
- **Check if power of 2**: `n > 0 && (n & (n - 1)) == 0`
- **Count set bits**: Repeatedly do `n & (n - 1)` until n becomes 0

## Optimization Notes

The implemented bit manipulation solution is **optimal**:

- O(1) time - cannot do better
- O(1) space - no extra memory
- Single bitwise operation - hardware-level efficiency
- Clean and readable once the pattern is understood

This is the gold standard solution for checking powers of 2.

## Test Cases

```python
# Powers of two
isPowerOfTwo(1)            # True (2⁰)
isPowerOfTwo(2)            # True (2¹)
isPowerOfTwo(4)            # True (2²)
isPowerOfTwo(16)           # True (2⁴)
isPowerOfTwo(1024)         # True (2¹⁰)
isPowerOfTwo(1073741824)   # True (2³⁰, max 32-bit signed)

# Non-powers of two
isPowerOfTwo(3)            # False
isPowerOfTwo(5)            # False
isPowerOfTwo(6)            # False
isPowerOfTwo(18)           # False
isPowerOfTwo(1023)         # False (2¹⁰ - 1)
isPowerOfTwo(2147483647)   # False (2³¹ - 1, max 32-bit int)

# Edge cases
isPowerOfTwo(0)            # False
isPowerOfTwo(-16)          # False
isPowerOfTwo(-2)           # False

# Close to powers
isPowerOfTwo(15)           # False (2⁴ - 1 = 0b1111)
isPowerOfTwo(17)           # False (2⁴ + 1 = 0b10001)
isPowerOfTwo(1073741825)   # False (2³⁰ + 1)
```

## Thought Process

The problem asks us to identify powers of 2, which have a distinctive property in binary: exactly one bit is set. The bit manipulation approach `n & (n-1) == 0` elegantly captures this property.

Key insights:

1. Powers of 2 have exactly one bit set in binary representation
2. Subtracting 1 from a power of 2 flips all bits from the set bit rightward
3. AND-ing these two numbers results in 0 (no overlapping bits)
4. This check must be combined with a positive number check

This is a classic bit manipulation pattern that every programmer should know, as it's both efficient and idiomatic for power-of-2 detection. It's used extensively in systems programming, hash table sizing, memory allocation, and algorithm optimization.

## Related Problems

- [326. Power of Three](https://leetcode.com/problems/power-of-three/)
- [342. Power of Four](https://leetcode.com/problems/power-of-four/)
- [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [461. Hamming Distance](https://leetcode.com/problems/hamming-distance/)
