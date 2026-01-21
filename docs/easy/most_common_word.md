# Most Common Word

## Problem Summary

- Given a paragraph and list of banned words, find the most frequent non-banned word (case-insensitive).
- Words are separated by spaces and punctuation.
- Example: "Bob hit a ball..." with banned=["hit"] -> "ball".

Current implementation (in repository)

- Implementation uses regex and Counter:
  - Uses regex `\w+` to extract all words (ignoring punctuation).
  - Converts all words to lowercase for case-insensitive comparison.
  - Filters out banned words using list comprehension.
  - Uses Counter.most_common(1) to find most frequent word.
  - Returns the word (first element of tuple).
- Example code:
  ```python
  words = re.findall(r'\w+', paragraph.lower())
  return Counter([word for word in words if word not in banned]).most_common(1)[0][0]
  ```

Why this works

- Regex `\w+` matches word characters, automatically handling punctuation removal.
- Lowercase conversion ensures case-insensitive matching.
- List comprehension filters banned words before counting.
- Counter provides efficient frequency counting and most_common() method.
- most_common(1) returns list with one tuple: [(word, count)], so [0][0] extracts the word.

Time complexity

- Let n = length of paragraph, m = number of unique words, b = number of banned words.
- Regex findall: O(n).
- Filtering: O(m × b) for checking each word against banned list (could optimize with set).
- Counter: O(m).
- Overall time complexity: O(n + m × b).

Space complexity

- Words list: O(m) for unique words.
- Counter: O(m).
- Overall space complexity: O(m).

Thought process and trade-offs

- Regex approach: clean handling of punctuation and word boundaries.
- Counter: Pythonic solution for frequency counting.
- Optimization: convert banned to set for O(1) lookup instead of list - reduces complexity to O(n + m).
- Current approach: functional but could optimize banned word checking.

## Approach: Frequency Counting (Implemented)

### Strategy

The solution uses frequency counting to solve the problem efficiently.

```python
  words = re.findall(r'\w+', paragraph.lower())
  return Counter([word for word in words if word not in banned]).most_common(1)[0][0]
  ```

### How It Works

- Counter: Pythonic solution for frequency counting.
- Optimization: convert banned to set for O(1) lookup instead of list - reduces complexity to O(n + m).
- Current approach: functional but could optimize banned word checking.

### Why Frequency Counting Works

- Regex `\w+` matches word characters, automatically handling punctuation removal.
- Lowercase conversion ensures case-insensitive matching.
- List comprehension filters banned words before counting.
- Counter provides efficient frequency counting and most_common() method.
- most_common(1) returns list with one tuple: [(word, count)], so [0][0] extracts the word.

Time complexity

- Let n = length of paragraph, m = number of unique words, b = number of banned words.
- Regex findall: O(n).
- Filtering: O(m × b) for checking each word against banned list (could optimize with set).
- Counter: O(m).
- Overall time complexity: O(n + m × b).

Space complexity

- Words list: O(m) for unique words.
- Counter: O(m).
- Overall space complexity: O(m).

Thought process and trade-offs

- Regex approach: clean handling of punctuation and word boundaries.
- Counter: Pythonic solution for frequency counting.
- Optimization: convert banned to set for O(1) lookup instead of list - reduces complexity to O(n + m).
- Current approach: functional but could optimize banned word checking.

### Complexity Analysis

- **Time Complexity**: - Let n = length of paragraph, m = number of unique words, b = number of banned words. - Regex findall: O(n). - Filtering: O(m × b) for checking each word against banned list (could optimize with set). - Counter: O(m). - Overall time complexity: O(n + m × b). Space complexity - Words list: O(m) for unique words. - Counter: O(m). - Overall space complexity: O(m). Thought process and trade-offs - Regex approach: clean handling of punctuation and word boundaries. - Counter: Pythonic solution for frequency counting. - Optimization: convert banned to set for O(1) lookup instead of list - reduces complexity to O(n + m). - Current approach: functional but could optimize banned word checking.
- **Space Complexity**: - Words list: O(m) for unique words. - Counter: O(m). - Overall space complexity: O(m). Thought process and trade-offs - Regex approach: clean handling of punctuation and word boundaries. - Counter: Pythonic solution for frequency counting. - Optimization: convert banned to set for O(1) lookup instead of list - reduces complexity to O(n + m). - Current approach: functional but could optimize banned word checking.

### Advantages

- Efficient frequency counting solution
- Clear and maintainable code

### Disadvantages

- May require additional space
