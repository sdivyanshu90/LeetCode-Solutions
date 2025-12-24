# Single Number

## Problem Summary

Given a non-empty array of integers `nums`, every element appears **twice except for one element which appears once**. Find that single element.

You must implement a solution with a linear runtime complexity O(n) and use only O(1) extra space.

**LeetCode Problem**: [136. Single Number](https://leetcode.com/problems/single-number/)

## Approach 1: Hash Map (Implemented)

### Strategy

The implemented solution uses **a hash map to count occurrences**:

1. Create a dictionary to store character counts
2. Iterate through all numbers and increment their count
3. Iterate through the dictionary and return the number with count = 1

**Code**:

```python
def singleNumber(self, nums: List[int]) -> int:
    num_count = {}

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == 1:
            return num
```

### How It Works

**Example 1**: `nums = [2, 2, 1]`

```
Dictionary building:
  num=2: num_count = {2: 1}
  num=2: num_count = {2: 2}
  num=1: num_count = {2: 2, 1: 1}

Finding single number:
  (2, 2): count != 1, skip
  (1, 1): count == 1, return 1 ✓
```

**Example 2**: `nums = [4, 1, 2, 1, 2]`

```
Dictionary building:
  num=4: num_count = {4: 1}
  num=1: num_count = {4: 1, 1: 1}
  num=2: num_count = {4: 1, 1: 1, 2: 1}
  num=1: num_count = {4: 1, 1: 2, 2: 1}
  num=2: num_count = {4: 1, 1: 2, 2: 2}

Finding single number:
  (4, 1): count == 1, return 4 ✓
```

**Example 3**: `nums = [-1, -1, -2]`

```
Dictionary building:
  num=-1: num_count = {-1: 1}
  num=-1: num_count = {-1: 2}
  num=-2: num_count = {-1: 2, -2: 1}

Finding single number:
  (-1, 2): count != 1, skip
  (-2, 1): count == 1, return -2 ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - First pass: iterate through all n elements to build dictionary
  - Second pass: iterate through dictionary (at most n entries)
  - Total: O(n) + O(n) = O(n)
- **Space Complexity**: O(n)
  - Dictionary stores up to n unique numbers
  - Worst case: all different numbers except one duplicate
  - Actually stores at most (n+1)/2 unique numbers (since all except one appear twice)

### Advantages

- **Easy to understand**: Clear logic, straightforward code
- **Handles all cases**: Works with negative numbers, zeros, any values
- **Reliable**: No bit manipulation tricks needed

### Disadvantages

- **Uses O(n) space**: Violates the O(1) space constraint
- **Two passes**: Requires iterating through data twice
- **Not optimal**: Better solutions exist

## Approach 2: XOR Bitwise Operator (Optimal)

Use XOR operation to achieve O(1) space:

```python
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
```

### How XOR Works

**XOR Properties**:

- `a ^ a = 0` (same number XORed = 0)
- `a ^ 0 = a` (any number XORed with 0 = itself)
- `a ^ b = b ^ a` (XOR is commutative)
- `(a ^ b) ^ c = a ^ (b ^ c)` (XOR is associative)

**Example**: `nums = [4, 1, 2, 1, 2]`

```
result = 0

result ^= 4: result = 0 ^ 4 = 4
result ^= 1: result = 4 ^ 1 = 5 (binary: 100 ^ 001 = 101)
result ^= 2: result = 5 ^ 2 = 7 (binary: 101 ^ 010 = 111)
result ^= 1: result = 7 ^ 1 = 6 (binary: 111 ^ 001 = 110)
result ^= 2: result = 6 ^ 2 = 4 (binary: 110 ^ 010 = 100)

Return 4 ✓

Why it works:
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1 ^ 1) ^ (2 ^ 2)  (by associativity)
= 4 ^ 0 ^ 0              (a ^ a = 0)
= 4                      (a ^ 0 = a)
```

**Visual explanation**:

```
nums = [2, 2, 1]

Binary representation:
  2 = 010
  2 = 010
  1 = 001

XOR all:
  010 ^ 010 ^ 001
  = 000 ^ 001  (2 ^ 2 = 0)
  = 001        (0 ^ 1 = 1)
  = 1 ✓

The duplicates cancel out, leaving the single number!
```

### Complexity

- **Time**: O(n) - single pass through array
- **Space**: O(1) - only result variable (meets constraint!)

### Advantages

- **Optimal space**: O(1) extra space
- **Single pass**: Only one iteration needed
- **Elegant**: Beautiful use of bit properties
- **Fast**: XOR is very efficient operation

### Disadvantages

- **Less intuitive**: Requires understanding XOR properties
- **Not immediately obvious**: Why does this work?

## Approach 3: Set Addition/Subtraction

Use set operations:

```python
def singleNumber(self, nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)
```

### How It Works

**Mathematical insight**:

```
Let unique_sum = sum of all unique numbers
Let total_sum = sum of all numbers

Since every number appears twice except one:
  total_sum = 2 * (num1 + num2 + ... + numk) + single_number

Rearranging:
  single_number = 2 * unique_sum - total_sum
```

**Example**: `nums = [4, 1, 2, 1, 2]`

```
unique_set = {4, 1, 2}
sum(set(nums)) = 4 + 1 + 2 = 7
sum(nums) = 4 + 1 + 2 + 1 + 2 = 10

2 * 7 - 10 = 14 - 10 = 4 ✓

Why:
  2 * unique_sum = 2 * (4 + 1 + 2) = 2(4) + 2(1) + 2(2)
                 = 8 + 2 + 4 = 14

  total_sum = 4 + 1 + 2 + 1 + 2 = 10

  Difference = 14 - 10 = 4
  (The single number appears once in total_sum but twice in 2*unique_sum)
```

### Complexity

- **Time**: O(n) - creating set, two sums
- **Space**: O(n) - set stores unique elements

### Advantages

- **One-liner**: Most concise solution
- **Mathematical elegance**: Uses clever arithmetic

### Disadvantages

- **Uses O(n) space**: Violates space constraint
- **Less intuitive**: Not obvious why it works
- **Slower in practice**: Multiple operations overhead

## Approach 4: Using Counter

From collections import:

```python
from collections import Counter

def singleNumber(self, nums: List[int]) -> int:
    counter = Counter(nums)
    for num, count in counter.items():
        if count == 1:
            return num
```

### How It Works

Counter automatically counts element occurrences.

### Complexity

- **Time**: O(n)
- **Space**: O(n)

### Advantages

- **Built-in solution**: Uses Python standard library
- **Clean syntax**: Counter handles counting

### Disadvantages

- **Same space complexity as dict**: O(n)
- **Not as elegant as XOR**: Doesn't meet O(1) space requirement

## Comparison of Approaches

| Approach               | Time | Space | Difficulty | Pros                           | Cons                      |
| ---------------------- | ---- | ----- | ---------- | ------------------------------ | ------------------------- |
| Hash Map (Implemented) | O(n) | O(n)  | Easy       | Clear, reliable                | Violates space constraint |
| XOR (Optimal)          | O(n) | O(1)  | Medium     | Meets all constraints, elegant | Less intuitive            |
| Set Math               | O(n) | O(n)  | Medium     | One-liner, clever              | Violates space constraint |
| Counter                | O(n) | O(n)  | Easy       | Pythonic                       | Violates space constraint |

**Winner**: XOR approach for meeting all constraints

## Edge Cases & Considerations

1. **Single element array**:

   - `nums = [1]` → `1`
   - No duplicates, return the element ✓

2. **Two elements (one pair, one single)**:

   - `nums = [1, 1, 2]` → `2`
   - XOR: 0 ^ 1 ^ 1 ^ 2 = 2 ✓

3. **Negative numbers**:

   - `nums = [-1, -1, -2]` → `-2`
   - XOR works with negative numbers (two's complement) ✓

4. **Zero in array**:

   - `nums = [0, 1, 0]` → `1`
   - XOR: 0 ^ 1 ^ 0 = 1 ✓

5. **Large numbers**:

   - `nums = [2147483647, 2147483646, 2147483647]` → `2147483646`
   - Works with any integer value ✓

6. **Many duplicates**:

   - `nums = [1]*1000 + [2]*1000 + [3]` → `3`
   - Still O(n) time complexity ✓

7. **All same except one**:
   - `nums = [5]*999 + [6]` → `6`
   - Handles large duplicate counts ✓

## Common Pitfalls

1. **Not understanding XOR properties**:

   ```python
   # WRONG: Think XOR is exclusive OR in logic sense
   # XOR is bitwise XOR, different operation!

   # CORRECT: Learn XOR truth table:
   # 0 ^ 0 = 0
   # 0 ^ 1 = 1
   # 1 ^ 0 = 1
   # 1 ^ 1 = 0
   ```

2. **Using set incorrectly**:

   ```python
   # WRONG: Forgetting math formula
   sum(set(nums)) - sum(nums)  # Wrong formula

   # CORRECT: 2 * unique_sum - total_sum
   2 * sum(set(nums)) - sum(nums)
   ```

3. **Not initializing result for XOR**:

   ```python
   # WRONG: No initialization
   for num in nums:
       result ^= num  # result not defined

   # CORRECT: Initialize to 0
   result = 0
   for num in nums:
       result ^= num
   ```

4. **Hash map implementation errors**:

   ```python
   # WRONG: Not counting correctly
   num_count[num] += 1  # KeyError if num not in dict

   # CORRECT: Use get with default
   num_count[num] = num_count.get(num, 0) + 1
   ```

5. **Missing return statement**:

   ```python
   # WRONG: Forgetting to return
   def singleNumber(self, nums):
       for num in set(nums):
           if nums.count(num) == 1:
               pass  # Forgot return!

   # CORRECT: Return the number
   return num
   ```

6. **Assuming sorted input**:

   ```python
   # WRONG: Assuming array is sorted
   # Problem doesn't guarantee sorted order

   # CORRECT: Don't assume any order
   ```

## Optimization Notes

The XOR solution is **optimal for this problem**:

- **Time**: O(n) - must examine every element
- **Space**: O(1) - single pass doesn't need storage
- **Performance**: XOR is very fast operation

**Interview tips**:

- Start with hash map (intuitive)
- Mention time/space complexity
- Then reveal XOR solution
- Explain XOR properties carefully
- Show why `a ^ a = 0` works

**Key insight for interviews**:

```
Why XOR eliminates duplicates:

nums = [a, b, c, a, b]

Process:
  0 ^ a ^ b ^ c ^ a ^ b

Regroup (commutative/associative):
  (a ^ a) ^ (b ^ b) ^ c

Apply a ^ a = 0:
  0 ^ 0 ^ c

Apply 0 ^ x = x:
  c

All duplicates cancel out!
```

## Performance Comparison

```
Array size: 1,000,000 elements

Hash Map approach:
  - Time: ~10 operations per element (hash, insert, iterate)
  - Space: ~1,000,000 entries (huge!)

XOR approach:
  - Time: 1 operation per element (XOR)
  - Space: 1 integer variable

Winner: XOR by huge margin!
```

## Visual Example

```
nums = [4, 1, 2, 1, 2]

XOR approach visualization:

result = 0        (binary: 0000)

result ^= 4
  0000
  0100 (4 in binary)
  ----
  0100 (4)

result ^= 1
  0100
  0001 (1 in binary)
  ----
  0101 (5)

result ^= 2
  0101
  0010 (2 in binary)
  ----
  0111 (7)

result ^= 1
  0111
  0001 (1 in binary)
  ----
  0110 (6)

result ^= 2
  0110
  0010 (2 in binary)
  ----
  0100 (4)

Return 4 ✓


Hash Map approach:

num_count = {}

Process nums:
  num_count = {4:1, 1:1, 2:1, 1:2, 2:2}
            = {4:1, 1:2, 2:2}

Find count == 1:
  4 has count 1 → return 4 ✓
```

## Test Cases

```python
# Basic cases
singleNumber([2, 2, 1])            # 1
singleNumber([4, 1, 2, 1, 2])      # 4

# Single element
singleNumber([1])                  # 1

# With zero
singleNumber([0, 1, 0])            # 1

# Negative numbers
singleNumber([-1, -1, -2])         # -2

# Two elements
singleNumber([1, 1, 2])            # 2
singleNumber([3, 3, 5])            # 5

# Larger numbers
singleNumber([100, 100, 200])      # 200

# More duplicates
singleNumber([1, 1, 2, 2, 3])      # 3
singleNumber([7, 7, 8, 8, 9])      # 9

# Mixed positive/negative
singleNumber([1, -1, 1, -1, 2])    # 2

# Large array
singleNumber([i for i in range(1000) for _ in range(2)] + [5000])  # 5000
```

## Thought Process

**Problem analysis**:

- Array with every number appearing twice except one
- Must find the single number
- O(n) time, O(1) space constraint

**Key observations**:

1. If we could use extra space, hash map is easy
2. O(1) space constraint rules out hash maps
3. Need to find pattern or mathematical property
4. Numbers appear in pairs except one

**Approach considerations**:

**Hash Map approach**:

- Count each number
- Find count = 1
- Easy but O(n) space

**XOR insight**:

- Key properties:
  - `a ^ a = 0` (same number cancels)
  - `a ^ 0 = a` (0 is identity)
  - Commutative and associative
- Apply to problem:
  - XOR all numbers together
  - Duplicate pairs cancel to 0
  - Single number remains!

**Why XOR works**:

```
All numbers ^ together
= (num1 ^ num1) ^ (num2 ^ num2) ^ ... ^ single
= 0 ^ 0 ^ ... ^ single
= single
```

**Optimal solution**:

- Time: O(n) - must examine each element
- Space: O(1) - only one variable needed
- Elegant: Beautiful use of bit properties

**Interview strategy**:

1. Start with hash map (intuitive)
2. Identify space constraint issue
3. Brainstorm: what property cancels duplicates?
4. Recognize XOR property
5. Code XOR solution
6. Explain why it works

This problem tests:

- Bit manipulation knowledge (XOR)
- Space optimization awareness
- Creative problem-solving
- Understanding of mathematical properties

## Related Problems

- [260. Single Number III](https://leetcode.com/problems/single-number-iii/)
- [137. Single Number II](https://leetcode.com/problems/single-number-ii/)
- [268. Missing Number](https://leetcode.com/problems/missing-number/)
- [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/)
- [1389. Create Target Array in Given Order](https://leetcode.com/problems/create-target-array-in-given-order/)
