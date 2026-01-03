# Number of Equivalent Domino Pairs

## Problem Summary

Given a list of `dominoes` where each domino is `[a,b]`, count pairs of equivalent dominoes. Two dominoes `[a,b]` and `[c,d]` are equivalent if `(a==c and b==d)` or `(a==d and b==c)`.

**Example**: `[[1,2],[2,1],[3,4],[5,6]]` → `1` (one pair: [1,2] and [2,1])

## Current Implementation

The solution uses a frequency array and normalized encoding:

```python
def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    num = [0] * 100
    ret = 0
    for x, y in dominoes:
        val = x * 10 + y if x <= y else y * 10 + x
        ret += num[val]
        num[val] += 1
    return ret
```

## How It Works

The algorithm normalizes dominoes and counts pairs:

1. **Normalization**: Encode domino as `small*10 + large` to make `[1,2]` and `[2,1]` identical (both become 12)
2. **For each domino**:
   - Compute normalized value
   - Add current count of this value to result (number of pairs this domino can form with previous ones)
   - Increment count for this value
3. **Return** total pairs

**Key insight**: If we've seen a domino k times before, the current domino forms k new pairs.

**Example** for `[[1,2],[1,2],[1,1],[1,2]]`:

```
[1,2]: val=12, ret+=num[12]=0, num[12]=1 → ret=0
[1,2]: val=12, ret+=num[12]=1, num[12]=2 → ret=1
[1,1]: val=11, ret+=num[11]=0, num[11]=1 → ret=1
[1,2]: val=12, ret+=num[12]=2, num[12]=3 → ret=3
Result: 3 pairs
```

## Why This Works

- **Normalization**: Treats `[a,b]` and `[b,a]` as identical by always encoding as `min*10+max`
- **Incremental counting**: Each domino forms pairs with all previously seen identical dominoes
- **Array indexing**: Since domino values are 1-9, encoding as `x*10+y` gives range 11-99, fits in size-100 array
- **Avoids double counting**: Count pairs as we go, not after seeing all

## Time Complexity

O(n) where n is the number of dominoes. Single pass through the list.

## Space Complexity

O(1) - uses fixed-size array of 100 elements regardless of input size.

## Trade-offs

- **Efficient**: O(1) lookup and update via array indexing
- **Clever encoding**: Two-digit number uniquely identifies normalized domino
- **Fixed space**: Array size independent of input
- **Constraint-dependent**: Relies on domino values being 1-9 (problem constraint)
- **Alternative with hash map**: More general but slightly slower:
  ```python
  count = {}
  ret = 0
  for x, y in dominoes:
      key = (min(x,y), max(x,y))
      ret += count.get(key, 0)
      count[key] = count.get(key, 0) + 1
  return ret
  ```
