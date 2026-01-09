# Find Words That Can Be Formed by Characters

## Problem Summary

Given an array of `words` and a string `chars`, return the sum of lengths of all "good" words. A word is good if it can be formed using characters from `chars` (each character can be used at most as many times as it appears in `chars`).

**Example**: `words=["cat","bt","hat","tree"]`, `chars="atach"` → `6` ("cat" + "hat" = 3 + 3)

## Approach: Frequency Counting (Implemented)

### Strategy

The solution uses frequency counting to solve the problem efficiently.

```python
def countCharacters(self, words: List[str], chars: str) -> int:
    charsMap = {}
    result = 0
    for char in chars:
        if char not in charsMap:
            charsMap[char] = 1
        else:
            charsMap[char] += 1

    for word in words:
        charsMapCopy = charsMap.copy()
        end = True
        for char in word:
            if char in charsMapCopy and charsMapCopy[char] > 0:
                charsMapCopy[char] -= 1
            else:
                end = False
                break
        if end:
            result += len(word)

    return result
```

### How It Works

The algorithm uses frequency counting:

1. **Build frequency map**: Count how many times each character appears in `chars`
2. **For each word**:
   - Make a copy of the frequency map
   - Try to "spend" characters from the copy for each letter in the word
   - If any character is unavailable or depleted, mark as invalid
   - If all characters successfully used, add word length to result
3. **Return** total length

**Example** for `words=["cat","bt"]`, `chars="atach"`:

```
charsMap: {a:2, t:1, c:1, h:1}

Word "cat":
  Copy: {a:2, t:1, c:1, h:1}
  'c': available, copy={a:2, t:1, c:0, h:1}
  'a': available, copy={a:1, t:1, c:0, h:1}
  't': available, copy={a:1, t:0, c:0, h:1}
  All matched → result += 3

Word "bt":
  Copy: {a:2, t:1, c:1, h:1}
  'b': not in copy → fail

Result: 3
```

### Why Frequency Counting Works

- **Frequency tracking**: Ensures we don't use more of a character than available
- **Copy for each word**: Allows independent checking without mutating original map
- **Early termination**: Breaks as soon as a character cannot be matched
- **Count matching words**: Sums lengths of all formable words

### Complexity Analysis

- **Time Complexity**: O(n + m\*k) where n = len(chars), m = number of words, k = average word length. Building the map is O(n), and checking each word is O(k) with m words.
- **Space Complexity**: O(1) in terms of the character set (at most 26 lowercase letters). The copy operation is O(26) = O(1).

### Advantages

- Efficient frequency counting solution
- Clear and maintainable code

### Disadvantages

- May require additional space
