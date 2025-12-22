# Valid Perfect Square

## Problem Summary

Given a positive integer `num`, determine if it is a perfect square (i.e., if there exists an integer `x` such that `x * x == num`). Return `true` if `num` is a perfect square, `false` otherwise.

**LeetCode Problem**: [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

## Approach 1: Square Root Conversion (Implemented)

### Strategy

The implemented solution uses a straightforward mathematical approach:

1. Calculate the square root of `num` using `num ** 0.5`
2. Convert the result to an integer (truncates decimals)
3. Square this integer and check if it equals the original number

**Code**:

```python
def isPerfectSquare(self, num: int) -> bool:
    ans = int(num ** 0.5)
    return ans * ans == num
```

### How It Works

- For `num = 16`: `int(16 ** 0.5) = 4`, and `4 * 4 = 16` ✓
- For `num = 14`: `int(14 ** 0.5) = 3`, and `3 * 3 = 9 ≠ 14` ✗
- The truncation via `int()` ensures we only check the integer part

### Complexity Analysis

- **Time Complexity**: O(1) - Single square root calculation and comparison
- **Space Complexity**: O(1) - Only storing one integer value

### Edge Cases Handled

- **1**: Smallest perfect square (1² = 1) ✓
- **0**: Zero is technically a perfect square (0² = 0) ✓
- **Large perfect squares**: e.g., 1000000 (1000²) works correctly
- **Large numbers**: The float precision can handle up to ~2⁵³ accurately

## Approach 2: Binary Search (Alternative)

For a more algorithmic approach without using square root operations:

```python
def isPerfectSquare(self, num: int) -> bool:
    if num < 2:
        return True

    left, right = 2, num // 2
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

### Complexity

- **Time**: O(log n) - Binary search on range [2, n/2]
- **Space**: O(1) - Constant extra space

### When to Use

- When you want to avoid floating-point arithmetic
- When the problem explicitly disallows built-in sqrt functions
- For interview settings where the "algorithm" is more important than the "solution"

## Approach 3: Newton's Method (Mathematical)

An iterative mathematical approach to find the square root:

```python
def isPerfectSquare(self, num: int) -> bool:
    if num < 2:
        return True

    x = num
    while x * x > num:
        x = (x + num // x) // 2

    return x * x == num
```

### Complexity

- **Time**: O(log n) - Converges quadratically
- **Space**: O(1)

### Advantages

- Very fast convergence (fewer iterations than binary search)
- No floating-point operations
- Mathematically elegant

## Approach 4: Mathematical Property (Odd Numbers)

Perfect squares are sums of consecutive odd numbers: 1 + 3 + 5 + ... = n²

```python
def isPerfectSquare(self, num: int) -> bool:
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0
```

### Complexity

- **Time**: O(√n) - Need to subtract √n odd numbers
- **Space**: O(1)

This is less efficient but demonstrates an interesting mathematical property.

## Edge Cases & Considerations

1. **Floating-Point Precision**:

   - For very large numbers (> 2⁵³), floating-point square root may lose precision
   - The implemented approach works for most practical cases
   - For extreme accuracy requirements, use integer-only methods (binary search or Newton's)

2. **Zero and One**: Both are perfect squares and must return `True`

3. **Negative Numbers**: The problem specifies positive integers, so no handling needed

4. **Performance**:
   - For single checks: The sqrt approach is fastest O(1)
   - For repeated checks without sqrt: Binary search or Newton's method
   - For educational purposes: Odd numbers sum demonstrates math property

## Common Pitfalls

1. **Direct Comparison with sqrt**: Don't do `num == int(num ** 0.5) ** 2` - reversed logic
2. **Float Precision**: For very large numbers, consider integer-only methods
3. **Off-by-One**: In binary search, ensure `right = num // 2` (not `num`) to avoid overflow
4. **Rounding vs Truncation**: Use `int()` for truncation, not `round()` which rounds to nearest

## Optimization Notes

- The implemented solution is optimal for the general case: O(1) time and space
- If sqrt operations are not allowed, binary search is the next best: O(log n)
- Newton's method provides the best balance between efficiency and avoiding floats
- The mathematical property approach is too slow for large inputs: O(√n)

## Test Cases

```python
# Perfect squares
isPerfectSquare(1)         # True (1²)
isPerfectSquare(4)         # True (2²)
isPerfectSquare(16)        # True (4²)
isPerfectSquare(1000000)   # True (1000²)

# Non-perfect squares
isPerfectSquare(14)        # False
isPerfectSquare(999999)    # False

# Edge cases
isPerfectSquare(0)         # True (0²)
isPerfectSquare(2)         # False

# Large numbers
isPerfectSquare(12345678987654321)  # True (111111111²)
isPerfectSquare(123456789)          # False
```

## Thought Process

The implemented solution leverages Python's built-in exponentiation for simplicity and efficiency. The key insight is that if we truncate the square root to an integer, squaring it back should give us the original number only if it was a perfect square. This approach is elegant, concise, and performs in constant time, making it ideal for the problem constraints.

For scenarios where built-in mathematical functions are restricted (common in interviews), binary search provides a clean algorithmic alternative that demonstrates problem-solving skills while maintaining good performance.

## Related Problems

- [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/)
- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)
