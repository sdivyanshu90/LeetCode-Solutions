# Occurrences After Bigram

## Problem Summary

- Given a text string and two words first and second, find all words that appear immediately after the bigram "first second".
- Return as a list of strings.
- Example: text = "alice is a good girl she is a good student", first = "a", second = "good" -> ["girl", "student"].

Current implementation (in repository)

- Implementation splits text and checks consecutive triplets:
  - Splits text into words array.
  - Iterates up to len-2 to avoid index out of bounds.
  - For each position, checks if word[i] == first and word[i+1] == second.
  - If match found, appends word[i+2] to result.
  - Returns list of all words following the bigram.
- Example code:
  ```python
  split_text = text.split(" ")
  for i in range(len(split_text) - 2):
      if split_text[i] == first and split_text[i + 1] == second:
          res.append(split_text[i + 2])
  ```

Why this works

- Splitting on spaces creates array of words for easy indexing.
- Checking consecutive pairs identifies bigram occurrences.
- i+2 position always exists because loop stops at len-2.
- Multiple occurrences of bigram all get counted (non-overlapping).

Time complexity

- Let n = number of words in text.
- Splitting text: O(n).
- Iterating through words: O(n).
- String comparisons: O(1) average for short words.
- Overall time complexity: O(n).

Space complexity

- Split text array: O(n) words.
- Result list: O(k) where k is number of matches, k <= n.
- Overall space complexity: O(n).

Thought process and trade-offs

- Simple array iteration: straightforward and efficient.
- Alternative: use sliding window or string pattern matching - more complex, no performance benefit.
- Alternative: regex pattern matching - possible but overkill for this problem.
- Current approach: optimal for this problem type.
- Note: splits on single space " ", assumes single space between words (standard for this problem).

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  split_text = text.split(" ")
  for i in range(len(split_text) - 2):
      if split_text[i] == first and split_text[i + 1] == second:
          res.append(split_text[i + 2])
  ```

### How It Works

- Note: splits on single space " ", assumes single space between words (standard for this problem).

### Why Iteration Works

- Splitting on spaces creates array of words for easy indexing.
- Checking consecutive pairs identifies bigram occurrences.
- i+2 position always exists because loop stops at len-2.
- Multiple occurrences of bigram all get counted (non-overlapping).

Time complexity

- Let n = number of words in text.
- Splitting text: O(n).
- Iterating through words: O(n).
- String comparisons: O(1) average for short words.
- Overall time complexity: O(n).

Space complexity

- Split text array: O(n) words.
- Result list: O(k) where k is number of matches, k <= n.
- Overall space complexity: O(n).

Thought process and trade-offs

- Simple array iteration: straightforward and efficient.
- Alternative: use sliding window or string pattern matching - more complex, no performance benefit.
- Alternative: regex pattern matching - possible but overkill for this problem.
- Current approach: optimal for this problem type.
- Note: splits on single space " ", assumes single space between words (standard for this problem).

### Complexity Analysis

- **Time Complexity**: - Let n = number of words in text. - Splitting text: O(n). - Iterating through words: O(n). - String comparisons: O(1) average for short words. - Overall time complexity: O(n). Space complexity - Split text array: O(n) words. - Result list: O(k) where k is number of matches, k <= n. - Overall space complexity: O(n). Thought process and trade-offs - Simple array iteration: straightforward and efficient. - Alternative: use sliding window or string pattern matching - more complex, no performance benefit. - Alternative: regex pattern matching - possible but overkill for this problem. - Current approach: optimal for this problem type. - Note: splits on single space " ", assumes single space between words (standard for this problem).
- **Space Complexity**: - Split text array: O(n) words. - Result list: O(k) where k is number of matches, k <= n. - Overall space complexity: O(n). Thought process and trade-offs - Simple array iteration: straightforward and efficient. - Alternative: use sliding window or string pattern matching - more complex, no performance benefit. - Alternative: regex pattern matching - possible but overkill for this problem. - Current approach: optimal for this problem type. - Note: splits on single space " ", assumes single space between words (standard for this problem).

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
