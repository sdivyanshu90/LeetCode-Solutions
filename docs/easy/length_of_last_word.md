# Length of Last Word

## Problem Summary

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string. A **word** is a maximal substring consisting of non-space characters only.

**LeetCode Problem**: [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

**LeetCode Problem**: [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def lengthOfLastWord(self, s: str) -> int:
    ans = s.split()
    return len(ans[len(ans)-1])
```

### How It Works

**Example 1**: `s = "Hello World"`

```
s.split() → ["Hello", "World"]
Last element: "World"
Length: 5
```

**Example 2**: `s = "   fly me   to   the moon  "`

```
s.split() → ["fly", "me", "to", "the", "moon"]
Last element: "moon"
Length: 4
```

**Example 3**: `s = "luffy is still joyboy"`

```
s.split() → ["luffy", "is", "still", "joyboy"]
Last element: "joyboy"
Length: 6
```

### Why Iteration Works

The iteration approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
