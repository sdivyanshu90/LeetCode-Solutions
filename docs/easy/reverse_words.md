# Reverse Words in a String III

## Problem Summary

Given a string `s`, reverse the order of characters in each word within a sentence while preserving whitespace and word order.

**Example**: `"Let's take LeetCode contest"` → `"s'teL ekat edoCteeL tsetnoc"`

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def reverseWords(self, s: str) -> str:
    return " ".join([i[::-1] for i in s.split(" ")])
```

### How It Works

This one-liner combines several string operations:

1. **`s.split(" ")`**: Split string into list of words by spaces
2. **`i[::-1]`**: Reverse each word using Python slice notation (step=-1)
3. **`" ".join(...)`**: Join reversed words back with spaces

**Example breakdown** for `"Hello World"`:

```
split(" ") → ["Hello", "World"]
reverse each → ["olleH", "dlroW"]
join(" ") → "olleH dlroW"
```

### Why Iteration Works

- **Word separation**: `split(" ")` isolates individual words
- **Character reversal**: `[::-1]` reverses character order within each word
- **Reconstruction**: `join(" ")` reassembles with original spacing
- **Preserves structure**: Word order and spacing remain unchanged

### Complexity Analysis

- **Time Complexity**: O(n) where n is the total number of characters. Split, reverse, and join each require linear time.
- **Space Complexity**: O(n) for storing the split words list and the result string.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
