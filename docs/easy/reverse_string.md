# Reverse String

## Problem Summary

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

**LeetCode Problem**: [344. Reverse String](https://leetcode.com/problems/reverse-string/)

## Approach 1: Built-in Reverse Method (Implemented)

### Strategy

The implemented solution uses **Python's built-in `reverse()` method**:

1. Call `s.reverse()` on the list
2. This reverses the list in-place
3. No return value (modifies list directly)

**Code**:

```python
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
```

### How It Works

The `list.reverse()` method is implemented in C and uses a simple swap algorithm:

- Swaps elements from both ends moving toward center
- Continues until middle is reached

**Example**: `s = ["h","e","l","l","o"]`

```
Internal process (what reverse() does):
  Initial: ["h","e","l","l","o"]
           ↓             ↓
  Swap indices 0 and 4: ["o","e","l","l","h"]
                 ↓     ↓
  Swap indices 1 and 3: ["o","l","l","e","h"]
           Middle: "l" stays (index 2)

  Result: ["o","l","l","e","h"]
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Must swap n/2 pairs = O(n)
  - n = length of string
- **Space Complexity**: O(1)
  - In-place reversal
  - No additional data structures

### Advantages

- **Most concise**: Single line solution
- **Built-in optimization**: C implementation is fast
- **Pythonic**: Uses standard library
- **Clean and readable**: Clear intent

### Disadvantages

- **Python-specific**: Not available in all languages
- **Less educational**: Hides the algorithm
- **No control**: Can't customize swap logic

## Approach 2: Two-Pointer Swap

Manual two-pointer approach:

```python
def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap elements
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### How It Works

**Example**: `s = ["h","e","l","l","o"]`

```
Initial state:
  ["h", "e", "l", "l", "o"]
    ↑                   ↑
   left=0            right=4

Iteration 1:
  Swap s[0] and s[4]: ["o", "e", "l", "l", "h"]
  left = 1, right = 3

  ["o", "e", "l", "l", "h"]
         ↑       ↑
       left=1  right=3

Iteration 2:
  Swap s[1] and s[3]: ["o", "l", "l", "e", "h"]
  left = 2, right = 2

  ["o", "l", "l", "e", "h"]
              ↑
        left=2, right=2

left >= right, stop
Result: ["o", "l", "l", "e", "h"]
```

### Step-by-Step Process

```
s = ["a", "b", "c", "d", "e"]

Step 1: left=0, right=4
  ["a", "b", "c", "d", "e"]
    ↑                   ↑
  Swap: ["e", "b", "c", "d", "a"]
  left++, right--

Step 2: left=1, right=3
  ["e", "b", "c", "d", "a"]
         ↑       ↑
  Swap: ["e", "d", "c", "b", "a"]
  left++, right--

Step 3: left=2, right=2
  ["e", "d", "c", "b", "a"]
              ↑
  left >= right, stop

Final: ["e", "d", "c", "b", "a"]
```

### Complexity

- **Time**: O(n) - swap n/2 pairs
- **Space**: O(1) - only two pointers

### Advantages

- **Universal**: Works in any programming language
- **Educational**: Shows the algorithm explicitly
- **Clear logic**: Easy to understand and debug
- **Control**: Can modify swap behavior

### Disadvantages

- **More code**: Requires explicit loop
- **Manual**: More prone to off-by-one errors

## Approach 3: Two-Pointer with XOR Swap

Swap without temporary variable using XOR:

```python
def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        # XOR swap (only works with same type)
        s[left] = chr(ord(s[left]) ^ ord(s[right]))
        s[right] = chr(ord(s[left]) ^ ord(s[right]))
        s[left] = chr(ord(s[left]) ^ ord(s[right]))
        left += 1
        right -= 1
```

### How XOR Swap Works

**Mathematical property**: `a ^ b ^ b = a`

```
Example: Swap 'a' (97) and 'z' (122)

Step 1: a = a ^ z
  a = 97 ^ 122 = 27

Step 2: z = a ^ z
  z = 27 ^ 122 = 97  (now z holds original a)

Step 3: a = a ^ z
  a = 27 ^ 97 = 122  (now a holds original z)

Result: a='z', z='a'
```

### Complexity

- **Time**: O(n) - same swap count
- **Space**: O(1) - no temp variable

### Advantages

- **No temp variable**: Swaps in-place using XOR
- **Clever trick**: Shows bit manipulation knowledge

### Disadvantages

- **Confusing**: Hard to understand
- **Not practical**: Python tuple swap is clearer
- **Character conversion overhead**: ord/chr calls
- **Overkill**: No real benefit over simple swap

## Approach 4: Recursion

Recursive solution:

```python
def reverseString(self, s: List[str]) -> None:
    def reverse(left, right):
        if left >= right:
            return

        # Swap
        s[left], s[right] = s[right], s[left]

        # Recurse with next pair
        reverse(left + 1, right - 1)

    reverse(0, len(s) - 1)
```

### How It Works

**Example**: `s = ["a", "b", "c"]`

```
Call stack:
  reverse(0, 2):
    Swap s[0] and s[2]: ["c", "b", "a"]
    Call reverse(1, 1)

      reverse(1, 1):
        left >= right, return

Result: ["c", "b", "a"]
```

### Complexity

- **Time**: O(n) - n/2 recursive calls
- **Space**: O(n) - recursion call stack

### Advantages

- **Elegant**: Clean recursive structure
- **Educational**: Good for learning recursion

### Disadvantages

- **Not O(1) space**: Uses call stack
- **Violates constraint**: Problem requires O(1) space
- **Stack overflow risk**: Deep recursion for large strings
- **Unnecessary**: Iterative is better

## Approach 5: Slicing (Creates New List)

Using Python slicing:

```python
def reverseString(self, s: List[str]) -> None:
    s[:] = s[::-1]
```

### How It Works

- `s[::-1]` creates reversed copy
- `s[:] = ...` replaces contents in-place

### Complexity

- **Time**: O(n) - creates reversed copy
- **Space**: O(n) - temporary reversed list

### Advantages

- **Most concise**: One-liner
- **Pythonic**: Uses slicing syntax

### Disadvantages

- **Not O(1) space**: Creates temporary list
- **Violates constraint**: Problem requires O(1) space
- **Less efficient**: Extra memory allocation

## Comparison of Approaches

| Approach           | Time | Space | Constraint | Difficulty | Pros             | Cons                |
| ------------------ | ---- | ----- | ---------- | ---------- | ---------------- | ------------------- |
| Built-in reverse() | O(n) | O(1)  | ✓          | Easy       | Concise, fast    | Language-specific   |
| Two-Pointer Swap   | O(n) | O(1)  | ✓          | Easy       | Universal, clear | More code           |
| XOR Swap           | O(n) | O(1)  | ✓          | Medium     | No temp          | Confusing, slow     |
| Recursion          | O(n) | O(n)  | ✗          | Medium     | Elegant          | Violates constraint |
| Slicing            | O(n) | O(n)  | ✗          | Easy       | Pythonic         | Violates constraint |

**Winner**: Built-in `reverse()` for simplicity, two-pointer for universality

## Edge Cases & Considerations

1. **Empty list**:

   - `s = []` → `[]`
   - No operations performed ✓

2. **Single character**:

   - `s = ["a"]` → `["a"]`
   - No swap needed ✓

3. **Two characters**:

   - `s = ["a", "b"]` → `["b", "a"]`
   - Single swap ✓

4. **Palindrome**:

   - `s = ["r","a","c","e","c","a","r"]` → Same structure
   - Still performs swaps but result looks identical

5. **Even vs odd length**:

   - Even: All characters swap
   - Odd: Middle character stays in place

6. **Special characters**:

   - `s = ["!","@","#"]` → `["#","@","!"]`
   - Works with any characters ✓

7. **Unicode characters**:

   - Works with any string characters
   - Python handles Unicode properly

8. **Very long string**:
   - Still O(n) time, O(1) space
   - No performance issues

## Common Pitfalls

1. **Creating new list instead of in-place**:

   ```python
   # WRONG: Returns new list
   def reverseString(self, s):
       return s[::-1]

   # CORRECT: Modifies in-place
   def reverseString(self, s):
       s[:] = s[::-1]  # or s.reverse()
   ```

2. **Using extra space**:

   ```python
   # WRONG: Violates O(1) space constraint
   def reverseString(self, s):
       temp = s[::-1]
       s[:] = temp

   # CORRECT: Direct in-place
   def reverseString(self, s):
       s.reverse()
   ```

3. **Off-by-one errors in two-pointer**:

   ```python
   # WRONG: Will miss elements or go out of bounds
   while left <= right:  # Should be <

   # CORRECT: Stop when pointers meet
   while left < right:
   ```

4. **Not moving both pointers**:

   ```python
   # WRONG: Infinite loop or incorrect result
   while left < right:
       s[left], s[right] = s[right], s[left]
       left += 1  # Forgot right -= 1

   # CORRECT: Move both pointers
   while left < right:
       s[left], s[right] = s[right], s[left]
       left += 1
       right -= 1
   ```

5. **Swapping incorrectly**:

   ```python
   # WRONG: Loses data
   s[left] = s[right]
   s[right] = s[left]  # Both now have s[right]'s value

   # CORRECT: Use simultaneous assignment
   s[left], s[right] = s[right], s[left]
   ```

6. **Returning value**:

   ```python
   # WRONG: Problem says "Do not return anything"
   def reverseString(self, s):
       s.reverse()
       return s

   # CORRECT: Return None (implicit)
   def reverseString(self, s):
       s.reverse()
   ```

## Optimization Notes

The implemented solution (`s.reverse()`) is **already optimal**:

- **Time**: O(n) - cannot be faster (must touch each element)
- **Space**: O(1) - meets constraint perfectly
- **Implementation**: C-optimized, very fast

**For interviews**:

- **Python interviews**: Use `s.reverse()` (Pythonic)
- **General interviews**: Use two-pointer (shows algorithm knowledge)
- **Follow-up**: Mention recursion (but note space issue)

**Performance comparison**:

- `s.reverse()`: Fastest (C implementation)
- Two-pointer: Very close, minimal overhead
- XOR swap: Slower (ord/chr conversions)
- Recursion: Call stack overhead
- Slicing: Extra memory allocation

**When to use each**:

- Production code: `s.reverse()`
- Learning: Two-pointer
- Bit manipulation practice: XOR (not recommended)
- Recursion study: Recursive (but violates constraint)

## Visual Example

```
Original: ["h", "e", "l", "l", "o"]

Two-pointer swap visualization:

Step 0:
  ["h", "e", "l", "l", "o"]
    ↑                   ↑
  left=0            right=4

Step 1: Swap indices 0 and 4
  ["o", "e", "l", "l", "h"]
         ↑       ↑
      left=1  right=3

Step 2: Swap indices 1 and 3
  ["o", "l", "l", "e", "h"]
              ↑
        left=2, right=2

Step 3: left >= right, done
  Result: ["o", "l", "l", "e", "h"]


Even length example: ["a", "b", "c", "d"]

Step 1: ["d", "b", "c", "a"]  (swap 0,3)
Step 2: ["d", "c", "b", "a"]  (swap 1,2)
Done


Odd length example: ["a", "b", "c"]

Step 1: ["c", "b", "a"]  (swap 0,2)
Middle "b" stays at index 1
```

## Test Cases

```python
# Standard string
reverseString(["h","e","l","l","o"])         # ["o","l","l","e","h"]

# Single character
reverseString(["a"])                         # ["a"]

# Empty string
reverseString([])                            # []

# Palindrome
reverseString(["r","a","c","e","c","a","r"]) # ["r","a","c","e","c","a","r"]

# With spaces
reverseString([" ","h","e","l","l","o"," "]) # [" ","o","l","l","e","h"," "]

# Long string
reverseString(list("abcdefghijklmnopqrstuvwxyz"))  # list("zyxwvutsrqponmlkjihgfedcba")

# Special characters
reverseString(["!","@","#","$","%"])         # ["%","$","#","@","!"]

# Numbers as strings
reverseString(["1","2","3","4","5"])         # ["5","4","3","2","1"]

# Mixed characters
reverseString(["a","1","!","b","2","@"])     # ["@","2","b","!","1","a"]

# All same characters
reverseString(["a","a","a","a","a"])         # ["a","a","a","a","a"]
```

## Thought Process

**Problem analysis**:

- Reverse array of characters in-place
- Must use O(1) extra space
- Modify input directly, no return value

**Key observations**:

1. In-place means swap elements, don't create new array
2. O(1) space rules out recursion and creating copies
3. Symmetric operation: swap from both ends toward center

**Approach considerations**:

**Built-in method**:

- Python provides `list.reverse()`
- Meets all constraints (O(n) time, O(1) space)
- Simplest and most Pythonic
- Implemented in C, very fast

**Two-pointer approach**:

- Classic algorithm: left and right pointers
- Swap elements and move toward center
- Works in any programming language
- Educational and clear

**Why two-pointer works**:

```
For any array of length n:
- Swap element at index i with element at index n-1-i
- Repeat for i from 0 to n/2
- Middle element (if odd length) doesn't move

This naturally reverses the array!
```

**Space constraint eliminates**:

- Recursion (call stack is O(n))
- Creating new arrays (O(n) space)
- Storing elements in auxiliary structures

**Optimal solution**:

- Time: O(n) - must touch each element at least once
- Space: O(1) - only need swap variables (or none with tuple assignment)
- Both `reverse()` and two-pointer achieve this

**Interview strategy**:

1. Mention the constraint (O(1) space)
2. Explain two-pointer approach
3. Code it clearly
4. Mention `reverse()` exists in Python
5. Discuss trade-offs

This is a fundamental algorithm demonstrating:

- In-place array manipulation
- Two-pointer technique
- Space complexity constraints
- Pythonic vs universal solutions

## Related Problems

- [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)
- [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- [186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
- [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)
