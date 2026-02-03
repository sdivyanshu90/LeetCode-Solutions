# Unique Morse Code Words

## Problem Summary

International Morse Code defines a standard encoding where each letter is mapped to a sequence of dots and dashes. Given an array of `words`, return the number of different transformations when each word is converted to Morse code.

**Example**: `["gin","zen","gig","msg"]` → `2` (gin, zen, msg → same code, gig → different)

## Approach: String Manipulation (Implemented)

### Strategy

The solution uses string manipulation to solve the problem efficiently.

```python
def uniqueMorseRepresentations(self, words: List[str]) -> int:
    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    res = []
    for word in words:
        temp = ""
        for char in word:
            idx = ord(char) - ord('a')
            temp += table[idx]
        res.append(temp)
    return len(set(res))
```

### How It Works

The algorithm performs transformation and deduplication:

1. **Morse lookup table**: Array indexed 0-25 for letters a-z
2. **For each word**:
   - Convert each character to its Morse equivalent using `ord(char) - ord('a')` as index
   - Concatenate Morse codes to form word representation
3. **Count unique**: Use set to eliminate duplicates, return set size

**Example** for `["gin","zen"]`:

```
"gin": g(--.) + i(..) + n(-.) = "--..-.."
"zen": z(--..) + e(.) + n(-.) = "--..-.."
Unique codes: {"--..-.."} → count = 1
```

### Why String Manipulation Works

- **Standard mapping**: Morse table provides deterministic letter-to-code conversion
- **String building**: Concatenating Morse codes creates unique identifier for each word
- **Set deduplication**: Automatically handles identical transformations
- **ASCII math**: `ord(char) - ord('a')` maps 'a'→0, 'b'→1, ..., 'z'→25

### Complexity Analysis

- **Time Complexity**: O(n \* m) where n is number of words and m is average word length. Each character requires O(1) lookup and O(1) string append (amortized).
- **Space Complexity**: O(n \* m) for storing Morse representations in the result list and set. In worst case, all words have unique Morse codes.

### Advantages

- Efficient string manipulation solution
- Clear and maintainable code

### Disadvantages

- May require additional space
