# Palindrome Number

## Problem Summary

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number that reads the same backward as forward. For example, `121` is a palindrome while `123` is not.

**LeetCode Problem**: [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

**Follow-up**: Could you solve it without converting the integer to a string?

## Approach 1: String Conversion (Implemented)

### Strategy

The implemented solution uses **string conversion and reversal**:

1. Convert the integer to a string
2. Reverse the string using Python slicing `[::-1]`
3. Compare the original string with the reversed string
4. Return `True` if they're equal, `False` otherwise

**Code**:

```python
def isPalindrome(self, x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
```

**Simplified version**:

```python
def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]
```

### How It Works

**Example 1**: `x = 121`

```
Convert to string: "121"
Reverse string: "121"[::-1] = "121"
Compare: "121" == "121"? Yes
Return True ✓
```

**Example 2**: `x = -121`

```
Convert to string: "-121"
Reverse string: "-121"[::-1] = "121-"
Compare: "-121" == "121-"? No
Return False ✓
```

**Example 3**: `x = 10`

```
Convert to string: "10"
Reverse string: "10"[::-1] = "01"
Compare: "10" == "01"? No
Return False ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Converting to string: O(n) where n = number of digits
  - Reversing string: O(n)
  - Comparing strings: O(n)
  - Total: O(n)
- **Space Complexity**: O(n)
  - String representation: O(n)
  - Reversed string: O(n)

### Advantages

- **Simple and clean**: One-liner solution
- **Readable**: Intent is immediately clear
- **Handles all edge cases** automatically (negative numbers, trailing zeros)

### Disadvantages

- **Uses extra space**: O(n) for string storage
- **Converts between types**: Not solving it "mathematically"
- **Slower in practice**: String operations have overhead

## Approach 2: Mathematical Reversal (Optimal)

Reverse the number mathematically without string conversion:

```python
def isPalindrome(self, x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Numbers ending in 0 (except 0 itself) are not palindromes
    if x != 0 and x % 10 == 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num
```

### How It Works

**Example**: `x = 121`

```
original = 121
reversed_num = 0

Iteration 1:
  digit = 121 % 10 = 1
  reversed_num = 0 * 10 + 1 = 1
  x = 121 // 10 = 12

Iteration 2:
  digit = 12 % 10 = 2
  reversed_num = 1 * 10 + 2 = 12
  x = 12 // 10 = 1

Iteration 3:
  digit = 1 % 10 = 1
  reversed_num = 12 * 10 + 1 = 121
  x = 1 // 10 = 0

Compare: 121 == 121? Yes
Return True ✓
```

### Complexity

- **Time**: O(n) where n = number of digits
- **Space**: O(1) - Only using variables

### Advantages

- **O(1) space** - No extra storage needed
- **Mathematical approach** - Solves without type conversion
- **Satisfies follow-up** requirement

## Approach 3: Half Reversal (Most Efficient)

Only reverse half the number:

```python
def isPalindrome(self, x: int) -> bool:
    # Negative numbers and numbers ending in 0 (except 0) are not palindromes
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    reversed_half = 0

    # Reverse half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For even length: x == reversed_half
    # For odd length: x == reversed_half // 10 (ignore middle digit)
    return x == reversed_half or x == reversed_half // 10
```

### How It Works

**Example 1**: `x = 1221` (even length)

```
x = 1221, reversed_half = 0

Iteration 1:
  reversed_half = 0 * 10 + 1 = 1
  x = 122
  122 > 1? Yes, continue

Iteration 2:
  reversed_half = 1 * 10 + 2 = 12
  x = 12
  12 > 12? No, stop

Check: 12 == 12? Yes
Return True ✓
```

**Example 2**: `x = 12321` (odd length)

```
x = 12321, reversed_half = 0

Iteration 1:
  reversed_half = 0 * 10 + 1 = 1
  x = 1232
  1232 > 1? Yes

Iteration 2:
  reversed_half = 1 * 10 + 2 = 12
  x = 123
  123 > 12? Yes

Iteration 3:
  reversed_half = 12 * 10 + 3 = 123
  x = 12
  12 > 123? No, stop

Check: 12 == 123? No
Check: 12 == 123 // 10? → 12 == 12? Yes
Return True ✓
```

### Why This Works

For a palindrome:

- **Even length** (1221): First half equals reversed second half
- **Odd length** (12321): First half equals reversed second half (ignoring middle digit)

By only reversing half, we can compare in the middle!

### Complexity

- **Time**: O(n/2) = O(n) - Only process half the digits
- **Space**: O(1)

### Advantages

- **Most efficient**: Half the iterations
- **O(1) space**
- **Elegant approach**

## Approach 4: Two-Pointer String Comparison

Use two pointers on string without creating reversed copy:

```python
def isPalindrome(self, x: int) -> bool:
    s = str(x)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

### Complexity

- **Time**: O(n)
- **Space**: O(n) for string conversion

### Advantages

- **Better than full reversal**: No need to create reversed string
- **Early exit**: Returns False as soon as mismatch found

## Comparison of Approaches

| Approach                        | Time | Space | Pros                    | Cons                         |
| ------------------------------- | ---- | ----- | ----------------------- | ---------------------------- |
| String Conversion (Implemented) | O(n) | O(n)  | Simple, one-liner       | Extra space, type conversion |
| Mathematical Reversal           | O(n) | O(1)  | No string conversion    | Full reversal needed         |
| Half Reversal                   | O(n) | O(1)  | Most efficient, optimal | Slightly complex logic       |
| Two-Pointer String              | O(n) | O(n)  | Early exit possible     | Still uses strings           |

**Winner**: Half Reversal - O(n) time, O(1) space, most efficient

## Edge Cases & Considerations

1. **Negative numbers**:

   - `x = -121` → `False`
   - Negative sign makes it non-palindrome (reversed would be "121-")

2. **Single digit**:

   - `x = 7` → `True`
   - All single digits are palindromes

3. **Zero**:

   - `x = 0` → `True`
   - Zero is a palindrome

4. **Numbers with trailing zeros**:

   - `x = 10` → `False`
   - Reversed would be "01" which isn't equal to "10"
   - Can't have leading zeros, so not a palindrome

5. **Even-length palindromes**:

   - `x = 1221` → `True`
   - `x = 8008` → `True`

6. **Odd-length palindromes**:

   - `x = 121` → `True`
   - `x = 12321` → `True`

7. **All same digits**:

   - `x = 555` → `True`
   - `x = 11` → `True`

8. **Very large numbers**:

   - `x = 1234567890987654321` → `True`
   - Works with Python's arbitrary precision

9. **Numbers near palindromes**:
   - `x = 1231` → `False`
   - `x = 1233` → `False`

## Common Pitfalls

1. **Not handling negative numbers**:

   ```python
   # WRONG: Doesn't check for negative
   def isPalindrome(self, x):
       return str(x) == str(x)[::-1]

   # Works but inefficient for mathematical approach
   # BETTER: Add explicit check for clarity in math approach
   if x < 0:
       return False
   ```

2. **Not handling trailing zeros**:

   ```python
   # Mathematical approach needs special handling
   # WRONG: Doesn't reject 10, 100, etc.

   # CORRECT: Check for trailing zero
   if x != 0 and x % 10 == 0:
       return False
   ```

3. **Integer overflow** (in other languages):

   ```
   // C++: Reversed number might overflow
   int reversed = 0;
   while (x > 0) {
       reversed = reversed * 10 + x % 10;  // Can overflow!
   }
   ```

   Python doesn't have this issue due to arbitrary precision.

4. **Comparing with != instead of ==**:

   ```python
   # WRONG: Logic inverted
   return str(x) != str(x)[::-1]

   # CORRECT: Check equality
   return str(x) == str(x)[::-1]
   ```

5. **Forgetting middle digit in odd-length half reversal**:

   ```python
   # WRONG: Only checks equal halves
   return x == reversed_half

   # CORRECT: Check both even and odd cases
   return x == reversed_half or x == reversed_half // 10
   ```

## Optimization Notes

The **half reversal approach** is the most optimal:

- **Time**: O(n) - Can't do better, must check all digits
- **Space**: O(1) - Optimal space usage
- **Practical**: Fewer iterations than full reversal

**String approach** (implemented):

- **Pros**: Extremely simple, readable
- **Cons**: O(n) extra space
- **Good for**: Quick prototyping, interviews where simplicity matters

**When to use each**:

- **String approach**: When code clarity is paramount
- **Half reversal**: When optimizing for space and time
- **Full reversal**: Middle ground between simplicity and efficiency

## Visual Example

```
Example: x = 12321

String approach:
  "12321" reversed = "12321"
  Equal? Yes → True

Half reversal approach:
  Original: 12321

  Step 1: 12321 → x=1232, reversed=1
  Step 2: 1232 → x=123, reversed=12
  Step 3: 123 → x=12, reversed=123

  Stop when x <= reversed
  x=12, reversed=123

  Check: 12 == 123 // 10? → 12 == 12? Yes → True


Example: x = 10

String approach:
  "10" reversed = "01"
  Equal? No → False

Mathematical approach:
  Check: 10 != 0 and 10 % 10 == 0? Yes
  Return False immediately (trailing zero check)
```

## Test Cases

```python
# Palindromes
isPalindrome(121)                    # True
isPalindrome(1221)                   # True
isPalindrome(12321)                  # True
isPalindrome(7)                      # True (single digit)
isPalindrome(0)                      # True
isPalindrome(555)                    # True (all same)
isPalindrome(1234567890987654321)    # True (large)

# Not palindromes
isPalindrome(-121)                   # False (negative)
isPalindrome(10)                     # False (trailing zero)
isPalindrome(1234567)                # False
isPalindrome(1231)                   # False (close but not)

# Edge cases
isPalindrome(1)                      # True
isPalindrome(11)                     # True
isPalindrome(100)                    # False
isPalindrome(1001)                   # True
isPalindrome(-12321)                 # False (negative)
```

## Thought Process

**Problem analysis**:

- Check if number reads same forward and backward
- Must handle negative numbers and trailing zeros

**Key observations**:

1. Negative numbers can't be palindromes (minus sign)
2. Numbers ending in 0 (except 0) can't be palindromes (no leading zeros)
3. Can solve with strings OR mathematically

**Approach considerations**:

**String approach** (implemented):

- **Pros**: One line, very simple, clear intent
- **Cons**: Uses O(n) extra space
- **Decision**: Great for readability, acceptable for interviews

**Mathematical full reversal**:

- **Pros**: O(1) space, no type conversion
- **Cons**: More code, must handle edge cases manually
- **Decision**: Better for follow-up requirement

**Half reversal**:

- **Pros**: Optimal (O(1) space, fewer iterations)
- **Cons**: Slightly tricky logic (even vs odd length)
- **Decision**: Best solution for optimization

**String two-pointer**:

- **Pros**: No reversed string creation
- **Cons**: Still O(n) space for original string
- **Decision**: Middle ground, not optimal

For most practical purposes, the **string approach** is perfectly fine due to its simplicity. For optimization-focused scenarios, use **half reversal**.

## Related Problems

- [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- [2217. Find Palindrome With Fixed Length](https://leetcode.com/problems/find-palindrome-with-fixed-length/)
