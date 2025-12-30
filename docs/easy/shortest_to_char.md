# Shortest Distance to a Character

## Problem Summary

Given a string `s` and a character `c`, return an array of integers representing the shortest distance from each character to `c` in the string.

**Example**: `s = "loveleetcode"`, `c = 'e'` → `[3,2,1,0,1,0,0,1,2,2,1,0]`

## Current Implementation

The solution first collects all positions of `c`, then calculates minimum distance for each position:

```python
def shortestToChar(self, s: str, c: str) -> List[int]:
    temp = []
    for i in range(len(s)):
        if s[i] == c:
            temp.append(i)

    res = []
    for i in range(len(s)):
        if s[i] != c:
            res.append(min([abs(i - j) for j in temp]))
        else:
            res.append(0)
    return res
```

## How It Works

Two-pass algorithm:

1. **First pass**: Scan string and record all indices where character `c` appears in `temp`
2. **Second pass**: For each position `i`:
   - If `s[i] == c`: distance is 0
   - Otherwise: compute distance to all `c` positions, take minimum

**Example** for `s = "loveleetcode"`, `c = 'e'`:

```
Step 1: Find 'e' positions → temp = [3, 5, 6, 11]

Step 2: Calculate distances:
i=0: min(|0-3|, |0-5|, |0-6|, |0-11|) = min(3,5,6,11) = 3
i=1: min(|1-3|, |1-5|, |1-6|, |1-11|) = min(2,4,5,10) = 2
i=2: min(|2-3|, |2-5|, |2-6|, |2-11|) = min(1,3,4,9) = 1
i=3: s[3]=='e' → 0
...
```

## Why This Works

- **Precomputing positions**: Avoids repeated scanning for `c`
- **Minimum distance**: Naturally finds closest occurrence of `c`
- **Handles all cases**: Works with one or multiple occurrences of `c`

## Time Complexity

O(n \* m) where n is string length and m is number of `c` occurrences. Worst case O(n²) if all characters are `c`, but typically much better.

## Space Complexity

O(m) for storing positions of `c`, plus O(n) for result array.

## Trade-offs

- **Straightforward**: Easy to understand logic
- **Suboptimal**: Calculates distance to all `c` positions even when only nearest matters
- **Better O(n) approach**: Use two passes - one left-to-right tracking nearest `c` from left, one right-to-left tracking from right, take minimum. Example:

  ```python
  # Forward pass
  pos = float('-inf')
  for i, char in enumerate(s):
      if char == c: pos = i
      res[i] = i - pos

  # Backward pass
  pos = float('inf')
  for i in range(len(s)-1, -1, -1):
      if s[i] == c: pos = i
      res[i] = min(res[i], pos - i)
  ```
