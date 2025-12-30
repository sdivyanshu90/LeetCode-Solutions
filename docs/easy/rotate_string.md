# Rotate String

## Problem Summary

Given two strings `A` and `B`, return `true` if `B` is a rotation of `A`, meaning `B` can be formed by rotating `A` left by some number of positions.

**Example**: `A = "abcde"`, `B = "cdeab"` → `true` (rotate left by 2)

## Current Implementation

The solution implements the KMP (Knuth-Morris-Pratt) string matching algorithm to check if `B` appears in `A+A`:

```python
def rotateString(self, A, B):
    N = len(A)
    if N != len(B): return False
    if N == 0: return True

    shifts = [1] * (N+1)
    left = -1
    for right in range(N):
        while left >= 0 and B[left] != B[right]:
            left -= shifts[left]
        shifts[right + 1] = right - left
        left += 1

    match_len = 0
    for char in A+A:
        while match_len >= 0 and B[match_len] != char:
            match_len -= shifts[match_len]
        match_len += 1
        if match_len == N:
            return True
    return False
```

## How It Works

The solution uses KMP pattern matching with a key insight:

**Key insight**: If `B` is a rotation of `A`, then `B` will appear as a substring in `A+A`.

Example: `A = "abcde"`, `B = "cdeab"`

- `A+A = "abcdeabcde"`
- `B = "cdeab"` appears at index 2 in `A+A`

The KMP algorithm:

1. **Build failure function** (`shifts` array): Preprocesses pattern `B` for efficient matching
2. **Search in `A+A`**: Uses the shifts array to avoid redundant comparisons
3. **Return on match**: Once full pattern matched, return `true`

## Why This Works

- **Rotation property**: Any rotation creates a substring in the doubled string
- **KMP efficiency**: Avoids naive O(n²) substring search
- **Failure function**: Enables smart backtracking during mismatches

## Time Complexity

O(n) where n is the length of the strings. KMP preprocessing is O(n) and searching is O(n).

## Space Complexity

O(n) for the shifts/failure function array and the concatenated string `A+A`.

## Trade-offs

- **Optimal algorithm**: KMP is theoretically optimal for string matching
- **Complex implementation**: KMP is more intricate than simpler approaches
- **Alternative simpler solution**: `return len(A) == len(B) and B in A+A` (Python's `in` uses efficient C-level string search, often faster in practice)
- **Academic value**: Demonstrates KMP algorithm understanding
