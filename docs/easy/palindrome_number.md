# Palindrome Number

## Problem Summary

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number that reads the same backward as forward. For example, `121` is a palindrome while `123` is not.

**LeetCode Problem**: [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

**Follow-up**: Could you solve it without converting the integer to a string?

**LeetCode Problem**: [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def isPalindrome(self, x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
```

### How It Works

**Example 1**: `x = 121`

```
Convert to string: "121"
Reverse string: "121"[::-1] = "121"
Compare: "121" == "121"? Yes
Return True ✓
```

**Example 2**: `x = -121`

```
Convert to string: "-121"
Reverse string: "-121"[::-1] = "121-"
Compare: "-121" == "121-"? No
Return False ✓
```

**Example 3**: `x = 10`

```
Convert to string: "10"
Reverse string: "10"[::-1] = "01"
Compare: "10" == "01"? No
Return False ✓
```

### Why Two Pointers Works

For a palindrome:

- **Even length** (1221): First half equals reversed second half
- **Odd length** (12321): First half equals reversed second half (ignoring middle digit)

By only reversing half, we can compare in the middle!

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
