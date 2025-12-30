# To Lower Case

## Problem Summary

Implement a function that converts all uppercase letters in a string to lowercase letters.

**Example**: `"Hello"` → `"hello"`

## Current Implementation

The solution uses Python's built-in string method:

```python
def toLowerCase(self, s: str) -> str:
    return s.lower()
```

## How It Works

This is a trivial one-liner that delegates to Python's built-in `str.lower()` method, which:

- Iterates through the string
- Converts each uppercase letter (A-Z) to its lowercase equivalent (a-z)
- Leaves all other characters unchanged (digits, punctuation, already-lowercase letters, etc.)

**Example**: `"TeSt123!@#"` → `"test123!@#"`

## Why This Works

- **Built-in efficiency**: Python's `lower()` is implemented in optimized C code
- **Unicode support**: Handles international characters correctly
- **Comprehensive**: Covers all uppercase letters defined in Unicode, not just A-Z

## Time Complexity

O(n) where n is the length of the string. Must examine each character.

## Space Complexity

O(n) for the new string created. Strings are immutable in Python, so a new string must be created.

## Trade-offs

- **Simplest solution**: One-liner using standard library
- **Best practice**: Use well-tested library functions rather than reimplementing
- **Unicode-aware**: Handles international characters (e.g., "CAFÉ" → "café")
- **Manual implementation** (if built-in not allowed):
  ```python
  def toLowerCase(self, s: str) -> str:
      return ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s)
  ```
  This only handles ASCII A-Z, not full Unicode.

## Notes

This problem is typically used to test:

- Knowledge of string manipulation basics
- Understanding of ASCII/Unicode character codes
- When to use library functions vs custom implementation
