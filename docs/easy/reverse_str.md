# Reverse String II

## Problem Summary

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string. If fewer than `k` characters remain, reverse all of them.

**Example**: `s = "abcdefg"`, `k = 2` → `"bacdfeg"`

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
def reverseStr(self, s: str, k: int) -> str:
    a = list(s)
    for i in range(0, len(a), 2*k):
        a[i : i+k] = reversed(a[i: i+k])
    return "".join(a)
```

### How It Works

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

### Why Iteration Works

- **Step size 2k**: Naturally divides string into alternating chunks
- **Slice reversal**: `reversed()` on slice creates reversed iterator
- **Automatic edge handling**: Python slices gracefully handle insufficient elements
- **Clean pattern**: Loop structure directly encodes the problem logic

### Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the string. Each character is processed once (reading and possibly writing).
- **Space Complexity**: O(n) for the list conversion. The algorithm uses O(1) auxiliary space beyond that.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
