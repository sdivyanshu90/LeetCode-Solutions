# Defang IP Address

## Problem Summary

Given a valid IPv4 address, return a "defanged" version where every period `.` is replaced with `[.]`.

**Example**: `"1.1.1.1"` → `"1[.]1[.]1[.]1"`

## Current Implementation

The solution iterates through characters and replaces periods:

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

## How It Works

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

## Why This Works

- **Character replacement**: Simple substitution pattern
- **String building**: Accumulates result character by character
- **Preserves order**: Processes left to right

## Time Complexity

O(n) where n is the length of the address string. Each character is processed once.

## Space Complexity

O(n) for the result string.

## Trade-offs

- **Straightforward**: Easy to understand logic
- **String concatenation**: In Python, string concatenation in loops can be inefficient (creates new string each time), but for small inputs like IP addresses (max ~15 chars), this is negligible
- **Much simpler alternative**: Python's built-in replace:
  ```python
  def defangIPaddr(self, address: str) -> str:
      return address.replace(".", "[.]")
  ```
  One-liner that's more efficient and idiomatic.
- **Another alternative**: Using join with generator:
  ```python
  return ''.join('[.]' if c == '.' else c for c in address)
  ```
  Avoids repeated string concatenation.
