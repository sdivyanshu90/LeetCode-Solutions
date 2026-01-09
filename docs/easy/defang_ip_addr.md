# Defang IP Address

## Problem Summary

Given a valid IPv4 address, return a "defanged" version where every period `.` is replaced with `[.]`.

**Example**: `"1.1.1.1"` → `"1[.]1[.]1[.]1"`

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def defangIPaddr(self, address: str) -> str:
    res = ""
    for ip in address:
        if ip == ".":
            res += "[.]"
        else:
            res += ip
    return res
```

### How It Works

Simple character-by-character processing:

1. Initialize empty result string
2. For each character in address:
   - If it's a period: append `"[.]"`
   - Otherwise: append the character as-is
3. Return the constructed result

**Example** for `"192.168.0.1"`:

```
'1' → "1"
'9' → "19"
'2' → "192"
'.' → "192[.]"
'1' → "192[.]1"
'6' → "192[.]16"
'8' → "192[.]168"
'.' → "192[.]168[.]"
... → "192[.]168[.]0[.]1"
```

### Why Iteration Works

- **Character replacement**: Simple substitution pattern
- **String building**: Accumulates result character by character
- **Preserves order**: Processes left to right

### Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the address string. Each character is processed once.
- **Space Complexity**: O(n) for the result string.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
