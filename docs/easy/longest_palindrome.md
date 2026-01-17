# Longest Palindrome

## Problem Summary

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

**LeetCode Problem**: [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

**LeetCode Problem**: [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
def longestPalindrome(self, s: str) -> int:
    character_set = set()
    res = 0

    # Loop over characters in the string
    for c in s:
        # If set contains the character, match found
        if c in character_set:
            character_set.remove(c)
            # Add the two occurrences to our palindrome
            res += 2
        else:
            # Add the character to the set
            character_set.add(c)

    # If any character remains, we have at least one unmatched
    # character to make the center of an odd length palindrome.
    if character_set:
        res += 1

    return res
```

### How It Works

**Example 1**: `s = "abccccdd"`

```
Character 'a':
  - Not in set, add to set
  - Set: {'a'}, Result: 0

Character 'b':
  - Not in set, add to set
  - Set: {'a', 'b'}, Result: 0

Character 'c':
  - Not in set, add to set
  - Set: {'a', 'b', 'c'}, Result: 0

Character 'c':
  - In set! Remove from set, add 2 to result
  - Set: {'a', 'b'}, Result: 2

Character 'c':
  - Not in set, add to set
  - Set: {'a', 'b', 'c'}, Result: 2

Character 'c':
  - In set! Remove from set, add 2 to result
  - Set: {'a', 'b'}, Result: 4

Character 'd':
  - Not in set, add to set
  - Set: {'a', 'b', 'd'}, Result: 4

Character 'd':
  - In set! Remove from set, add 2 to result
  - Set: {'a', 'b'}, Result: 6

After loop: Set not empty (has 'a' or 'b'), add 1 for center
Final result: 7

Possible palindrome: "dccaccd" or "dccbccd"
```

**Example 2**: `s = "a"`

```
Character 'a':
  - Not in set, add to set
  - Set: {'a'}, Result: 0

After loop: Set not empty, add 1 for center
Final result: 1
```

### Why Hash Map Works

The hash map approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space
