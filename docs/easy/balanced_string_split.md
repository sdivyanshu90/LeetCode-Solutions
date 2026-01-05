# Split a String in Balanced Strings

## Problem Summary

Given a balanced string `s` containing only 'R' and 'L' characters, split it into the maximum number of balanced substrings. A balanced string has an equal number of 'L' and 'R' characters.

**Example**: `"RLRRLLRLRL"` → `4` (can be split as "RL", "RRLL", "RL", "RL")

## Current Implementation

The solution uses a counter to track balance and counts splits when balanced:

```python
def balancedStringSplit(self, s: str) -> int:
    temp = 0
    res = 0

    for i in range(len(s)):
        if s[i] == 'L':
            temp += 1
        else:
            temp -= 1
        if temp == 0:
            res += 1
    return res
```

## How It Works

The algorithm uses a running balance counter:

1. **Initialize**: `temp=0` tracks balance, `res=0` counts splits
2. **For each character**:
   - If 'L': increment counter (+1)
   - If 'R': decrement counter (-1)
   - If counter reaches 0: we have a balanced substring, increment result
3. **Return** total count of balanced substrings

**Key insight**: Greedily split at earliest balance point maximizes count.

**Example** for `"RLRRLLRLRL"`:

```
'R': temp=-1
'L': temp=0 → res=1 (split "RL")
'R': temp=-1
'R': temp=-2
'L': temp=-1
'L': temp=0 → res=2 (split "RRLL")
'R': temp=-1
'L': temp=0 → res=3 (split "RL")
'R': temp=-1
'L': temp=0 → res=4 (split "RL")
Result: 4
```

## Why This Works

- **Balance tracking**: +1 for L, -1 for R means temp=0 when counts equal
- **Greedy is optimal**: Splitting as early as possible maximizes total splits (can't do better by waiting)
- **Mathematical proof**: If we wait to combine two balanced substrings, we get 1 split instead of 2
- **Single pass**: Processes each character exactly once

## Time Complexity

O(n) where n is the length of the string. Single pass through all characters.

## Space Complexity

O(1) - only uses two integer variables regardless of input size.

## Trade-offs

- **Optimal**: Greedy approach achieves maximum splits
- **Simple**: Clean counter-based logic
- **Efficient**: Cannot do better than O(n) time since all characters must be examined
- **Elegant**: The balance counter naturally identifies split points
