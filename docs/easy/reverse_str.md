# Reverse String II

## Problem Summary

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string. If fewer than `k` characters remain, reverse all of them.

**Example**: `s = "abcdefg"`, `k = 2` → `"bacdfeg"`

## Current Implementation

The solution iterates through the string in steps of `2k`, reversing the first `k` characters in each chunk:

```python
def reverseStr(self, s: str, k: int) -> str:
    a = list(s)
    for i in range(0, len(a), 2*k):
        a[i : i+k] = reversed(a[i: i+k])
    return "".join(a)
```

## How It Works

The algorithm processes the string in chunks:

1. Convert string to list for in-place modification
2. Loop with step size `2k` (skipping every `2k` characters)
3. For each chunk, reverse first `k` characters using slice assignment
4. Python's slicing handles edge cases (fewer than k remaining)

**Example walkthrough** for `s = "abcdefg"`, `k = 2`:

```
Initial: ['a','b','c','d','e','f','g']

i=0: reverse a[0:2] → ['b','a','c','d','e','f','g']
i=4: reverse a[4:6] → ['b','a','c','d','f','e','g']
i=8: out of range, stop

Result: "bacdfeg"
```

**Edge case** (`k=3`, `s="abcdefghij"`):

```
i=0: reverse a[0:3] → "cbadefghij"
i=6: reverse a[6:9] → "cbadefihgj"
```

## Why This Works

- **Step size 2k**: Naturally divides string into alternating chunks
- **Slice reversal**: `reversed()` on slice creates reversed iterator
- **Automatic edge handling**: Python slices gracefully handle insufficient elements
- **Clean pattern**: Loop structure directly encodes the problem logic

## Time Complexity

O(n) where n is the length of the string. Each character is processed once (reading and possibly writing).

## Space Complexity

O(n) for the list conversion. The algorithm uses O(1) auxiliary space beyond that.

## Trade-offs

- **Pythonic**: Uses built-in `reversed()` and slice assignment elegantly
- **Simple**: Minimal code, easy to understand
- **String to list**: Necessary in Python since strings are immutable
- **Optimal**: Cannot do better than O(n) time since all characters must be examined
