# Sqrt(x)

## Problem Summary

Given a non-negative integer `x`, return the square root of `x` **rounded down to the nearest integer**. The returned integer should also be non-negative.

You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

**LeetCode Problem**: [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

## Approach 1: Binary Search (Implemented)

### Strategy

The implemented solution uses a **binary search approach**:

1. Handle the special case where `x = 0`
2. Initialize search range: `left = 1`, `right = x`
3. Binary search to find the largest number whose square is ≤ x
4. Use the condition `mid <= x // mid` to avoid integer overflow
5. Return the largest valid `mid` found

**Code**:

```python
def mySqrt(self, x: int) -> int:
    if x == 0:
        return 0

    left, right = 1, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        if mid <= x // mid:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### How It Works

**Example 1**: `x = 8`

```
Find largest integer k where k² ≤ 8

Initial: left=1, right=8, result=0

Iteration 1:
  mid = 1 + (8-1)//2 = 4
  4 <= 8//4? → 4 <= 2? No
  right = 4 - 1 = 3

Iteration 2:
  mid = 1 + (3-1)//2 = 2
  2 <= 8//2? → 2 <= 4? Yes
  result = 2
  left = 2 + 1 = 3

Iteration 3:
  mid = 3 + (3-3)//2 = 3
  3 <= 8//3? → 3 <= 2? No
  right = 3 - 1 = 2

left > right, exit loop
Return result = 2 ✓
```

**Example 2**: `x = 4`

```
Find k where k² ≤ 4

Initial: left=1, right=4, result=0

Iteration 1:
  mid = 1 + (4-1)//2 = 2
  2 <= 4//2? → 2 <= 2? Yes
  result = 2
  left = 3

Iteration 2:
  mid = 3 + (4-3)//2 = 3
  3 <= 4//3? → 3 <= 1? No
  right = 2

left > right, exit loop
Return result = 2 ✓
```

### Key Techniques

**Avoid Overflow**:

- Instead of `mid * mid <= x`, use `mid <= x // mid`
- Multiplication might overflow, division is safer
- Integer division avoids floating point issues

**Binary Search Pattern**:

- Standard binary search with modification
- Looking for the largest value satisfying a condition
- Update result when condition is true, then search right half

### Complexity Analysis

- **Time Complexity**: O(log x)
  - Binary search halves search space each iteration
  - Maximum iterations: log₂(x)
- **Space Complexity**: O(1)
  - Only using pointers and variables, no extra data structures

### Edge Cases Handled

1. **x = 0**: Returns 0 immediately
2. **x = 1**: Binary search finds 1 correctly
3. **Perfect squares**: `4 → 2`, `16 → 4`, `25 → 5`
4. **Non-perfect squares**: `8 → 2`, `26 → 5` (rounds down)
5. **Very large numbers**: `2147483647 → 46340` (no overflow with division)

## Approach 2: Newton's Method

Mathematical iterative approach:

```python
def mySqrt(self, x: int) -> int:
    if x == 0:
        return 0

    # Start with initial guess
    root = x

    while root * root > x:
        # Newton's method: next = (current + x/current) / 2
        root = (root + x // root) // 2

    return root
```

### How It Works

**Newton's Method Formula**:

```
If y is current approximation for sqrt(x),
next approximation = (y + x/y) / 2
```

Converges very quickly to the square root.

**Example**: `x = 8`

```
root = 8

Iteration 1:
  8*8 = 64 > 8? Yes
  root = (8 + 8//8) // 2 = (8 + 1) // 2 = 4

Iteration 2:
  4*4 = 16 > 8? Yes
  root = (4 + 8//4) // 2 = (4 + 2) // 2 = 3

Iteration 3:
  3*3 = 9 > 8? Yes
  root = (3 + 8//3) // 2 = (3 + 2) // 2 = 2

Iteration 4:
  2*2 = 4 > 8? No
  Return 2 ✓
```

### Advantages

- **Faster convergence**: Typically fewer iterations than binary search
- **Elegant**: Natural mathematical approach
- **O(log log x)** in theory, but O(log x) worst case in practice

### Disadvantages

- **Less intuitive** for some developers
- **Division by zero risk** if starting with 0 (handled by checking x first)

### Complexity

- **Time**: O(log log x) typically, O(log x) worst case
- **Space**: O(1)

## Approach 3: Bit Manipulation

Use bit operations to construct the answer:

```python
def mySqrt(self, x: int) -> int:
    result = 0
    i = 15  # 2^15 > sqrt(2^31 - 1), so start from here

    while i >= 0:
        # Try adding the i-th bit to result
        if (result | (1 << i)) ** 2 <= x:
            result |= (1 << i)
        i -= 1

    return result
```

### How It Works

Build the answer bit by bit, trying each bit position from high to low.

**Example**: `x = 8` (binary: 1000)

```
result = 0, i = 15 to 3 (skip, bits too high)

i = 2:
  (0 | (1<<2))² = 4² = 16 > 8? Yes, don't set
  result = 0

i = 1:
  (0 | (1<<1))² = 2² = 4 <= 8? Yes, set
  result = 10 (binary) = 2

i = 0:
  (2 | (1<<0))² = 3² = 9 > 8? Yes, don't set
  result = 2

Return 2 ✓
```

### Complexity

- **Time**: O(log x) - 32 iterations for 32-bit integers
- **Space**: O(1)

### Disadvantages

- **Not intuitive** for beginners
- **Bit operations** slower in practice than division
- **Fixed iterations** unlike binary search which adapts

## Approach 4: Linear Search (Naive)

Simple brute force approach:

```python
def mySqrt(self, x: int) -> int:
    for i in range(x + 1):
        if i * i > x:
            return i - 1
    return x
```

### Analysis

- **Time**: O(√x) - Can optimize to O(√x) by only checking up to √x
- **Space**: O(1)
- **Too slow** for large values
- Not suitable for interview

## Approach 5: Built-in Function (Reference Only)

Python's math library:

```python
import math

def mySqrt(self, x: int) -> int:
    return int(math.sqrt(x))
```

### Notes

- **Not allowed** per problem constraints
- Given for reference only
- Used for verification in testing

## Comparison of Approaches

| Approach                    | Time           | Space | Pro                           | Con               |
| --------------------------- | -------------- | ----- | ----------------------------- | ----------------- |
| Binary Search (Implemented) | O(log x)       | O(1)  | Standard, intuitive, reliable | Standard approach |
| Newton's Method             | O(log log x)\* | O(1)  | Faster convergence            | Less intuitive    |
| Bit Manipulation            | O(log x)       | O(1)  | Bit-level insight             | Complex logic     |
| Linear Search               | O(√x)          | O(1)  | Simplest                      | Too slow          |
| Built-in                    | O(1)           | O(1)  | Instant                       | Not allowed       |

**Winner**: Binary Search - O(log x) time, O(1) space, most reliable

## Edge Cases & Considerations

1. **x = 0**:

   - `mySqrt(0)` → `0`
   - Special case, returns immediately

2. **x = 1**:

   - `mySqrt(1)` → `1`
   - Binary search handles correctly

3. **Perfect squares**:

   - `mySqrt(4)` → `2` (2² = 4)
   - `mySqrt(16)` → `4` (4² = 16)
   - `mySqrt(25)` → `5` (5² = 25)

4. **Non-perfect squares** (rounding down):

   - `mySqrt(8)` → `2` (2² = 4 < 8 < 9 = 3²)
   - `mySqrt(26)` → `5` (5² = 25 < 26 < 36 = 6²)

5. **Large numbers**:

   - `mySqrt(2147483647)` → `46340` (max 32-bit int)
   - No overflow with integer division approach

6. **Powers of 2**:

   - `mySqrt(1)` → `1`
   - `mySqrt(2)` → `1`
   - `mySqrt(4)` → `2`
   - `mySqrt(8)` → `2`

7. **Numbers near perfect squares**:
   - `mySqrt(99)` → `9` (99 is just below 100)
   - `mySqrt(101)` → `10` (101 is just above 100)

## Common Pitfalls

1. **Using multiplication instead of division**:

   ```python
   # RISKY: Potential overflow
   if mid * mid <= x:
       result = mid

   # BETTER: Use division
   if mid <= x // mid:
       result = mid
   ```

2. **Incorrect binary search initialization**:

   ```python
   # WRONG: If x < 1, right could be negative
   left, right = 0, x

   # CORRECT: Handle x=0 separately or set right appropriately
   if x == 0:
       return 0
   left, right = 1, x
   ```

3. **Integer division rounding**:

   ```python
   # WRONG: Using floating point
   mid = (left + right) / 2.0

   # CORRECT: Use integer division
   mid = left + (right - left) // 2
   ```

4. **Forgetting to update result**:

   ```python
   # WRONG: Never capture valid answer
   while left <= right:
       mid = ...
       if condition:
           left = mid + 1  # Missing: result = mid

   # CORRECT: Store the last valid result
   if mid <= x // mid:
       result = mid  # Capture answer
       left = mid + 1
   ```

5. **Off-by-one errors**:

   ```python
   # WRONG: right = x causes large search space
   left, right = 1, x  # For x=100, searches [1..100]

   # CORRECT but inefficient: right = x works but slower
   # BETTER: For large x, could use right = x // 2 or similar
   ```

## Optimization Notes

The binary search approach is **optimal** for this problem:

- **Time**: O(log x) - Best possible for comparison-based search
- **Space**: O(1) - Minimum possible (only pointers)

**Practical optimizations**:

1. **Right boundary**: Could use `right = x // 2` for x ≥ 2 (since √x ≤ x/2)
2. **Avoid multiplication**: Always use division to prevent overflow
3. **Early termination**: When mid²exactly equals x

**Newton's Method insight**:

- Theoretically faster (O(log log x))
- Practically similar due to constant factors
- More sensitive to starting value

## Visual Example

```
Finding sqrt(8):

Search space narrows:
[1, 8] → mid=4 → 4>8//4? No → result=4, search right
[5, 8] → mid=6 → 6>8//6? Yes → search left
[5, 5] → mid=5 → 5>8//5? Yes → search left
[5, 4] → left > right, exit

Actually for x=8:
[1, 8] → mid=4 → 4 > 2? No, result=4, left=5... WAIT

Let me redo:
x=8, left=1, right=8

Iteration 1: mid=4
  4 <= 8//4? → 4 <= 2? No
  right = 3

Iteration 2: mid=2
  2 <= 8//2? → 2 <= 4? Yes
  result=2, left=3

Iteration 3: mid=3
  3 <= 8//3? → 3 <= 2? No
  right=2

left > right, return 2 ✓

Visual of answer:
  √8 ≈ 2.83, rounded down = 2
```

## Test Cases

```python
# Basic perfect squares
mySqrt(4)                    # 2
mySqrt(16)                   # 4
mySqrt(25)                   # 5
mySqrt(100)                  # 10

# Non-perfect squares (rounding down)
mySqrt(8)                    # 2
mySqrt(26)                   # 5

# Edge cases
mySqrt(0)                    # 0
mySqrt(1)                    # 1
mySqrt(2)                    # 1
mySqrt(3)                    # 1

# Large numbers
mySqrt(2147395599)           # 46339
mySqrt(2147483647)           # 46340

# More test cases
mySqrt(6)                    # 2
mySqrt(7)                    # 2
mySqrt(9)                    # 3
mySqrt(15)                   # 3
mySqrt(18)                   # 4
mySqrt(36)                   # 6
```

## Thought Process

**Problem analysis**:

- Find the integer square root (floor)
- Cannot use built-in power functions
- Should be efficient for large numbers

**Key observations**:

1. For any x, sqrt(x) is in range [0, x]
2. For x ≥ 1, sqrt(x) ≤ x/2 (tighter bound)
3. Need to find largest integer k where k² ≤ x

**Approach considerations**:

**Why not linear search?**

- O(√x) time is too slow for x up to 2^31
- For x = 2^31, √x ≈ 46000 iterations ✓ (actually acceptable)
- But binary search is better: O(log x) ≈ 31 iterations

**Why binary search?**

- Logarithmic time complexity
- Natural fit for "find value in range"
- Avoids multiplication overflow

**Why use `mid <= x // mid` instead of `mid * mid <= x`?**

- Multiplication: mid\*mid could overflow for large mid
- Division: x // mid is always safe in integer math
- Equivalent: mid ≤ x/mid ⟺ mid² ≤ x

**Why Newton's method?**

- Even faster theoretically
- Natural mathematical approach
- But more iterations due to integer rounding

The binary search approach is the standard, reliable solution for this problem!

## Related Problems

- [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
- [1300. Sum of Mutated Array Closest to Target](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/)
