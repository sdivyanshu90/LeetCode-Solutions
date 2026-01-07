# Find Common Characters

## Problem Summary

- Given an array of strings, find all characters that appear in every string including duplicates.
- Return the characters in any order.
- Example: ["bella","label","roller"] -> ["e","l","l"] (appears in all three).

Current implementation (in repository)

- Implementation iterates through first word's characters:
  - For each character in words[0], checks if it exists in all other words.
  - Uses `all()` function with generator to verify presence in remaining words.
  - If character is common, adds to result and removes one occurrence from each word.
  - Removal ensures duplicates are handled correctly (each occurrence matched once).
- Example code:
  ```python
  for char in words[0]:
      if all(char in word for word in words[1:]):
          result.append(char)
          words = [word.replace(char, '', 1) for word in words]
  ```

Why this works

- Using first word as reference ensures only characters present there are considered.
- `all()` checks guarantee character exists in every word.
- Removing one occurrence (`.replace(char, '', 1)`) handles duplicate counting correctly.
- Each matched character is counted as many times as it appears in all words (minimum frequency).

Time complexity

- Let n = number of words, m = average length of words.
- For each character in first word (m iterations):
  - Check all other words: O(n × m) for `all()` check.
  - Replace in all words: O(n × m).
- Overall time complexity: O(m × n × m) = O(n × m²).

Space complexity

- Result list: O(m) for storing common characters.
- Modified words list: O(n × m) for creating new word copies after replacements.
- Overall space complexity: O(n × m).

Thought process and trade-offs

- Character-by-character approach: intuitive but not optimal for performance.
- Alternative efficient approach: use Counter to count character frequencies in each word, then find minimum frequency for each character across all words. Time: O(n × m), Space: O(1) for limited character set.
- Current approach: simpler to understand but less efficient.
- For small inputs (typical constraint), performance difference is acceptable.
- Trade-off: code clarity vs. algorithmic efficiency.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  for char in words[0]:
      if all(char in word for word in words[1:]):
          result.append(char)
          words = [word.replace(char, '', 1) for word in words]
  ```

### How It Works

- Alternative efficient approach: use Counter to count character frequencies in each word, then find minimum frequency for each character across all words. Time: O(n × m), Space: O(1) for limited character set.
- Current approach: simpler to understand but less efficient.
- For small inputs (typical constraint), performance difference is acceptable.
- Trade-off: code clarity vs. algorithmic efficiency.

### Why Iteration Works

- Using first word as reference ensures only characters present there are considered.
- `all()` checks guarantee character exists in every word.
- Removing one occurrence (`.replace(char, '', 1)`) handles duplicate counting correctly.
- Each matched character is counted as many times as it appears in all words (minimum frequency).

Time complexity

- Let n = number of words, m = average length of words.
- For each character in first word (m iterations):
  - Check all other words: O(n × m) for `all()` check.
  - Replace in all words: O(n × m).
- Overall time complexity: O(m × n × m) = O(n × m²).

Space complexity

- Result list: O(m) for storing common characters.
- Modified words list: O(n × m) for creating new word copies after replacements.
- Overall space complexity: O(n × m).

Thought process and trade-offs

- Character-by-character approach: intuitive but not optimal for performance.
- Alternative efficient approach: use Counter to count character frequencies in each word, then find minimum frequency for each character across all words. Time: O(n × m), Space: O(1) for limited character set.
- Current approach: simpler to understand but less efficient.
- For small inputs (typical constraint), performance difference is acceptable.
- Trade-off: code clarity vs. algorithmic efficiency.

### Complexity Analysis

- **Time Complexity**: - Let n = number of words, m = average length of words. - For each character in first word (m iterations):   - Check all other words: O(n × m) for `all()` check.   - Replace in all words: O(n × m). - Overall time complexity: O(m × n × m) = O(n × m²). Space complexity - Result list: O(m) for storing common characters. - Modified words list: O(n × m) for creating new word copies after replacements. - Overall space complexity: O(n × m). Thought process and trade-offs - Character-by-character approach: intuitive but not optimal for performance. - Alternative efficient approach: use Counter to count character frequencies in each word, then find minimum frequency for each character across all words. Time: O(n × m), Space: O(1) for limited character set. - Current approach: simpler to understand but less efficient. - For small inputs (typical constraint), performance difference is acceptable. - Trade-off: code clarity vs. algorithmic efficiency.
- **Space Complexity**: - Result list: O(m) for storing common characters. - Modified words list: O(n × m) for creating new word copies after replacements. - Overall space complexity: O(n × m). Thought process and trade-offs - Character-by-character approach: intuitive but not optimal for performance. - Alternative efficient approach: use Counter to count character frequencies in each word, then find minimum frequency for each character across all words. Time: O(n × m), Space: O(1) for limited character set. - Current approach: simpler to understand but less efficient. - For small inputs (typical constraint), performance difference is acceptable. - Trade-off: code clarity vs. algorithmic efficiency.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
