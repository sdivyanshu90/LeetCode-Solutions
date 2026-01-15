# Is Subsequence

## Problem Summary

Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

**LeetCode Problem**: [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

**LeetCode Problem**: [Is Subsequence](https://leetcode.com/problems/is-subsequence/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

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

### Why Two Pointers Works

- `char in t_iter` advances the iterator until it finds `char` or reaches the end
- Once a character is found, the iterator position is preserved
- This ensures the order is maintained

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
