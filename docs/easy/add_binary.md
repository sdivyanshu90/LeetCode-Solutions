# Add Binary

## Problem Summary

Given two binary strings `a` and `b`, return their sum as a binary string.

**Example**: `a = "11"`, `b = "1"` → `"100"`

## Approach: Built-in Base Conversion (Implemented)

### Strategy

The solution uses Python's built-in base conversion and formatting to add binary strings:

1. Convert both binary strings to integers using `int(s, 2)`
2. Add the two integers
3. Convert the sum back to binary string using format specifier `:b`

```python
return f"{int(a, 2) + int(b, 2):b}"
```

### How It Works

**One-liner conversion approach**:

- `int(a, 2)` parses binary string `a` as a base-2 number
- `int(b, 2)` parses binary string `b` as a base-2 number
- Addition is performed on integers
- `f"{result:b}"` formats the integer back to binary without `0b` prefix

**Example**: `a = "11"`, `b = "1"`

```
int("11", 2) = 3
int("1", 2) = 1
3 + 1 = 4
f"{4:b}" = "100"
```

**Edge cases**:

- Both inputs `"0"` → returns `"0"`
- Leading zeros in inputs: `int()` handles them naturally
- Different lengths: conversion handles unequal lengths automatically

### Why Built-in Base Conversion Works

- **Correct interpretation**: Converting binary string to integer interprets the full binary number correctly
- **Arbitrary precision**: Python integers are arbitrary-precision, so conversion and addition produce the exact numeric sum without overflow
- **Clean formatting**: The `:b` format specifier serializes the integer back to binary representation without the `0b` prefix

### Complexity Analysis

- **Time Complexity**: O(n) where n = max(len(a), len(b))
  - Parsing each binary string: O(n) (scan and accumulate)
  - Addition of two big integers: O(n) in typical implementations
  - Formatting back to binary: O(n)
- **Space Complexity**: O(n)
  - Big integer objects and result string require O(n) space
  - Auxiliary space beyond inputs and output is O(1)

### Advantages

- **Simplicity**: One-liner that is easy to read and maintain
- **Correctness**: Arbitrary precision integers handle very long inputs without overflow
- **Readability**: Using Python's built-ins yields clean, idiomatic code
- **Performance**: Efficient for typical input sizes

### Disadvantages

- **Memory allocation**: Converting to big integers allocates memory proportional to string length
- **May be heavier**: For extremely long inputs, this may use more memory than a manual streaming approach
- **Built-in dependency**: Relies on Python's built-in functions

## Alternative Approach 1: Manual Bitwise Addition

Implement addition manually to avoid intermediate big-int objects:

```python
def add_binary_manual(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += ord(a[i]) - 48  # '0' -> 48
            i -= 1
        if j >= 0:
            total += ord(b[j]) - 48
            j -= 1
        res.append(str(total & 1))
        carry = total >> 1
    return ''.join(reversed(res))
```

### How It Works

- Use two indices starting from the end of `a` and `b` (least-significant bit)
- Maintain carry (0 or 1)
- At each step: add corresponding bits plus carry, append result bit
- After processing, reverse the result list and join into string

### Complexity

- **Time**: O(n) - same as built-in approach
- **Space**: O(n) for output, constant auxiliary space

### Advantages

- **Fine-grained control**: Avoids big-int allocation
- **Streaming**: Processes bits one at a time
- **Memory efficient**: Better for extremely long strings

### Disadvantages

- **More complex**: Requires manual index management and bit operations
- **Less readable**: More code compared to one-liner
- **Same asymptotic complexity**: Still O(n) time and space
