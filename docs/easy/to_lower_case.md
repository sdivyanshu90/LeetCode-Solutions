# To Lower Case

## Problem Summary

Implement a function that converts all uppercase letters in a string to lowercase letters.

**Example**: `"Hello"` → `"hello"`

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def toLowerCase(self, s: str) -> str:
    return s.lower()
```

### How It Works

This is a trivial one-liner that delegates to Python's built-in `str.lower()` method, which:

- Iterates through the string
- Converts each uppercase letter (A-Z) to its lowercase equivalent (a-z)
- Leaves all other characters unchanged (digits, punctuation, already-lowercase letters, etc.)

**Example**: `"TeSt123!@#"` → `"test123!@#"`

### Why Iteration Works

- **Built-in efficiency**: Python's `lower()` is implemented in optimized C code
- **Unicode support**: Handles international characters correctly
- **Comprehensive**: Covers all uppercase letters defined in Unicode, not just A-Z

### Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the string. Must examine each character.
- **Space Complexity**: O(n) for the new string created. Strings are immutable in Python, so a new string must be created.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
