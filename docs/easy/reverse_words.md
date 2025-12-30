# Reverse Words in a String III

## Problem Summary

Given a string `s`, reverse the order of characters in each word within a sentence while preserving whitespace and word order.

**Example**: `"Let's take LeetCode contest"` → `"s'teL ekat edoCteeL tsetnoc"`

## Current Implementation

The solution uses list comprehension to split, reverse, and rejoin words:

```python
def reverseWords(self, s: str) -> str:
    return " ".join([i[::-1] for i in s.split(" ")])
```

## How It Works

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

## Why This Works

- **Word separation**: `split(" ")` isolates individual words
- **Character reversal**: `[::-1]` reverses character order within each word
- **Reconstruction**: `join(" ")` reassembles with original spacing
- **Preserves structure**: Word order and spacing remain unchanged

## Time Complexity

O(n) where n is the total number of characters. Split, reverse, and join each require linear time.

## Space Complexity

O(n) for storing the split words list and the result string.

## Trade-offs

- **Extremely concise**: One-line solution is readable and maintainable
- **Pythonic**: Leverages Python's powerful string methods
- **Space allocation**: Creates intermediate list, but unavoidable for this approach
- **Performance**: Highly optimized built-in methods make this very efficient in practice
- **Alternative**: Could manually iterate and build result, but would be more verbose with similar complexity
