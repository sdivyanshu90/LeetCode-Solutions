# Power of Four

## Problem Summary

Given an integer `n`, return `true` if it is a power of four (i.e., if there exists an integer `x` such that `n == 4^x`). Otherwise, return `false`.

**LeetCode Problem**: [342. Power of Four](https://leetcode.com/problems/power-of-four/)

## Approach 1: Iterative Division (Implemented)

### Strategy

The implemented solution uses a straightforward iterative approach:

1. Handle edge case: if `n < 1`, return `False` (powers of 4 are always positive)
2. Repeatedly divide `n` by 4 while it's greater than 1
3. If at any point `n` is not divisible by 4, return `False`
4. If the loop completes with `n == 1`, return `True`

**Code**:

```python
def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
        return False

    while n > 1:
        if n % 4 != 0:
            return False
        n //= 4
    return True
```

### How It Works

- For `n = 16`: 16 → 4 → 1 (all divisible by 4) ✓
- For `n = 8`: 8 → 2 (not divisible by 4) ✗
- For `n = 1`: Already 1, which is 4⁰ = 1 ✓

### Complexity Analysis

- **Time Complexity**: O(log₄ n) = O(log n) - We divide by 4 each iteration
- **Space Complexity**: O(1) - Only using constant extra space

### Edge Cases Handled

- **Negative numbers**: Return `False` immediately (n < 1)
- **Zero**: Return `False` (0 is not a power of 4)
- **One**: Returns `True` (4⁰ = 1)
- **Large powers**: e.g., 1073741824 (4¹⁵) works correctly

## Approach 2: Logarithmic (Mathematical)

Use logarithms to check if log₄(n) is an integer:

```python
import math

def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
        return False
    log_val = math.log(n, 4)
    return log_val == int(log_val)
```

### Complexity

- **Time**: O(1) - Single logarithm calculation
- **Space**: O(1)

### Caveat

- Floating-point precision issues can cause incorrect results for large numbers
- Better to check: `abs(log_val - round(log_val)) < 1e-10`

## Approach 3: Bit Manipulation (Optimal)

Powers of 4 have specific bit patterns:

- Must be a power of 2: `n & (n-1) == 0`
- Must have the bit at an even position (0, 2, 4, 6, ...)

```python
def isPowerOfFour(self, n: int) -> bool:
    # Check if positive, power of 2, and bit is at even position
    # 0x55555555 = 0b01010101010101010101010101010101 (bits at even positions)
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```

### How It Works

1. `n > 0`: Powers of 4 are positive
2. `n & (n-1) == 0`: Checks if n is a power of 2
   - Powers of 2 have exactly one bit set
3. `n & 0x55555555 != 0`: Checks if that bit is at an even position
   - 0x55555555 has bits set at positions 0, 2, 4, 6, ..., 30
   - Powers of 4: 1 (2⁰), 4 (2²), 16 (2⁴), 64 (2⁶), ...
   - Powers of 2 but not 4: 2 (2¹), 8 (2³), 32 (2⁵), ... would fail this check

### Examples

- `n = 16` (0b10000): `16 & 15 = 0` ✓, `16 & 0x55555555 = 16` ✓
- `n = 8` (0b1000): `8 & 7 = 0` ✓, `8 & 0x55555555 = 0` ✗ (bit at position 3, odd)

### Complexity

- **Time**: O(1) - Three bitwise operations
- **Space**: O(1)

### Why This Works

Powers of 4 are powers of 2 where the exponent is even:

- 4⁰ = 2⁰ = 1 (bit at position 0)
- 4¹ = 2² = 4 (bit at position 2)
- 4² = 2⁴ = 16 (bit at position 4)
- 4³ = 2⁶ = 64 (bit at position 6)

## Approach 4: Modulo Property

Powers of 4 have the property: `4^x % 3 == 1` for all x ≥ 0

```python
def isPowerOfFour(self, n: int) -> bool:
    # Must be positive, power of 2, and satisfy modulo property
    return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
```

### Mathematical Proof

- 4 ≡ 1 (mod 3)
- Therefore, 4^x ≡ 1^x ≡ 1 (mod 3) for all x ≥ 0

### Why This Works

- 1 % 3 = 1 ✓
- 4 % 3 = 1 ✓
- 16 % 3 = 1 ✓
- 64 % 3 = 1 ✓
- But 2 % 3 = 2 ✗, 8 % 3 = 2 ✗ (powers of 2 but not 4)

### Complexity

- **Time**: O(1) - Constant operations
- **Space**: O(1)

## Comparison of Approaches

| Approach           | Time     | Space | Pros                          | Cons                             |
| ------------------ | -------- | ----- | ----------------------------- | -------------------------------- |
| Iterative Division | O(log n) | O(1)  | Simple, intuitive             | Slower for large n               |
| Logarithmic        | O(1)     | O(1)  | Fast                          | Floating-point precision issues  |
| Bit Manipulation   | O(1)     | O(1)  | Fastest, no precision issues  | Less intuitive                   |
| Modulo Property    | O(1)     | O(1)  | Elegant mathematical property | Requires understanding the proof |

## Edge Cases & Considerations

1. **Negative Numbers**: Cannot be powers of 4 (4^x is always positive)
2. **Zero**: Not a power of 4
3. **One**: Special case - 4⁰ = 1, should return `True`
4. **Powers of 2 but not 4**: Numbers like 2, 8, 32, 128 should return `False`
5. **Large Numbers**:
   - Max power of 4 in 32-bit signed: 4¹⁵ = 1,073,741,824
   - The iterative approach handles these correctly

## Common Pitfalls

1. **Confusing with Power of Two**:

   - 8 is 2³ (power of 2) but not a power of 4
   - Must check that the exponent of 2 is even

2. **Off-by-One with n = 1**:

   - 1 = 4⁰, so it IS a power of 4
   - Don't start loop at `n == 1`

3. **Float Precision in Log Approach**:

   - Direct equality check `log_val == int(log_val)` can fail
   - Use epsilon comparison: `abs(log_val - round(log_val)) < 1e-10`

4. **Bitwise Mask Size**:

   - 0x55555555 works for 32-bit integers
   - For 64-bit: use 0x5555555555555555

5. **Forgetting Negative Check**:
   - In bit manipulation, ensure `n > 0` check
   - Negative numbers have different bit representations

## Optimization Notes

- **For Interviews**: The bit manipulation approach (Approach 3 or 4) is most impressive
- **For Production**: The iterative approach is clearest and most maintainable
- **For Performance**: O(1) bit manipulation is optimal
- **Best Practice**: Use modulo property (Approach 4) - combines clarity with efficiency

## Test Cases

```python
# Powers of four
isPowerOfFour(1)            # True (4⁰)
isPowerOfFour(4)            # True (4¹)
isPowerOfFour(16)           # True (4²)
isPowerOfFour(64)           # True (4³)
isPowerOfFour(1073741824)   # True (4¹⁵, max 32-bit)

# Powers of two but not four
isPowerOfFour(2)            # False (2¹)
isPowerOfFour(8)            # False (2³)
isPowerOfFour(32)           # False (2⁵)

# Non-powers
isPowerOfFour(5)            # False
isPowerOfFour(1000000000)   # False
isPowerOfFour(1073741823)   # False (one less than 4¹⁵)

# Edge cases
isPowerOfFour(0)            # False
isPowerOfFour(-4)           # False
isPowerOfFour(-16)          # False
```

## Thought Process

The implemented iterative solution is straightforward and easy to understand: repeatedly divide by 4 until we can't anymore, checking divisibility at each step. This approach directly mirrors the mathematical definition of a power of 4.

However, for optimal performance and interview scenarios, the bit manipulation or modulo approaches are preferred. They reduce the problem to O(1) constant-time checks by exploiting mathematical properties:

- Bit manipulation: Powers of 4 are powers of 2 with the bit at even positions
- Modulo property: 4^x % 3 always equals 1

Both O(1) approaches are elegant and demonstrate deep understanding of number theory and bit operations.

## Related Problems

- [231. Power of Two](https://leetcode.com/problems/power-of-two/)
- [326. Power of Three](https://leetcode.com/problems/power-of-three/)
- [1492. The kth Factor of n](https://leetcode.com/problems/the-kth-factor-of-n/)
