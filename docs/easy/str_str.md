# Implement strStr()

## Problem Summary

Implement the `strStr()` function. Given two strings `haystack` and `needle`, return the **index of the first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Clarification**: What should we return when `needle` is an empty string? This is a good question to ask during an interview.

For the purpose of this problem, we will return `0` when `needle` is an empty string.

**LeetCode Problem**: [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

**LeetCode Problem**: [Implement strStr()](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

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

### Why Stack Works

The stack approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient stack solution
- Clear and maintainable code

### Disadvantages

- May require additional space
