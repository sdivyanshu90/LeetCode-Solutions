# Uncommon Words from Two Sentences

## Problem Summary

Given two sentences `s1` and `s2`, return all words that appear exactly once across both sentences (uncommon words). A word is uncommon if it appears exactly once in one sentence and not at all in the other, or once total across both.

**Example**: `s1 = "this apple is sweet"`, `s2 = "this apple is sour"` → `["sweet", "sour"]`

## Current Implementation

The solution uses a frequency counter to track word occurrences:

```python
def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    count = {}
    for word in s1.split():
        count[word] = count.get(word, 0) + 1
    for word in s2.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]
```

## How It Works

The algorithm counts all word frequencies across both sentences:

1. **Count s1 words**: Add each word from sentence 1 to frequency map
2. **Count s2 words**: Add each word from sentence 2 (incrementing if already exists)
3. **Filter**: Return only words with count exactly equal to 1

**Example** for `s1 = "apple apple"`, `s2 = "banana"`:

```
After s1: count = {"apple": 2}
After s2: count = {"apple": 2, "banana": 1}
Filter count==1: ["banana"]
```

**Example** for `s1 = "this apple is sweet"`, `s2 = "this apple is sour"`:

```
After s1: count = {"this": 1, "apple": 1, "is": 1, "sweet": 1}
After s2: count = {"this": 2, "apple": 2, "is": 2, "sweet": 1, "sour": 1}
Filter count==1: ["sweet", "sour"]
```

## Why This Works

- **Unified counting**: Combining both sentences treats them as one corpus
- **Frequency filter**: Words appearing exactly once are uncommon by definition
- **Hash map efficiency**: O(1) lookup and update per word
- **Handles all cases**: Works whether word appears in one sentence or split across both

## Time Complexity

O(n + m) where n and m are the lengths of the two sentences. We process each word once for counting and once for filtering.

## Space Complexity

O(k) where k is the number of unique words across both sentences (for the count dictionary).

## Trade-offs

- **Straightforward**: Simple frequency counting approach
- **Clean filter**: Final list comprehension clearly expresses the condition
- **Alternative using Counter**: Could use `collections.Counter` for more concise code:
  ```python
  from collections import Counter
  count = Counter(s1.split() + s2.split())
  return [word for word in count if count[word] == 1]
  ```
- **Optimal**: O(n+m) time is optimal since we must examine all words
