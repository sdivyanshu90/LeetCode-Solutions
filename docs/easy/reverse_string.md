# Reverse String

## Problem Summary

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

**LeetCode Problem**: [344. Reverse String](https://leetcode.com/problems/reverse-string/)

**LeetCode Problem**: [Reverse String](https://leetcode.com/problems/reverse-string/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

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

### Why Two Pointers Works

The two pointers approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: constraints - Pythonic vs universal solutions

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
