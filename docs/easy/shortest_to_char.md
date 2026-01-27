# Shortest Distance to a Character

## Problem Summary

Given a string `s` and a character `c`, return an array of integers representing the shortest distance from each character to `c` in the string.

**Example**: `s = "loveleetcode"`, `c = 'e'` → `[3,2,1,0,1,0,0,1,2,2,1,0]`

## Approach: String Manipulation (Implemented)

### Strategy

The solution uses string manipulation to solve the problem efficiently.

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

### How It Works

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

### Why String Manipulation Works

- **Precomputing positions**: Avoids repeated scanning for `c`
- **Minimum distance**: Naturally finds closest occurrence of `c`
- **Handles all cases**: Works with one or multiple occurrences of `c`

### Complexity Analysis

- **Time Complexity**: O(n \* m) where n is string length and m is number of `c` occurrences. Worst case O(n²) if all characters are `c`, but typically much better.
- **Space Complexity**: O(m) for storing positions of `c`, plus O(n) for result array.

### Advantages

- Efficient string manipulation solution
- Clear and maintainable code

### Disadvantages

- May require additional space
