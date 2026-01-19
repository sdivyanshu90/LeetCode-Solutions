# Maximum Number of Balloons

## Problem Summary

Given a string `text`, return the maximum number of times the word "balloon" can be formed using the characters from the text. Each character can only be used once.

**Example**: `"nlaebolko"` → `1`, `"loonbalxballpoon"` → `2`

## Approach: Frequency Counting (Implemented)

### Strategy

The solution uses frequency counting to solve the problem efficiently.

```python
def maxNumberOfBalloons(self, text: str) -> int:
    char_count = Counter(text)

    return min(
        char_count['b'],
        char_count['a'],
        char_count['l'] // 2,
        char_count['o'] // 2,
        char_count['n']
    )
```

### How It Works

The word "balloon" has specific character requirements:

- 'b': 1 time
- 'a': 1 time
- 'l': 2 times
- 'o': 2 times
- 'n': 1 time

The algorithm:

1. **Count all characters** in text using Counter
2. **Calculate bottleneck**:
   - For 'b', 'a', 'n': available count (appear once per "balloon")
   - For 'l', 'o': available count ÷ 2 (appear twice per "balloon")
3. **Return minimum**: The limiting character determines max instances

**Example** for `"loonbalxballpoon"`:

```
Counter: {l:4, o:4, n:2, b:2, a:2, x:1, p:1}

Constraints:
  'b': 2 → can make 2 "balloon"s
  'a': 2 → can make 2 "balloon"s
  'l': 4 ÷ 2 = 2 → can make 2 "balloon"s
  'o': 4 ÷ 2 = 2 → can make 2 "balloon"s
  'n': 2 → can make 2 "balloon"s

Result: min(2,2,2,2,2) = 2
```

**Example** for `"leetcode"`:

```
Counter: {e:3, l:1, t:1, c:1, o:1, d:1}
Missing 'b', 'a', 'n' → counts as 0
Result: min(0,0,0,0,0) = 0
```

### Why Frequency Counting Works

- **Frequency requirement**: Each "balloon" needs specific character counts
- **Minimum constraint**: The rarest character limits total instances
- **Integer division**: For 'l' and 'o', we need pairs, so divide by 2
- **Counter default**: Missing characters return 0, naturally handled by min()

### Complexity Analysis

- **Time Complexity**: O(n) where n is the length of text. Counter construction is O(n), and the min calculation is O(1) (fixed 5 values).
- **Space Complexity**: O(k) where k is the number of unique characters in text (at most 26 for lowercase letters).

### Advantages

- Efficient frequency counting solution
- Clear and maintainable code

### Disadvantages

- May require additional space
