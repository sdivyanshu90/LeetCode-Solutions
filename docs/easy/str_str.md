# Implement strStr()

## Problem Summary

Implement the `strStr()` function. Given two strings `haystack` and `needle`, return the **index of the first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Clarification**: What should we return when `needle` is an empty string? This is a good question to ask during an interview.

For the purpose of this problem, we will return `0` when `needle` is an empty string.

**LeetCode Problem**: [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Approach 1: Built-in String Methods (Implemented)

### Strategy

The implemented solution uses **Python's built-in `in` operator and `index()` method**:

1. Check if `needle` exists in `haystack` using the `in` operator
2. If found, return the index using `index()` method
3. If not found, return `-1`

**Code**:

```python
def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
```

### How It Works

**Key point**: Python strings support fast substring search through optimized algorithms.

**Example 1**: `haystack = "hello"`, `needle = "ll"`

```
Check if "ll" in "hello":
  h e l l o
      ^ ^
  "ll" found at index 2

Return 2 ✓
```

**Example 2**: `haystack = "aaaaa"`, `needle = "bba"`

```
Check if "bba" in "aaaaa":
  a a a a a
  (no match found)

Return -1 ✓
```

**Example 3**: `haystack = "abc"`, `needle = ""`

```
Empty string is technically in every string:
  "" in "abc" → True

haystack.index("") → 0

Return 0 ✓
```

**Example 4**: `haystack = "ababcabc"`, `needle = "abc"`

```
Check if "abc" in "ababcabc":
  a b a b c a b c
  . . . . ^ ^ ^

First occurrence at index 4? No, let me check again:
  a b a b c a b c
  0 1 2 3 4 5 6 7
  . . ^ ^ ^

First occurrence at index 2 ✓

Return 2 ✓
```

### Complexity Analysis

- **Time Complexity**: O(n \* m)
  - In worst case, `in` operator checks substring at each position
  - n = length of haystack
  - m = length of needle
  - Modern Python uses optimized algorithm (Boyer-Moore-Horspool), often O(n)
- **Space Complexity**: O(1)
  - No additional data structures
  - Only using pointers for comparison

### Advantages

- **Most concise**: One-liner solution
- **Pythonic**: Uses standard library
- **Reliable**: Handles all edge cases
- **Fast in practice**: Uses optimized C implementation

### Disadvantages

- **Language-specific**: Not available in all languages (in same form)
- **Hidden complexity**: Actual algorithm hidden from view
- **Less educational**: Doesn't show the underlying algorithm

## Approach 2: Manual Sliding Window

Implement the search manually using a sliding window:

```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0

    h_len = len(haystack)
    n_len = len(needle)

    # If needle is longer than haystack
    if n_len > h_len:
        return -1

    # Sliding window approach
    for i in range(h_len - n_len + 1):
        # Check if substring matches
        if haystack[i:i + n_len] == needle:
            return i

    return -1
```

### How It Works

Compare each possible substring of length `m` with the needle.

**Example**: `haystack = "ababcabc"`, `needle = "abc"`

```
Needle length: 3
Check windows of size 3:

Window 1 (index 0):
  haystack[0:3] = "aba"
  "aba" == "abc"? No

Window 2 (index 1):
  haystack[1:4] = "bab"
  "bab" == "abc"? No

Window 3 (index 2):
  haystack[2:5] = "abc"
  "abc" == "abc"? Yes → Return 2 ✓
```

**Visual sliding window**:

```
haystack = "ababcabc"
needle = "abc"

Position 0:
  "aba" != "abc"

Position 1:
  "bab" != "abc"

Position 2:
  "abc" == "abc" ✓ MATCH!
  Return 2
```

### Complexity

- **Time**: O((n - m + 1) _ m) = O(n _ m)
  - Iterate n - m + 1 positions
  - Each comparison takes O(m)
  - Worst case: O(n \* m)
- **Space**: O(1) - only pointers

### Advantages

- **Universal**: Works in any language
- **Educational**: Shows the algorithm explicitly
- **Understandable**: Clear logic, easy to debug
- **Predictable**: Consistent performance

### Disadvantages

- **Slower**: No optimizations
- **More code**: Requires explicit implementation

## Approach 3: KMP Algorithm (Optimal)

Use Knuth-Morris-Pratt algorithm:

```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0

    # Build failure function
    def build_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    # KMP search
    n = len(haystack)
    m = len(needle)
    lps = build_lps(needle)

    i = 0  # Index for haystack
    j = 0  # Index for needle

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == m:
            return i - j  # Match found
        elif i < n and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1
```

### How It Works

**KMP insight**: Use a failure function to skip comparisons when mismatch occurs.

**Example**: `haystack = "ABABDABACDABABCABAB"`, `needle = "ABABCABAB"`

```
Build LPS array for "ABABCABAB":
  A B A B C A B A B
  0 0 1 2 0 1 2 3 4

Search:
  i=0: H[0]='A' == N[0]='A' → i++, j++
  i=1: H[1]='B' == N[1]='B' → i++, j++
  i=2: H[2]='A' == N[2]='A' → i++, j++
  i=3: H[3]='B' == N[3]='B' → i++, j++
  i=4: H[4]='D' != N[4]='C' → Use LPS to skip
    j = lps[3] = 2
  i=4: H[4]='D' != N[2]='A' → Use LPS
    j = lps[1] = 0
  i=4: H[4]='D' != N[0]='A' → i++
  ... (continues with skip optimization)
```

### Complexity

- **Time**: O(n + m)
  - Build LPS: O(m)
  - Search: O(n)
  - Total: O(n + m) - optimal!
- **Space**: O(m) for LPS array

### Advantages

- **Optimal time**: O(n + m) is theoretically best
- **No backtracking**: Never re-examines haystack characters
- **Efficient**: Perfect for large texts

### Disadvantages

- **Complex**: Hard to understand and implement
- **More space**: Requires LPS array
- **Overkill for small strings**: Overhead not worth it

## Approach 4: Z-Algorithm

Use Z-algorithm for pattern matching:

```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0

    # Create concatenated string: pattern$text
    combined = needle + "$" + haystack
    n = len(combined)

    # Build Z-array
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and combined[r - l] == combined[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and combined[r - l] == combined[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    # Find pattern match
    for i in range(len(needle) + 1, n):
        if z[i] == len(needle):
            return i - len(needle) - 1

    return -1
```

### Complexity

- **Time**: O(n + m) - same as KMP
- **Space**: O(n + m) - Z-array is larger

### Advantages

- **Optimal time**: O(n + m)
- **Alternative to KMP**: Different approach to same problem

### Disadvantages

- **Complex**: Even harder than KMP
- **More space**: Concatenation creates longer string
- **Not practical**: KMP usually preferred

## Comparison of Approaches

| Approach                       | Time                    | Space  | Difficulty | Pros             | Cons              |
| ------------------------------ | ----------------------- | ------ | ---------- | ---------------- | ----------------- |
| Built-in Methods (Implemented) | O(n) avg, O(n\*m) worst | O(1)   | Easy       | Concise, fast    | Language-specific |
| Sliding Window                 | O(n\*m)                 | O(1)   | Easy       | Universal, clear | Slower            |
| KMP                            | O(n+m)                  | O(m)   | Hard       | Optimal          | Complex           |
| Z-Algorithm                    | O(n+m)                  | O(n+m) | Hard       | Optimal          | Very complex      |

**Winner**: Built-in methods for practicality, KMP for interview depth

## Edge Cases & Considerations

1. **Empty needle**:

   - `haystack = "abc"`, `needle = ""` → `0`
   - Empty string found at position 0 ✓

2. **Empty haystack**:

   - `haystack = ""`, `needle = "a"` → `-1`
   - Cannot find non-empty pattern in empty text ✓

3. **Both empty**:

   - `haystack = ""`, `needle = ""` → `0`
   - Empty in empty is at position 0 ✓

4. **Needle longer than haystack**:

   - `haystack = "short"`, `needle = "longerneedle"` → `-1`
   - Impossible to find ✓

5. **Exact match**:

   - `haystack = "test"`, `needle = "test"` → `0`
   - Match at beginning ✓

6. **At beginning**:

   - `haystack = "abcdef"`, `needle = "abc"` → `0`
   - Match at start ✓

7. **At end**:

   - `haystack = "abcdef"`, `needle = "def"` → `3`
   - Match at end ✓

8. **In middle**:

   - `haystack = "hello"`, `needle = "ll"` → `2`
   - Match in middle ✓

9. **Multiple occurrences**:

   - `haystack = "ababab"`, `needle = "ab"` → `0`
   - Returns first occurrence ✓

10. **Case sensitivity**:

    - `haystack = "Hello"`, `needle = "hello"` → `-1`
    - Case matters! ✓

11. **Special characters**:

    - `haystack = "a!b@c#"`, `needle = "@c"` → `3`
    - Works with any characters ✓

12. **Spaces in string**:
    - `haystack = "hello world"`, `needle = "o w"` → `4`
    - Spaces are treated as characters ✓

## Common Pitfalls

1. **Not handling empty needle**:

   ```python
   # WRONG: Crashes or wrong answer
   def strStr(self, haystack, needle):
       return haystack.index(needle)  # Fails if needle = ""

   # CORRECT: Check for empty string first
   if not needle:
       return 0
   ```

2. **Not checking needle longer than haystack**:

   ```python
   # WRONG: Could access out of bounds
   for i in range(len(haystack)):
       if haystack[i:i+len(needle)] == needle:  # Might go past end

   # CORRECT: Limit range
   for i in range(len(haystack) - len(needle) + 1):
   ```

3. **Off-by-one in window size**:

   ```python
   # WRONG: Wrong range
   for i in range(len(haystack) - len(needle)):  # One position short

   # CORRECT: Include boundary
   for i in range(len(haystack) - len(needle) + 1):
   ```

4. **Comparing strings incorrectly**:

   ```python
   # WRONG: Character comparison won't work for substring
   if haystack[i] == needle:  # Wrong for multi-char needle

   # CORRECT: Compare substrings
   if haystack[i:i+len(needle)] == needle:
   ```

5. **Returning wrong index**:

   ```python
   # WRONG: Off by one
   return i + 1  # Should be just i

   # CORRECT: Return starting index
   return i
   ```

6. **Case sensitivity confusion**:
   ```python
   # Problem is case-sensitive by default
   # "Hello" and "hello" are different
   # Don't lowercase unless specified
   ```

## Optimization Notes

The implemented solution is **practical and efficient**:

- **Time**: O(n) on average with modern optimizations
- **Space**: O(1) - meets requirements
- **Performance**: Fast in practice despite theoretical worst case

**When to use each approach**:

- **Built-in methods**: Production code, interviews showing Pythonic skills
- **Sliding window**: Interviews showing algorithm understanding
- **KMP**: Advanced interviews, very large text processing
- **Z-Algorithm**: Competitive programming, pattern matching specialists

**Interview strategy**:

```
1. Ask about constraints (string sizes)
2. Start with built-in (if allowed)
3. Show understanding with sliding window
4. Mention KMP for optimization
5. Discuss time/space trade-offs
```

## String Matching Algorithm Comparison

| Algorithm              | Time        | Space  | Use Case              |
| ---------------------- | ----------- | ------ | --------------------- |
| Naive (sliding window) | O(n\*m)     | O(1)   | Small strings, simple |
| Built-in               | O(n) avg    | O(1)   | Production code       |
| KMP                    | O(n+m)      | O(m)   | Large text, optimal   |
| Boyer-Moore            | O(n/m) best | O(m)   | Very efficient        |
| Z-Algorithm            | O(n+m)      | O(n+m) | Multiple patterns     |

## Visual Example

```
String matching in action:

haystack = "hello"
needle = "ll"

Sliding window approach:

Position 0:
  "he" != "ll"

Position 1:
  "el" != "ll"

Position 2:
  "ll" == "ll" ✓ MATCH!
  Return 2


haystack = "ababcabc"
needle = "abc"

Position 0:
  "aba" != "abc"

Position 1:
  "bab" != "abc"

Position 2:
  "abc" == "abc" ✓ MATCH!
  Return 2


Built-in method:
  "abc" in "ababcabc" → True
  "ababcabc".index("abc") → 2
```

## Test Cases

```python
# Basic cases
strStr("hello", "ll")                       # 2
strStr("aaaaa", "bba")                      # -1

# Empty needle
strStr("abc", "")                           # 0

# Same string
strStr("test", "test")                      # 0

# At beginning
strStr("abcdef", "abc")                     # 0

# At end
strStr("abcdef", "def")                     # 3

# Not found
strStr("short", "longerneedle")             # -1

# Multiple occurrences (return first)
strStr("ababcabc", "abc")                   # 2

# Special characters
strStr("a!b@c#d$e%", "@c#d")                # 3

# Case sensitive
strStr("CaseSensitive", "casesensitive")    # -1

# Single character
strStr("a", "a")                            # 0

# Needle longer
strStr("a", "ab")                           # -1

# Repeated patterns
strStr("aaaa", "aa")                        # 0

# No match after partial
strStr("abab", "ba")                        # 1
```

## Thought Process

**Problem analysis**:

- Find first occurrence of substring in string
- Return index or -1 if not found
- Edge case: empty needle returns 0

**Key observations**:

1. Need to check all positions where needle could start
2. Each position: compare substring of needle length
3. Return immediately on first match
4. Different algorithms offer different trade-offs

**Algorithm considerations**:

**Naive sliding window**:

- Simple: move window across haystack
- Compare each window to needle
- O(n\*m) worst case but clear

**KMP improvement**:

- Avoids comparing same characters twice
- Uses failure function to skip positions
- O(n+m) optimal

**Why built-in is practical**:

- Uses optimized C implementation
- Often better than manual implementation
- Shows knowledge of standard library

**Optimal solution selection**:

```
For small strings: Built-in or sliding window
For large texts: KMP or Boyer-Moore
For interviews: Show 2-3 approaches
```

This problem tests:

- String manipulation skills
- Understanding of pattern matching
- Algorithm analysis and optimization
- Edge case handling
- Knowledge of standard library vs manual implementation

## Related Problems

- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/)
- [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)
- [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
- [796. Rotate String](https://leetcode.com/problems/rotate-string/)
