# Goat Latin

## Problem Summary

Convert a sentence to "Goat Latin" using these rules:

1. If a word starts with a vowel, append "ma" to the end
2. If a word starts with a consonant, move the first letter to the end and append "ma"
3. Add one letter 'a' to the end for each word index (first word gets 'a', second gets 'aa', etc.)

**Example**: `"I speak Goat Latin"` → `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"`

## Approach: String Manipulation (Implemented)

### Strategy

The solution uses string manipulation to solve the problem efficiently.

```python
def toGoatLatin(self, sentence: str) -> str:
    spl = sentence.split(" ")
    vowel = "aeiouAEIOU"
    for i in range(len(spl)):
        if spl[i][0] in vowel:
            spl[i] = spl[i] + "ma"
        else:
            spl[i] = spl[i][1:] + spl[i][0] + "ma"
        spl[i] = spl[i] + "a" * (i + 1)
    return " ".join(spl)
```

### How It Works

The algorithm processes words sequentially:

1. **Split**: Separate sentence into words
2. **For each word** (with index i):
   - **Check first letter**: If vowel, append "ma"; if consonant, rotate first letter to end and append "ma"
   - **Add index suffix**: Append 'a' repeated (i+1) times
3. **Join**: Reconstruct sentence with spaces

**Example** for `"I speak"`:

```
Word 0 "I": vowel → "I" + "ma" + "a"*1 = "Imaa"
Word 1 "speak": consonant → "peaks" + "ma" + "a"*2 = "peaksmaaa"
Result: "Imaa peaksmaaa"
```

### Why String Manipulation Works

- **Rule encoding**: Each transformation step directly implements one rule
- **Index tracking**: Loop index naturally provides word position for suffix
- **String building**: Concatenation constructs each modified word
- **Vowel check**: Using membership test in vowel string handles all cases

### Complexity Analysis

- **Time Complexity**: O(n _ m) where n is number of words and m is average word length. For each word, we perform string operations proportional to word length. The `"a" _ (i+1)` adds up to O(n²) total characters across all words. More precisely: O(total_chars + n²) where n is word count.
- **Space Complexity**: O(n \* m) for storing the word list and building result strings.

### Advantages

- Efficient string manipulation solution
- Clear and maintainable code

### Disadvantages

- May require additional space
