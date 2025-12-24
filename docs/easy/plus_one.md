# Plus One

## Problem Summary

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i`-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

**LeetCode Problem**: [66. Plus One](https://leetcode.com/problems/plus-one/)

## Approach 1: Recursive (Implemented)

### Strategy

The implemented solution uses a **recursive approach**:

1. **Base case (no carry)**: If last digit is ≤ 8, increment it and return
2. **Special case**: If single digit 9, return [1, 0]
3. **Recursive case**: Set last digit to 0, recursively add one to remaining digits
4. Handles carry propagation through recursion

**Code**:

```python
def plusOne(self, digits: List[int]) -> List[int]:
    if digits[-1] <= 8:
        digits[-1] += 1
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = self.plusOne(digits[0:-1])
        return digits
```

### How It Works

**Example 1**: `digits = [1,2,3]`

```
Call plusOne([1,2,3])
  Last digit = 3 ≤ 8
  Increment: 3 + 1 = 4
  Return [1,2,4] ✓
```

**Example 2**: `digits = [1,2,9]`

```
Call plusOne([1,2,9])
  Last digit = 9 > 8
  Set last to 0: [1,2,0]
  Recurse on [1,2]:
    Call plusOne([1,2])
      Last digit = 2 ≤ 8
      Increment: 2 + 1 = 3
      Return [1,3]
  Replace first part: [1,3,0]
  Return [1,3,0] ✓
```

**Example 3**: `digits = [9,9,9]`

```
Call plusOne([9,9,9])
  Last digit = 9 > 8
  Set last to 0: [9,9,0]
  Recurse on [9,9]:
    Call plusOne([9,9])
      Last digit = 9 > 8
      Set last to 0: [9,0]
      Recurse on [9]:
        Call plusOne([9])
          Length = 1 and digit = 9
          Return [1,0]
      Replace: [1,0,0]
      Return [1,0,0]
  Replace: [1,0,0,0]
  Return [1,0,0,0] ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - In worst case (all 9's), visits each digit once
  - Each recursive call processes one digit
- **Space Complexity**: O(n)
  - Recursion call stack: O(n) in worst case
  - Array slicing creates new arrays: O(n)

### Advantages

- **Handles carry naturally** through recursion
- **Clear logic** for carry propagation

### Disadvantages

- **Higher space complexity** due to recursion and slicing
- **Less efficient** than iterative approach
- **Array slicing** creates new arrays at each level

## Approach 2: Iterative (Optimal)

Clean iterative solution with O(1) extra space:

```python
def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)

    # Start from the last digit
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # Current digit is 9, set to 0 and continue carry
        digits[i] = 0

    # If we're here, all digits were 9
    return [1] + digits
```

### How It Works

**Example 1**: `digits = [1,2,9]`

```
i = 2: digits[2] = 9
  Set to 0: [1,2,0]
  Continue (carry)

i = 1: digits[1] = 2 < 9
  Increment: [1,3,0]
  Return [1,3,0] ✓
```

**Example 2**: `digits = [9,9,9]`

```
i = 2: digits[2] = 9, set to 0 → [9,9,0]
i = 1: digits[1] = 9, set to 0 → [9,0,0]
i = 0: digits[0] = 9, set to 0 → [0,0,0]

Loop complete, all were 9
Return [1] + [0,0,0] = [1,0,0,0] ✓
```

### Complexity

- **Time**: O(n) - Single pass in worst case
- **Space**: O(1) - In-place modification (except when all 9's)

### Advantages

- **Most efficient**: O(1) extra space (usually)
- **No recursion**: No stack overhead
- **In-place**: Modifies existing array
- **Clean logic**: Easy to understand

## Approach 3: Reverse, Add, Reverse

Alternative iterative approach:

```python
def plusOne(self, digits: List[int]) -> List[int]:
    carry = 1
    result = []

    # Process from right to left
    for i in range(len(digits) - 1, -1, -1):
        total = digits[i] + carry
        result.append(total % 10)
        carry = total // 10

    # If carry remains, add it
    if carry:
        result.append(carry)

    # Reverse to get correct order
    return result[::-1]
```

### Complexity

- **Time**: O(n)
- **Space**: O(n) - New result array

### Notes

- More general (works like adding any number)
- Useful for understanding carry logic
- Less efficient due to new array creation

## Approach 4: Convert to Integer

Simple but impractical for very large numbers:

```python
def plusOne(self, digits: List[int]) -> List[int]:
    # Convert to integer
    num = int(''.join(map(str, digits)))

    # Add one
    num += 1

    # Convert back to list
    return [int(d) for d in str(num)]
```

### Complexity

- **Time**: O(n)
- **Space**: O(n)

### Problems

- **Not practical**: Fails for very large numbers exceeding int limits
- **Type conversion overhead**: Multiple conversions
- **Against problem intent**: Problem treats it as array, not integer

## Comparison of Approaches

| Approach                | Time | Space  | In-Place | Pros               | Cons                        |
| ----------------------- | ---- | ------ | -------- | ------------------ | --------------------------- |
| Recursive (Implemented) | O(n) | O(n)   | No       | Clear carry logic  | Recursion overhead, slicing |
| Iterative               | O(n) | O(1)\* | Yes      | Optimal, efficient | N/A                         |
| Reverse-Add-Reverse     | O(n) | O(n)   | No       | General pattern    | Extra array                 |
| Convert to Integer      | O(n) | O(n)   | No       | Very simple        | Fails for large numbers     |

\*O(1) except when all digits are 9, then O(n) for new array

**Winner**: Iterative approach - O(n) time, O(1) space, in-place

## Edge Cases & Considerations

1. **No carry needed**:

   - `[1,2,3]` → `[1,2,4]`
   - Last digit < 9, simple increment

2. **Single carry**:

   - `[1,2,9]` → `[1,3,0]`
   - Carry propagates one position

3. **Multiple carries**:

   - `[1,9,9]` → `[2,0,0]`
   - Carry propagates through multiple digits

4. **All nines**:

   - `[9,9,9]` → `[1,0,0,0]`
   - Carry propagates through all, creates new leading digit

5. **Single digit (0-8)**:

   - `[8]` → `[9]`
   - Simple increment

6. **Single digit (9)**:

   - `[9]` → `[1,0]`
   - Special case, array length increases

7. **Leading zeros after operation**:

   - Won't happen since we're adding 1 to valid number

8. **Very large numbers**:

   - `[9,8,7,6,5,4,3,2,1,0]` → `[9,8,7,6,5,4,3,2,1,1]`
   - Works for arbitrary length

9. **Zero**:
   - `[0]` → `[1]`
   - Simple increment

## Common Pitfalls

1. **Not handling all 9's case**:

   ```python
   # WRONG: Doesn't handle [9,9,9] → [1,0,0,0]
   for i in range(n - 1, -1, -1):
       if digits[i] < 9:
           digits[i] += 1
           return digits
       digits[i] = 0
   # Missing: return [1] + digits

   # CORRECT: Add leading 1 after loop
   return [1] + digits
   ```

2. **Modifying array during iteration without care**:

   ```python
   # RISKY: Index issues if inserting
   for i in range(len(digits)):
       # Don't insert during forward iteration

   # BETTER: Iterate backward for carry propagation
   for i in range(len(digits) - 1, -1, -1):
       # ...
   ```

3. **Creating new array unnecessarily**:

   ```python
   # INEFFICIENT: Creates new array each time
   def plusOne(self, digits):
       return [int(d) for d in str(int(''.join(map(str, digits))) + 1)]

   # BETTER: Modify in-place when possible
   ```

4. **Not returning early when no carry**:

   ```python
   # WORKS but inefficient: Always processes all digits
   carry = 1
   for i in range(n - 1, -1, -1):
       digits[i] += carry
       carry = digits[i] // 10
       digits[i] %= 10

   # BETTER: Return early when no carry
   if digits[i] < 9:
       digits[i] += 1
       return digits
   ```

5. **Off-by-one in range**:

   ```python
   # WRONG: Misses first digit
   for i in range(n - 1, 0, -1):  # Stops at 1, not 0!

   # CORRECT: Include index 0
   for i in range(n - 1, -1, -1):
   ```

## Optimization Notes

The **iterative approach** is optimal:

- **Time**: O(n) worst case - Must potentially check all digits
- **Space**: O(1) best case - In-place modification
  - O(n) only when all 9's (unavoidable, need bigger array)

**Key optimizations**:

1. **Early return**: When digit < 9, no need to continue
2. **In-place**: Modify existing array instead of creating new one
3. **Backward iteration**: Natural for carry propagation

**Why iterative beats recursive**:

- No recursion stack overhead
- No array slicing overhead
- In-place modification
- More cache-friendly

## Visual Example

```
Example: [1, 2, 9]

Iterative approach:
  i=2: digits[2] = 9
       Set to 0: [1, 2, 0]
       Continue (carry)

  i=1: digits[1] = 2 < 9
       Increment: [1, 3, 0]
       Return ✓

Result: [1, 3, 0]


Example: [9, 9, 9]

Iterative approach:
  i=2: digits[2] = 9
       Set to 0: [9, 9, 0]
       Continue

  i=1: digits[1] = 9
       Set to 0: [9, 0, 0]
       Continue

  i=0: digits[0] = 9
       Set to 0: [0, 0, 0]
       Continue

  Loop done, all were 9
  Return [1] + [0, 0, 0] = [1, 0, 0, 0] ✓


Example: [1, 2, 3]

Iterative approach:
  i=2: digits[2] = 3 < 9
       Increment: [1, 2, 4]
       Return ✓

Result: [1, 2, 4]
```

## Test Cases

```python
# No carry
plusOne([1,2,3])                    # [1,2,4]
plusOne([4,3,2,1])                  # [4,3,2,2]

# Single carry
plusOne([1,2,9])                    # [1,3,0]
plusOne([2,9,9])                    # [3,0,0]

# All nines
plusOne([9])                        # [1,0]
plusOne([9,9,9])                    # [1,0,0,0]

# Single digit
plusOne([0])                        # [1]
plusOne([5])                        # [6]
plusOne([8])                        # [9]

# Multiple carries
plusOne([1,9,9])                    # [2,0,0]
plusOne([1,9,9,9])                  # [2,0,0,0]

# Large number
plusOne([9,8,7,6,5,4,3,2,1,0])      # [9,8,7,6,5,4,3,2,1,1]

# Edge case
plusOne([1,2,8])                    # [1,2,9]
```

## Thought Process

**Problem analysis**:

- Array represents a large integer
- Need to add 1 to this integer
- Return result as array

**Key observations**:

1. Only need to handle carry when digit is 9
2. Carry propagates from right to left
3. Only case where array size increases: all digits are 9
4. Can solve in-place by iterating backward

**Approach considerations**:

**Why not convert to integer?**

- Problem implies very large numbers (beyond int limits)
- Defeats the purpose of array representation
- Multiple type conversions are inefficient

**Recursive vs Iterative?**

- Both work, but iterative is more efficient
- Recursive has O(n) stack space overhead
- Recursive creates new arrays through slicing
- Iterative can modify in-place

**Optimal solution**:

- Iterate from right to left (carry direction)
- If digit < 9: increment and return (no carry)
- If digit = 9: set to 0 and continue (carry forward)
- If all 9's: prepend 1 after loop

This leads to an O(n) time, O(1) space solution!

## Related Problems

- [67. Add Binary](https://leetcode.com/problems/add-binary/)
- [415. Add Strings](https://leetcode.com/problems/add-strings/)
- [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/)
- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
