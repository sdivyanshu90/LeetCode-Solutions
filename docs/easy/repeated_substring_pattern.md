# Repeated Substring Pattern

## Problem Summary

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

**LeetCode Problem**: [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

## Approach 1: String Concatenation Trick (Implemented)

### Strategy

The implemented solution uses a **clever string concatenation trick**:

1. Concatenate the string with itself: `s + s`
2. Remove the first and last character: `new_string[1:-1]`
3. Check if the original string `s` appears in this modified doubled string
4. If yes, the string has a repeating pattern

**Code**:

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    new_string = s + s
    return s in new_string[1:-1]
```

### How It Works

**Example 1**: `s = "abab"`

```
Original: "abab"
Doubled: "abab" + "abab" = "abababab"
Remove first and last: "babababa" (new_string[1:-1])

Search for "abab" in "babababa":
  "babababa"
   "abab" ✓ Found at index 1

Return True ✓
```

**Example 2**: `s = "aba"`

```
Original: "aba"
Doubled: "aba" + "aba" = "abaaba"
Remove first and last: "baab" (new_string[1:-1])

Search for "aba" in "baab":
  "baab"
   Cannot find "aba"

Return False ✓
```

**Example 3**: `s = "abcabcabcabc"`

```
Original: "abcabcabcabc" (4 repetitions of "abc")
Doubled: "abcabcabcabcabcabcabcabc"
Remove first and last: "bcabcabcabcabcabcabcab"

Search for "abcabcabcabc" in "bcabcabcabcabcabcabcab":
  Found ✓

Return True ✓
```

### Why This Works

**Mathematical insight**: If a string `s` is made of repeating pattern `p`, then:

- `s = p + p + ... + p` (k times, k ≥ 2)
- When we create `s + s`, we get `2k` copies of `p`
- Removing first and last character creates a "window" where we can still find at least one complete copy of `s` (which is `k` copies of `p`)
- If no pattern exists, removing first and last character breaks the only copy

**Visual proof for "abab"**:

```
s = "abab" = "ab" + "ab"

s + s = "abababab" = "ab" + "ab" + "ab" + "ab"

Remove first and last:
  "babababa"
   |-------|
    "abab"   ← Still found! (2 copies of "ab")

If there was no pattern, removing edges would break it.
```

### Complexity Analysis

- **Time Complexity**: O(n²)
  - Creating `s + s`: O(n)
  - String search `in` operator: O(n²) worst case (naive search)
  - Python uses optimized algorithm (Boyer-Moore-Horspool), often O(n)
- **Space Complexity**: O(n)
  - Creating new string `s + s`: O(n)
  - Slicing creates another string: O(n)

### Advantages

- **Extremely concise**: One-liner solution
- **Clever and elegant**: Beautiful mathematical property
- **Easy to implement**: No complex logic

### Disadvantages

- **Not intuitive**: Requires understanding the trick
- **Extra space**: Creates new strings
- **Hidden complexity**: String search can be O(n²)

## Approach 2: Check All Divisors

Try all possible substring lengths that divide the string length:

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    n = len(s)

    # Try all possible pattern lengths from 1 to n//2
    for length in range(1, n // 2 + 1):
        if n % length == 0:  # Length must divide n
            pattern = s[:length]
            # Check if repeating pattern matches s
            if pattern * (n // length) == s:
                return True

    return False
```

### How It Works

**Example**: `s = "abcabcabcabc"` (length 12)

```
n = 12

length=1: 12 % 1 == 0
  pattern = "a"
  "a" * 12 = "aaaaaaaaaaaa" != "abcabcabcabc"

length=2: 12 % 2 == 0
  pattern = "ab"
  "ab" * 6 = "abababababab" != "abcabcabcabc"

length=3: 12 % 3 == 0
  pattern = "abc"
  "abc" * 4 = "abcabcabcabc" == "abcabcabcabc" ✓

Return True
```

### Complexity

- **Time**: O(n²) in worst case
  - Iterate over O(n) possible lengths
  - Each comparison is O(n)
- **Space**: O(n) for creating repeated pattern string

### Advantages

- **Intuitive**: Direct approach, easy to understand
- **Explicit**: Clear what's being checked

### Disadvantages

- **Slower**: Multiple string creations and comparisons
- **More code**: Longer implementation

## Approach 3: Check Divisors Without String Multiplication

More efficient divisor checking:

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    n = len(s)

    for length in range(1, n // 2 + 1):
        if n % length == 0:
            pattern = s[:length]
            # Check character by character
            match = True
            for i in range(n):
                if s[i] != pattern[i % length]:
                    match = False
                    break
            if match:
                return True

    return False
```

### Complexity

- **Time**: O(n \* d) where d is number of divisors
  - Typically much better than O(n²)
- **Space**: O(1) excluding pattern storage

### Advantages

- **Efficient**: No string multiplication
- **Lower space**: Character comparison only

## Approach 4: KMP Algorithm

Using KMP failure function:

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    n = len(s)

    # Build KMP failure function
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Check if pattern repeats
    last = lps[-1]
    return last > 0 and n % (n - last) == 0
```

### How It Works

The KMP failure function tracks the longest proper prefix which is also a suffix. If a string is made of repeating patterns, this property reveals it.

### Complexity

- **Time**: O(n)
- **Space**: O(n) for LPS array

### Advantages

- **Optimal time**: Linear time complexity
- **Theoretical best**: Used in string matching algorithms

### Disadvantages

- **Complex**: KMP algorithm is harder to understand
- **Overkill**: For this problem, simpler solutions work fine

## Comparison of Approaches

| Approach                        | Time    | Space | Difficulty | Pros             | Cons                |
| ------------------------------- | ------- | ----- | ---------- | ---------------- | ------------------- |
| String Trick (Implemented)      | O(n²)\* | O(n)  | Easy       | Elegant, concise | Not obvious         |
| Check All Divisors              | O(n²)   | O(n)  | Easy       | Intuitive        | Multiple operations |
| Divisors Without Multiplication | O(n·d)  | O(1)  | Medium     | Efficient        | More code           |
| KMP                             | O(n)    | O(n)  | Hard       | Optimal          | Complex             |

\*Average case often O(n) with optimized string search

**Winner**: String concatenation trick for elegance and simplicity

## Edge Cases & Considerations

1. **Single character**:

   - `s = "a"` → `False`
   - Cannot be formed by repeating (needs at least 2 copies)
   - `s + s = "aa"`, `[1:-1] = ""`, `"a" not in ""` → False ✓

2. **All same characters**:

   - `s = "aaaaaa"` → `True`
   - Pattern is "a" repeated 6 times
   - Works correctly

3. **No repeating pattern**:

   - `s = "abc"` → `False`
   - Each character unique

4. **Two characters alternating**:

   - `s = "ababab"` → `True`
   - Pattern is "ab" repeated 3 times

5. **Prime length strings**:

   - `s = "abcde"` (length 5, prime)
   - Can only check length=1 (all same) or full string
   - Returns False if not all same

6. **Pattern itself is repeated**:

   - `s = "abababab"` → `True`
   - Pattern could be "ab" (4 times) or "abab" (2 times)
   - Both work, returns True

7. **Empty string**:
   - Not in problem constraints, but would return False

## Common Pitfalls

1. **Forgetting to remove first and last character**:

   ```python
   # WRONG: Will always find s in s+s
   new_string = s + s
   return s in new_string  # Always True!

   # CORRECT: Remove edges
   return s in new_string[1:-1]
   ```

2. **Only checking half the length**:

   ```python
   # INCOMPLETE: Missing iteration
   for length in range(1, n // 2):  # Missing +1

   # CORRECT: Include n//2
   for length in range(1, n // 2 + 1):
   ```

3. **Not checking if length divides n**:

   ```python
   # WRONG: Pattern length must divide string length
   for length in range(1, n // 2 + 1):
       pattern = s[:length]
       if pattern * (n // length) == s:  # Might not fully cover

   # CORRECT: Check divisibility
   if n % length == 0:
       pattern = s[:length]
   ```

4. **Off-by-one in slicing**:

   ```python
   # WRONG: [0:-1] removes last only
   return s in (s + s)[0:-1]

   # CORRECT: [1:-1] removes both
   return s in (s + s)[1:-1]
   ```

5. **Assuming minimum pattern length**:

   ```python
   # WRONG: Pattern can be single character
   for length in range(2, n // 2 + 1):

   # CORRECT: Start from 1
   for length in range(1, n // 2 + 1):
   ```

## Optimization Notes

The string concatenation trick is **elegant and practical**:

- **Simple to implement**: One-liner
- **Good enough performance**: Modern string search is optimized
- **Easy to remember**: Beautiful trick

**For interviews**:

- Start with string trick (shows cleverness)
- Explain the divisor approach (shows understanding)
- Mention KMP for optimal solution (shows knowledge)

**Performance notes**:

- String trick: Usually fast in practice due to optimized `in` operator
- Divisor checking: More predictable performance
- KMP: Best asymptotic complexity but overhead for small inputs

## Visual Example

```
String: "abab"

Method 1: String trick
  s + s = "abababab"
  Remove edges: "bababab"
                   ^^^^^
                   "abab" found!

Method 2: Check divisors
  Length 4: divisors are 1, 2, 4

  Try length=1: "a" * 4 = "aaaa" ≠ "abab"
  Try length=2: "ab" * 2 = "abab" = "abab" ✓


String: "abc" (no pattern)

Method 1: String trick
  s + s = "abcabc"
  Remove edges: "bcab"
  "abc" not in "bcab" → False

Method 2: Check divisors
  Length 3: only divisor is 1, 3

  Try length=1: "a" * 3 = "aaa" ≠ "abc"
  No valid pattern → False
```

## Test Cases

```python
# Repeating patterns
repeatedSubstringPattern("abab")           # True (pattern: "ab")
repeatedSubstringPattern("abcabcabcabc")   # True (pattern: "abc")
repeatedSubstringPattern("zzzzzz")         # True (pattern: "z")

# No pattern
repeatedSubstringPattern("aba")            # False
repeatedSubstringPattern("abc")            # False

# Single character
repeatedSubstringPattern("a")              # False

# Edge cases
repeatedSubstringPattern("aa")             # True (pattern: "a")
repeatedSubstringPattern("abcabc")         # True (pattern: "abc")
repeatedSubstringPattern("ababab")         # True (pattern: "ab" or "abab")

# Complex patterns
repeatedSubstringPattern("abacababacab")   # True (pattern: "abacab")
repeatedSubstringPattern("aabaaba")        # False

# Long strings
repeatedSubstringPattern("a" * 1000)       # True
repeatedSubstringPattern("ab" * 500)       # True
```

## Thought Process

**Problem analysis**:

- Check if string can be formed by repeating a substring
- Substring must be repeated at least twice
- Pattern length must divide total length

**Key observations**:

1. If pattern exists, it must be at most half the string length
2. Pattern length must divide string length evenly
3. Mathematical property: `s` in `(s+s)[1:-1]` reveals pattern

**Approach considerations**:

**String concatenation trick**:

- Brilliant insight: doubling and removing edges
- If pattern exists, shifted version still contains original
- Very concise implementation

**Why it works mathematically**:

```
If s = p * k (pattern p repeated k times):
  s + s = p * 2k
  Removing first and last char still leaves enough to find s
  (at least k-1 full patterns remain)

If s has no pattern:
  Removing edges destroys the only copy
```

**Direct approach**:

- Check each possible pattern length
- Verify if repeating creates original string
- More intuitive but longer code

The string trick is a beautiful example of mathematical insight leading to elegant code!

## Related Problems

- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- [686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/)
- [796. Rotate String](https://leetcode.com/problems/rotate-string/)
- [1668. Maximum Repeating Substring](https://leetcode.com/problems/maximum-repeating-substring/)
- [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
