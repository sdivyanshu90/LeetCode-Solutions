# Longest Common Prefix

## Problem Summary

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

**LeetCode Problem**: [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

**LeetCode Problem**: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Approach: Binary Search (Implemented)

### Strategy

The solution uses binary search to solve the problem efficiently.

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
```

### How It Works

**Example 1**: `strs = ["flower", "flow", "flight"]`

```
Initial: prefix = "flower"

String 2: "flow"
  - "flow"[:6] = "flow" ≠ "flower"
  - Shorten: prefix = "flowe"
  - "flow"[:5] = "flow" ≠ "flowe"
  - Shorten: prefix = "flow"
  - "flow"[:4] = "flow" == "flow" ✓

String 3: "flight"
  - "flight"[:4] = "flig" ≠ "flow"
  - Shorten: prefix = "flo"
  - "flight"[:3] = "fli" ≠ "flo"
  - Shorten: prefix = "fl"
  - "flight"[:2] = "fl" == "fl" ✓

Result: "fl"
```

**Example 2**: `strs = ["dog", "racecar", "car"]`

```
Initial: prefix = "dog"

String 2: "racecar"
  - "racecar"[:3] = "rac" ≠ "dog"
  - Shorten: prefix = "do"
  - "racecar"[:2] = "ra" ≠ "do"
  - Shorten: prefix = "d"
  - "racecar"[:1] = "r" ≠ "d"
  - Shorten: prefix = ""
  - Empty prefix, return ""

Result: ""
```

### Why Binary Search Works

The binary search approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient binary search solution
- Clear and maintainable code

### Disadvantages

- May require additional space
