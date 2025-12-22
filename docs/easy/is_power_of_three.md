# Power of Three

## Problem Summary

Given an integer `n`, return `true` if it is a power of three (i.e., if there exists an integer `x` such that `n == 3^x`). Otherwise, return `false`.

**LeetCode Problem**: [326. Power of Three](https://leetcode.com/problems/power-of-three/)

## Approach 1: Maximum Power Division (Implemented)

### Strategy

The implemented solution uses an **elegant mathematical trick**:

1. Find the largest power of 3 that fits in a 32-bit signed integer: 3¹⁹ = 1,162,261,467
2. If `n` is a power of 3, it must be a divisor of this maximum power
3. Check: `n > 0 and 1162261467 % n == 0`

**Code**:

```python
def isPowerOfThree(self, n: int) -> bool:
    return n > 0 and 1162261467 % n == 0
```

### How It Works

Since 3 is a prime number, the only divisors of 3^19 are powers of 3:

- Divisors of 3¹⁹: 3⁰, 3¹, 3², 3³, ..., 3¹⁹
- Any other number will not divide 3¹⁹ evenly

### Examples

- For `n = 27`: 27 = 3³, and 1162261467 % 27 = 0 ✓
- For `n = 10`: 10 is not a power of 3, so 1162261467 % 10 ≠ 0 ✗
- For `n = 1`: 1 = 3⁰, and 1162261467 % 1 = 0 ✓

### Why 1162261467?

This is the maximum power of 3 that fits in a 32-bit signed integer:

- 3¹⁹ = 1,162,261,467 < 2³¹ - 1 = 2,147,483,647
- 3²⁰ = 3,486,784,401 > 2³¹ - 1 (overflow!)

### Complexity Analysis

- **Time Complexity**: O(1) - Single modulo operation
- **Space Complexity**: O(1) - No extra space

### Edge Cases Handled

- **Negative numbers**: Return `False` via `n > 0` check
- **Zero**: Return `False` (0 is not a power of 3)
- **One**: Returns `True` (3⁰ = 1, and 1162261467 % 1 = 0)
- **Maximum power**: 1162261467 itself returns `True`

## Approach 2: Iterative Division

A more traditional approach that repeatedly divides by 3:

```python
def isPowerOfThree(self, n: int) -> bool:
    if n < 1:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1
```

### How It Works

- Keep dividing by 3 while possible
- If we end up with 1, it was a power of 3
- If we get stuck with a remainder, it wasn't

### Examples

- `n = 27`: 27 → 9 → 3 → 1 ✓
- `n = 10`: 10 (not divisible by 3) ✗

### Complexity

- **Time**: O(log₃ n) = O(log n) - Divide by 3 each iteration
- **Space**: O(1)

### When to Use

- When the "magic number" approach seems unclear
- When you need to support arbitrary integer sizes (beyond 32-bit)
- For educational clarity

## Approach 3: Logarithmic

Use logarithms to check if log₃(n) is an integer:

```python
import math

def isPowerOfThree(self, n: int) -> bool:
    if n < 1:
        return False

    log_val = math.log(n, 3)
    return abs(log_val - round(log_val)) < 1e-10
```

### Complexity

- **Time**: O(1) - Single logarithm calculation
- **Space**: O(1)

### Caveats

- **Floating-point precision**: Must use epsilon comparison, not exact equality
- **Less reliable** for edge cases due to float arithmetic
- Not recommended for production code

## Approach 4: Recursive

A recursive version of the iterative division:

```python
def isPowerOfThree(self, n: int) -> bool:
    if n == 1:
        return True
    if n < 1 or n % 3 != 0:
        return False
    return self.isPowerOfThree(n // 3)
```

### Complexity

- **Time**: O(log n) - Same as iterative
- **Space**: O(log n) - Recursive call stack

### Drawback

- Uses more space than iterative (call stack)
- Risk of stack overflow for very large inputs
- No real advantage over iterative approach

## Why the Maximum Power Approach is Brilliant

### Key Insight: 3 is Prime

Since 3 is prime, the **only** positive divisors of 3^k are {1, 3, 3², 3³, ..., 3^k}

This property doesn't work for composite numbers:

- **Power of 4**: 4² = 16 has divisors {1, 2, 4, 8, 16}
  - 2 and 8 divide 16 but aren't powers of 4!
- **Power of 6**: 6² = 36 has divisors {1, 2, 3, 4, 6, 9, 12, 18, 36}
  - Many non-powers of 6 divide it!

### Mathematical Proof

If n is a positive divisor of 3^19:

- By fundamental theorem of arithmetic: n = 3^a × (product of other primes)
- But 3^19 has no other prime factors
- Therefore: n = 3^a where 0 ≤ a ≤ 19
- Thus n is a power of 3

### Trade-offs

**Pros**:

- O(1) time - fastest possible
- Extremely concise (one line)
- No loops or recursion

**Cons**:

- Requires knowing the maximum power (1162261467)
- Less intuitive at first glance
- Only works because 3 is prime
- Limited to 32-bit integers (for the specific constant)

## Comparison of Approaches

| Approach           | Time     | Space    | Pros                      | Cons                              |
| ------------------ | -------- | -------- | ------------------------- | --------------------------------- |
| Max Power Division | O(1)     | O(1)     | Fastest, most elegant     | Requires magic number, prime-only |
| Iterative Division | O(log n) | O(1)     | Clear, works for any size | Slower                            |
| Logarithmic        | O(1)     | O(1)     | Mathematical              | Floating-point precision issues   |
| Recursive          | O(log n) | O(log n) | Functional style          | Extra space, no advantages        |

## Edge Cases & Considerations

1. **Zero and Negative Numbers**:

   - Not powers of 3 (3^x is always positive)
   - Handled by `n > 0` check

2. **One**:

   - Special case: 3⁰ = 1
   - Correctly returns `True` (1162261467 % 1 = 0)

3. **Maximum Power of Three**:

   - 3¹⁹ = 1,162,261,467
   - This is the largest power of 3 in 32-bit signed integers
   - Should return `True`

4. **Powers of Other Numbers**:

   - 9 = 3², returns `True` ✓
   - 8 = 2³, returns `False` ✓
   - 6 = 2 × 3, returns `False` ✓

5. **Large Non-Powers**:
   - 1,000,000,000: Not a power of 3, returns `False`
   - 1,162,261,466: One less than 3¹⁹, returns `False`

## Common Pitfalls

1. **Using the Approach for Non-Primes**:

   - This trick **only works for prime bases**
   - Don't use for power of 4, 6, 8, 9, etc.
   - For composite numbers, use iterative division

2. **Wrong Maximum Power**:

   - Don't use 3²⁰ (causes overflow)
   - Must use 3¹⁹ for 32-bit integers

3. **Forgetting the Positive Check**:

   - Must verify `n > 0`
   - Negative numbers can have 0 remainder

4. **Float Precision in Log Approach**:

   - Never use `log_val == int(log_val)`
   - Always use epsilon comparison

5. **Off-by-One with n = 1**:
   - Remember that 3⁰ = 1
   - Don't exclude 1 from valid answers

## When to Use Each Approach

### In Interviews

- **Show the iterative approach first** - demonstrates clear thinking
- **Then optimize to O(1)** - shows mathematical insight
- **Explain why it only works for primes** - demonstrates deep understanding

### In Production

- **Use the max power approach** - most efficient
- **Add a comment** explaining the magic number
- **Consider iterative if clarity is more important** than micro-optimization

### For Learning

- **Start with iterative** - easiest to understand
- **Learn the mathematical trick** - expands problem-solving toolkit
- **Avoid logarithmic** - unreliable due to floating-point

## Optimization Notes

The implemented O(1) solution is **optimal** - you cannot do better than constant time. The trade-off is that it:

- Requires a specific constant (1162261467)
- Only works because 3 is prime
- Is limited to 32-bit integers

For 64-bit integers, the maximum would be 3³⁹ = 4,052,555,153,018,976,267.

## Test Cases

```python
# Powers of three
isPowerOfThree(1)            # True (3⁰)
isPowerOfThree(3)            # True (3¹)
isPowerOfThree(9)            # True (3²)
isPowerOfThree(27)           # True (3³)
isPowerOfThree(1162261467)   # True (3¹⁹, max 32-bit)

# Non-powers of three
isPowerOfThree(2)            # False
isPowerOfThree(10)           # False
isPowerOfThree(1000000000)   # False
isPowerOfThree(1162261466)   # False (one less than 3¹⁹)

# Edge cases
isPowerOfThree(0)            # False
isPowerOfThree(-3)           # False
isPowerOfThree(-27)          # False

# Powers of other numbers
isPowerOfThree(4)            # False (2²)
isPowerOfThree(8)            # False (2³)
isPowerOfThree(6)            # False (2 × 3)
```

## Thought Process

The implemented solution showcases a brilliant mathematical optimization. By recognizing that:

1. 3 is **prime**
2. The only divisors of a prime power are lower powers of that prime
3. We can pre-compute the maximum power that fits in our integer type

We transform an O(log n) problem into an O(1) problem with a single modulo operation. This is a classic example of trading a small amount of space (one constant) for significant time savings, and leveraging mathematical properties (primality) for algorithmic efficiency.

This approach is specific to prime bases and wouldn't work for composite numbers like 4, 6, or 9, making it a great interview discussion point about when optimizations apply.

## Related Problems

- [231. Power of Two](https://leetcode.com/problems/power-of-two/)
- [342. Power of Four](https://leetcode.com/problems/power-of-four/)
- [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)
