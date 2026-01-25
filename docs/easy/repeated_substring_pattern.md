# Repeated Substring Pattern

## Problem Summary

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

**LeetCode Problem**: [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

**LeetCode Problem**: [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

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

### Why Iteration Works

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

- **Time Complexity**: - **Theoretical best**: Used in string matching algorithms
- **Space Complexity**: O(1)

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
