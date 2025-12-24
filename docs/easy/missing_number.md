# Missing Number

## Problem Summary

Given an array `nums` containing `n` distinct numbers taken from the range `[0, n]`, return the only number in the range that is missing from the array.

**LeetCode Problem**: [268. Missing Number](https://leetcode.com/problems/missing-number/)

**Follow-up**: Could you do it in a single pass with O(1) extra space?

## Approach 1: Mathematical Sum (Implemented)

### Strategy

The implemented solution uses a **mathematical approach**:

1. Calculate the expected sum of all numbers from 0 to n using the formula: `sum = n * (n + 1) / 2`
2. Calculate the actual sum of the array
3. The missing number is the difference between expected and actual sum

**Code**:

```python
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    total = n * (n + 1) // 2
    sum_of_nums = sum(nums)
    return total - sum_of_nums
```

### How It Works

**Example 1**: `nums = [3,0,1]`

```
n = 3
Expected sum of [0,1,2,3] = 3 * 4 / 2 = 6
Actual sum of [3,0,1] = 4
Missing number = 6 - 4 = 2
```

**Example 2**: `nums = [0,1]`

```
n = 2
Expected sum of [0,1,2] = 2 * 3 / 2 = 3
Actual sum of [0,1] = 1
Missing number = 3 - 1 = 2
```

**Example 3**: `nums = [9,6,4,2,3,5,7,0,1]`

```
n = 9
Expected sum of [0..9] = 9 * 10 / 2 = 45
Actual sum = 9+6+4+2+3+5+7+0+1 = 37
Missing number = 45 - 37 = 8
```

### Why This Works

The formula `n * (n + 1) / 2` gives the sum of all integers from 0 to n.

**Derivation**:

```
Sum = 0 + 1 + 2 + ... + n
    = n * (n + 1) / 2  (Gauss's formula)

If we remove one number x:
Sum_of_array = (Sum of 0..n) - x

Therefore:
x = (Sum of 0..n) - Sum_of_array
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass to sum array: O(n)
  - Computing expected sum: O(1)
- **Space Complexity**: O(1)
  - Only using constant extra space

### Edge Cases Handled

1. **Missing 0**: `nums = [1,2,3]` → Expected: 0
2. **Missing n**: `nums = [0,1,2]` → Expected: 3
3. **Single element array**: `nums = [0]` → Expected: 1
4. **Shuffled array**: Works regardless of order
5. **Large numbers**: Works for any n due to O(1) space

## Approach 2: XOR Bit Manipulation

Clever bit manipulation solution that also achieves O(1) space:

```python
def missingNumber(self, nums: List[int]) -> int:
    result = 0
    n = len(nums)

    # XOR all indices and all numbers
    for i in range(n + 1):
        result ^= i

    for num in nums:
        result ^= num

    return result
```

### How It Works

**XOR Properties**:

```
a ^ a = 0  (XOR with itself is 0)
a ^ 0 = a  (XOR with 0 is itself)
XOR is commutative and associative
```

**Example**: `nums = [0,1,3]` (missing 2)

```
result = 0
result ^= 0 = 0
result ^= 1 = 1
result ^= 2 = 3
result ^= 3 = 0  (now all 0..3 XORed)

result ^= 0 = 0  (XOR with array[0])
result ^= 1 = 1  (XOR with array[1])
result ^= 3 = 2  (XOR with array[2])

Final result = 2 (the missing number)
```

**Why it works**:

- XOR all numbers 0 to n: `0 ^ 1 ^ 2 ^ ... ^ n`
- XOR all array elements: `nums[0] ^ nums[1] ^ ...`
- All existing numbers cancel out (appear twice)
- Only the missing number remains

### Complexity

- **Time**: O(n)
- **Space**: O(1)

### Advantages

- No overflow risk (unlike sum approach with very large numbers)
- Elegant bit manipulation

### Disadvantages

- Less intuitive
- Slower in practice (multiple XOR operations)

## Approach 3: Hash Set

Simple approach using extra space:

```python
def missingNumber(self, nums: List[int]) -> int:
    num_set = set(nums)

    for i in range(len(nums) + 1):
        if i not in num_set:
            return i
```

### Analysis

- **Time**: O(n) - Set creation O(n) + lookup O(n)
- **Space**: O(n) - Store all numbers in set
- **Simple and clear** but uses extra space
- Not optimal per follow-up constraint

## Approach 4: Sorting

Sort the array and find the gap:

```python
def missingNumber(self, nums: List[int]) -> int:
    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    # If no gap found, missing number is n
    return len(nums)
```

### Analysis

- **Time**: O(n log n) - Dominated by sorting
- **Space**: O(1) or O(n) - Depends on sort implementation
- **Not optimal** due to O(n log n) time

## Comparison of Approaches

| Approach                       | Time       | Space | Pros            | Cons             |
| ------------------------------ | ---------- | ----- | --------------- | ---------------- |
| Mathematical Sum (Implemented) | O(n)       | O(1)  | Simple, optimal | None             |
| XOR Bit Manipulation           | O(n)       | O(1)  | Overflow-safe   | Less intuitive   |
| Hash Set                       | O(n)       | O(n)  | Clear logic     | Uses extra space |
| Sorting                        | O(n log n) | O(1)  | Simple          | Suboptimal time  |

**Winner**: Mathematical Sum approach - O(n) time, O(1) space

## Edge Cases & Considerations

1. **Single element array**:

   - `nums = [0]` → `1`
   - Expected sum = 1, actual = 0, missing = 1

2. **Missing first number (0)**:

   - `nums = [1,2,3,4,5]` → `0`
   - Expected sum = 15, actual = 15 when starting from 0

3. **Missing last number (n)**:

   - `nums = [0,1,2,3,4]` (n=5)`→`5`
   - Expected sum = 15, actual = 10

4. **Shuffled array**:

   - `nums = [9,6,4,2,3,5,7,0,1]` → `8`
   - Order doesn't matter for sum

5. **Reverse sorted array**:

   - `nums = [8,7,6,5,3,2,1,0]` (n=9)`→`4`
   - Works correctly

6. **Nearly sorted array**:

   - `nums = [0,1,2,3,5,6,7,8]` (n=8)`→`4`
   - Works correctly

7. **Large n**:
   - Works up to n where n\*(n+1)/2 fits in integer
   - Python handles big integers automatically

## Common Pitfalls

1. **Off-by-one error in range**:

   ```python
   # WRONG: Range is [0, n], not [0, n-1]
   total = (n - 1) * n // 2

   # CORRECT: Must include n
   total = n * (n + 1) // 2
   ```

2. **Using sum directly without formula**:

   ```python
   # LESS EFFICIENT: Requires additional list creation
   total = sum(range(n + 1))

   # BETTER: Direct formula
   total = n * (n + 1) // 2
   ```

3. **Integer overflow** (in other languages):

   ```
   // C++: Can overflow with large n
   int total = n * (n + 1) / 2;  // Risk: overflow

   // Fix: Use long long
   long long total = (long long)n * (n + 1) / 2;
   ```

4. **Forgetting the array sum**:

   ```python
   # WRONG: Only calculates expected sum
   def missingNumber(self, nums):
       return len(nums) * (len(nums) + 1) // 2

   # CORRECT: Compare with actual sum
   def missingNumber(self, nums):
       n = len(nums)
       return n * (n + 1) // 2 - sum(nums)
   ```

5. **Not handling empty array edge case**:
   ```python
   # Works even for edge cases due to formula
   # nums = [] → n=0, total=0, sum=0, missing=0 ✓
   ```

## Optimization Notes

The mathematical approach is **optimal**:

- **Time**: O(n) - Must visit each element at least once
- **Space**: O(1) - Can't do better than constant space

**Performance comparison**:

- Mathematical sum: Fast in practice (simple operations)
- XOR: Slower in practice (multiple XOR operations)
- Hash set: Slower (hash operations overhead)
- Sorting: Slowest (O(n log n))

**Why XOR is overflow-safe**:

- XOR doesn't cause overflow like addition
- Better for languages with fixed integer sizes
- Python doesn't have this issue (arbitrary precision)

## Visual Example

```
Array: [3, 0, 1]  (n = 3, so range is [0,1,2,3])

Expected sum:
  0 + 1 + 2 + 3 = 6
  Or: 3 * 4 / 2 = 6

Actual sum:
  3 + 0 + 1 = 4

Missing:
  6 - 4 = 2 ✓


Another example: [0, 1, 2, 3, 5, 6, 7, 8] (n = 8, missing 4)

Expected: 0+1+2+3+4+5+6+7+8 = 36
Or: 8 * 9 / 2 = 36

Actual: 0+1+2+3+5+6+7+8 = 32

Missing: 36 - 32 = 4 ✓
```

## Test Cases

```python
# Basic cases
missingNumber([3,0,1])                    # 2
missingNumber([0,1])                      # 2

# Missing first (0)
missingNumber([1,2,3,4,5])                # 0

# Missing last (n)
missingNumber([0,1,2,3,4])                # 5

# Shuffled
missingNumber([9,6,4,2,3,5,7,0,1])        # 8

# Single element
missingNumber([0])                        # 1
missingNumber([1])                        # 0

# Small list
missingNumber([0,1,3])                    # 2

# Reverse sorted
missingNumber([8,7,6,5,3,2,1,0])          # 4

# Nearly sorted
missingNumber([0,1,2,3,5,6,7,8])          # 4

# Large array
nums = list(range(1001))
nums.remove(500)
missingNumber(nums)                       # 500
```

## Thought Process

**Problem analysis**:

- Array contains n distinct numbers from range [0, n]
- Exactly one number is missing
- Find that missing number

**Key observations**:

1. Array has length n, but contains numbers from [0, n] (which has n+1 numbers)
2. We know what range the numbers are from
3. Sum of [0..n] is predictable

**Approach considerations**:

**Brute force**:

- Check each number 0 to n: O(n²)
- Not optimal

**Hash set**:

- Store all numbers, check which is missing
- O(n) time, O(n) space
- Works but uses extra space

**Mathematical**:

- Use formula for sum: 0+1+2+...+n = n\*(n+1)/2
- Compare expected vs actual
- Missing = expected - actual
- O(n) time, O(1) space ✓ Optimal

This is the cleanest and most efficient approach!

## Related Problems

- [136. Single Number](https://leetcode.com/problems/single-number/)
- [137. Single Number II](https://leetcode.com/problems/single-number-ii/)
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/)
- [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
- [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
