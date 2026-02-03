# Unique Number of Occurrences

## Problem Summary

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique, otherwise return `false`.

**Example**: `[1,2,2,1,1,3]` → `true` (1 appears 3 times, 2 appears 2 times, 3 appears 1 time - all unique)

## Approach: Frequency Counting with Set (Implemented)

### Strategy

The solution uses a two-phase approach:

1. Build a frequency dictionary to count occurrences of each number
2. Use a set to check if all frequency counts are unique

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

### How It Works

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

### Why Frequency Counting with Set Works

- **Frequency counting**: First phase determines how often each number appears in the array
- **Set for uniqueness detection**: Sets naturally detect duplicates via membership test in O(1) time
- **Two separate concerns**: Counting and uniqueness checking are cleanly separated for clarity
- **Early termination**: Returns immediately upon finding duplicate frequency, avoiding unnecessary work

### Complexity Analysis

- **Time Complexity**: O(n) where n is the array length
  - First pass counts frequencies: O(n)
  - Second pass checks uniqueness: O(k) where k is number of unique values (k ≤ n)
  - Total: O(n) + O(k) = O(n)
- **Space Complexity**: O(n)
  - Frequency dictionary stores up to n unique numbers in worst case
  - Set stores up to k frequency values
  - Total space: O(n)

### Advantages

- **Clear logic**: Two-phase approach is intuitive and easy to understand
- **Efficient**: Linear time complexity with early termination on duplicate
- **Explicit**: Each step is clearly defined and easy to debug
- **No extra imports**: Uses only basic Python data structures

### Disadvantages

- **Could be more concise**: Can be simplified using Counter from collections
- **No early exit in counting**: Must count all frequencies before checking
- **Two passes**: Requires iterating through data structures twice

## Alternative Approach 1: Using Counter (More Concise)

Use Python's Counter class for cleaner code:

```python
from collections import Counter

def uniqueOccurrences(self, arr: List[int]) -> bool:
    freq = Counter(arr)
    return len(freq.values()) == len(set(freq.values()))
```

### How It Works

- `Counter(arr)` automatically counts all frequencies
- Compare the number of frequencies with the number of unique frequencies
- If they match, all frequencies are unique

### Complexity

- **Time**: O(n) - single pass through array
- **Space**: O(n) - Counter and set storage

### Advantages

- **More concise**: One-liner logic after Counter creation
- **Pythonic**: Uses standard library efficiently
- **Clean**: No manual dictionary building

### Disadvantages

- **No early exit**: Must check all values before comparison
- **Requires import**: Depends on collections module
