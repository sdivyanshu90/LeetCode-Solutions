# Is Subsequence

## Problem Summary

Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

**LeetCode Problem**: [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

## Approach 1: Two Pointers (Implemented)

### Strategy

The implemented solution uses a **two-pointer approach** to scan through both strings:

1. Use pointer `i` for string `s` (subsequence candidate)
2. Use pointer `j` for string `t` (main string)
3. When characters match, advance both pointers
4. When they don't match, only advance pointer `j`
5. If we reach the end of `s` (i.e., `i == n`), then `s` is a subsequence of `t`

**Code**:

```python
def isSubsequence(self, s: str, t: str) -> bool:
    n = len(s)
    i, j = 0, 0
    while i < n and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == n
```

### How It Works

**Example 1**: `s = "abc"`, `t = "ahbgdc"`

```
s: a b c
   ^

t: a h b g d c
   ^

Match 'a': i=1, j=1

s: a b c
     ^

t: a h b g d c
     ^

No match: j=2

s: a b c
     ^

t: a h b g d c
       ^

Match 'b': i=2, j=3

s: a b c
       ^

t: a h b g d c
         ^

No match: j=4

t: a h b g d c
           ^

No match: j=5

t: a h b g d c
             ^

Match 'c': i=3, j=6

i == n (3 == 3) → True
```

**Example 2**: `s = "axc"`, `t = "ahbgdc"`

```
After finding 'a', we look for 'x' but never find it.
Eventually j reaches end of t, but i is still at 1 (not equal to n=3)
→ False
```

### Complexity Analysis

- **Time Complexity**: O(n + m) where n = len(s), m = len(t)
  - In the worst case, we scan through all of `t`
  - We process each character at most once
- **Space Complexity**: O(1) - Only using two pointer variables

### Edge Cases Handled

- **Empty s**: `s = ""` → Always returns `True` (empty string is subsequence of any string)
- **Empty t**: `s = "a", t = ""` → Returns `False` (unless s is also empty)
- **Same strings**: `s == t` → Returns `True`
- **s longer than t**: Returns `False` (impossible to be subsequence)
- **Repeated characters**: Correctly matches in order

## Approach 2: Recursive

A recursive approach that mirrors the two-pointer logic:

```python
def isSubsequence(self, s: str, t: str) -> bool:
    def helper(i, j):
        # Base case: found all characters of s
        if i == len(s):
            return True
        # Base case: reached end of t without finding all of s
        if j == len(t):
            return False

        # If characters match, move both pointers
        if s[i] == t[j]:
            return helper(i + 1, j + 1)
        # If not, only move pointer in t
        else:
            return helper(i, j + 1)

    return helper(0, 0)
```

### Complexity

- **Time**: O(n + m) - Same as iterative
- **Space**: O(n + m) - Recursion call stack

### Drawback

- Uses more space due to call stack
- Risk of stack overflow for very long strings
- No real advantage over iterative approach

## Approach 3: Built-in Iterator

Using Python's iterator to find characters sequentially:

```python
def isSubsequence(self, s: str, t: str) -> bool:
    t_iter = iter(t)
    return all(char in t_iter for char in s)
```

### How It Works

- `iter(t)` creates an iterator over string `t`
- For each character in `s`, check if it exists in the remaining part of `t`
- The iterator maintains position, so subsequent searches continue from where we left off
- `all()` returns `True` if all characters are found

### Complexity

- **Time**: O(n + m)
- **Space**: O(1) - Iterator doesn't create new string

### Why This Works

- `char in t_iter` advances the iterator until it finds `char` or reaches the end
- Once a character is found, the iterator position is preserved
- This ensures the order is maintained

### Note

- Very Pythonic and concise
- Can be less intuitive to understand
- Performance is similar to two-pointer approach

## Approach 4: Follow-up - Binary Search for Multiple Queries

If there are many `s` strings to check against the same `t`, we can preprocess `t`:

```python
from collections import defaultdict
import bisect

def isSubsequence(self, s: str, t: str) -> bool:
    # Preprocess: create index map for each character in t
    char_indices = defaultdict(list)
    for i, char in enumerate(t):
        char_indices[char].append(i)

    # Current position in t
    current_pos = -1

    for char in s:
        if char not in char_indices:
            return False

        # Binary search for the next occurrence after current_pos
        indices = char_indices[char]
        idx = bisect.bisect_right(indices, current_pos)

        if idx == len(indices):
            return False  # No occurrence after current_pos

        current_pos = indices[idx]

    return True
```

### Preprocessing

- Build a map: `{char: [list of indices where char appears in t]}`
- Example: `t = "ahbgdc"` → `{'a': [0], 'h': [1], 'b': [2], 'g': [3], 'd': [4], 'c': [5]}`

### For Each Query

- For each character in `s`, use binary search to find its next occurrence after the current position
- Binary search: O(log k) where k is the number of occurrences of that character

### Complexity

- **Preprocessing**: O(m) to build the map
- **Per Query**: O(n log m) where n = len(s)
- **Space**: O(m) for the index map

### When to Use

- When you have **many queries** with the same `t` but different `s` strings
- Amortizes preprocessing cost over multiple queries
- If you only have one query, the simple two-pointer approach is better

## Comparison of Approaches

| Approach      | Time         | Space  | Pros                      | Cons                       |
| ------------- | ------------ | ------ | ------------------------- | -------------------------- |
| Two Pointers  | O(n+m)       | O(1)   | Simple, efficient, clear  | None for single query      |
| Recursive     | O(n+m)       | O(n+m) | Functional style          | Extra space, no advantages |
| Iterator      | O(n+m)       | O(1)   | Very Pythonic, concise    | Less intuitive             |
| Binary Search | O(n log m)\* | O(m)   | Fast for multiple queries | Overkill for single query  |

\*After O(m) preprocessing

## Edge Cases & Considerations

1. **Empty Subsequence**:

   - `s = "", t = "anything"` → `True`
   - Empty string is a subsequence of any string
   - The algorithm returns `True` because `i == 0 == n`

2. **Empty Main String**:

   - `s = "a", t = ""` → `False`
   - Non-empty string cannot be subsequence of empty string
   - Loop never executes, returns `i == n` → `0 == 1` → `False`

3. **Identical Strings**:

   - `s = "abc", t = "abc"` → `True`
   - Every character matches in order

4. **Longer Subsequence**:

   - `s = "longstring", t = "short"` → `False`
   - If `len(s) > len(t)`, impossible to be subsequence

5. **Repeated Characters**:

   - `s = "aa", t = "aaa"` → `True`
   - `s = "aa", t = "aba"` → `True`
   - Works correctly with repeated characters

6. **Order Matters**:

   - `s = "abc", t = "cba"` → `False`
   - Characters must appear in the same relative order

7. **Non-contiguous**:
   - `s = "ace", t = "abcde"` → `True`
   - Characters don't need to be adjacent

## Common Pitfalls

1. **Resetting Pointer on Mismatch**:

   ```python
   # WRONG: Don't reset i when characters don't match
   if s[i] == t[j]:
       i += 1
       j += 1
   else:
       i = 0  # ❌ Wrong!
       j += 1
   ```

   Only advance j, never reset i.

2. **Checking Both Pointers in Wrong Order**:

   ```python
   # WRONG: This can cause index out of bounds
   while i < n:
       if s[i] == t[j]:
           i += 1
       j += 1
   ```

   Must check both `i < n` AND `j < len(t)`.

3. **Wrong Return Condition**:

   ```python
   # WRONG: Checking j instead of i
   return j == len(t)
   ```

   Must check if we found all characters of s: `i == n`.

4. **Using `in` Operator Naively**:

   ```python
   # WRONG: This doesn't preserve order
   return all(char in t for char in s)
   ```

   This checks if characters exist, but not in order.

5. **Forgetting to Advance j**:
   ```python
   # WRONG: j must always advance
   while i < n and j < len(t):
       if s[i] == t[j]:
           i += 1
           j += 1
       # Missing: j += 1 for non-match case
   ```

## Optimization Notes

The two-pointer solution is **optimal** for a single query:

- O(n + m) time is the best possible (must examine characters)
- O(1) space is minimal
- Early termination when `i == n`

Possible micro-optimizations:

1. **Early exit if s is longer**: Check `len(s) > len(t)` first

   ```python
   if len(s) > len(t):
       return False
   ```

2. **Handle empty s early**:

   ```python
   if not s:
       return True
   ```

3. **For multiple queries**: Use the binary search approach with preprocessing

## Test Cases

```python
# Basic cases
isSubsequence("abc", "ahbgdc")        # True
isSubsequence("axc", "ahbgdc")        # False

# Edge cases
isSubsequence("", "ahbgdc")           # True (empty is subsequence)
isSubsequence("a", "")                # False
isSubsequence("", "")                 # True

# Same strings
isSubsequence("leetcode", "leetcode") # True

# Length mismatch
isSubsequence("long", "sh")           # False

# Position tests
isSubsequence("def", "abcdef")        # True (at end)
isSubsequence("abc", "abcdef")        # True (at beginning)
isSubsequence("bdf", "abcdef")        # True (scattered)

# Repeated characters
isSubsequence("aa", "aaa")            # True
isSubsequence("aa", "aba")            # True
isSubsequence("aaa", "aa")            # False

# Order matters
isSubsequence("abc", "cba")           # False
isSubsequence("ace", "abcde")         # True

# Large inputs
isSubsequence("a"*1000, "a"*10000)    # True
isSubsequence("a"*10000, "a"*1000)    # False
```

## Thought Process

The problem asks us to check if `s` is a subsequence of `t`, meaning all characters of `s` appear in `t` in the same relative order (but not necessarily contiguous).

**Key insight**: We need to find each character of `s` in `t` sequentially, without going backwards.

**Natural approach**:

1. Scan through `t` linearly
2. For each character in `s`, find it in the remaining part of `t`
3. If we find all characters, return `true`
4. If we reach the end of `t` before finding all characters of `s`, return `false`

**Implementation**: Two pointers naturally implement this:

- Pointer `i` tracks progress in `s` (how many characters we've found)
- Pointer `j` tracks position in `t` (where we're searching)
- Only advance `i` when we find a match
- Always advance `j` to continue scanning

This gives us O(n + m) time with O(1) space - optimal for this problem.

## Follow-up Question

**LeetCode Follow-up**: If there are lots of incoming `s` strings (e.g., billions) and you want to check them against the same `t`, how would you optimize?

**Answer**: Use the binary search approach:

1. **Preprocess once**: Build a map of character → list of indices in `t` (O(m) time, O(m) space)
2. **For each query**: Use binary search to find the next occurrence of each character (O(n log m) per query)
3. **Amortization**: Preprocessing cost is amortized over billions of queries

Example:

```python
# Preprocess once
t = "ahbgdc"
char_map = {'a': [0], 'h': [1], 'b': [2], 'g': [3], 'd': [4], 'c': [5]}

# For each s, use binary search instead of linear scan
# Much faster when there are many queries!
```

## Related Problems

- [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)
- [524. Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)
- [1055. Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/)
- [443. String Compression](https://leetcode.com/problems/string-compression/)
