# Unique Number of Occurrences

## Problem Summary

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique, otherwise return `false`.

**Example**: `[1,2,2,1,1,3]` → `true` (1 appears 3 times, 2 appears 2 times, 3 appears 1 time - all unique)

## Current Implementation

The solution uses frequency counting followed by uniqueness check:

```python
def uniqueOccurrences(self, arr: List[int]) -> bool:
    freq = {}
    has = set()
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    for key, val in freq.items():
        if val in has:
            return False
        has.add(val)
    return True
```

## How It Works

The algorithm performs two-phase checking:

1. **Phase 1 - Count frequencies**:
   - Build a dictionary mapping each number to its occurrence count
2. **Phase 2 - Check uniqueness**:
   - Use a set to track seen frequencies
   - For each frequency:
     - If already in set: duplicate frequency found, return `false`
     - Otherwise: add to set
   - If all frequencies unique: return `true`

**Example** for `[1,2,2,1,1,3]`:

```
Phase 1 - Count:
  freq = {1: 3, 2: 2, 3: 1}

Phase 2 - Check uniqueness:
  Frequency 3: not in has, add → has={3}
  Frequency 2: not in has, add → has={3,2}
  Frequency 1: not in has, add → has={3,2,1}

Result: True (all unique)
```

**Example** for `[1,2]`:

```
Phase 1: freq = {1: 1, 2: 1}

Phase 2:
  Frequency 1: not in has, add → has={1}
  Frequency 1: already in has → return False

Result: False (duplicate frequency)
```

## Why This Works

- **Frequency counting**: First phase determines how often each number appears
- **Set for uniqueness**: Set naturally detects duplicates via membership test
- **Two separate concerns**: Counting and uniqueness checking are cleanly separated
- **Early termination**: Returns immediately upon finding duplicate frequency

## Time Complexity

O(n) where n is the array length. First pass counts (O(n)), second pass checks uniqueness (O(k) where k is number of unique values, k ≤ n).

## Space Complexity

O(n) for the frequency dictionary and set in worst case (all unique elements).

## Trade-offs

- **Clear logic**: Two-phase approach is easy to understand
- **Efficient**: Linear time with early termination
- **Could simplify**: Can combine into one step using Counter:
  ```python
  from collections import Counter
  freq = Counter(arr)
  return len(freq.values()) == len(set(freq.values()))
  ```
  More concise but checks all values without early exit.
- **Alternative one-liner**:
  ```python
  freq = Counter(arr)
  return len(freq) == len(set(freq.values()))
  ```
