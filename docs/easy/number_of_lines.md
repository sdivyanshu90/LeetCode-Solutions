# Number of Lines To Write String

## Problem Summary

- Writing string to paper where each line fits 100 units width.
- Each character has a width given in array widths.
- Return [number of lines, width of last line].
- Example: widths (all 10), s="abcdefghij" -> [1, 100].

Current implementation (in repository)

- Implementation tracks line count and current line width:
  - Initializes line count to 1, current width to 0.
  - For each character, gets its width from array using ASCII offset.
  - If adding character exceeds 100, starts new line.
  - Otherwise adds to current line width.
  - Returns [line_count, current_width].
- Example code:
  ```python
  line = 1
  tot = 0
  for char in s:
      count = widths[ord(char) - ord('a')]
      if count + tot > 100:
          line += 1
          tot = count
      else:
          tot += count
  return [line, tot]
  ```

Why this works

- ord(char) - ord('a') maps 'a' to 0, 'b' to 1, etc., indexing widths array.
- Simulates line wrapping: when current line can't fit character, start new line.
- New line begins with current character (tot = count).
- Final state gives total lines and width of last line.

Time complexity

- Let n = length of string s.
- Process each character once: O(1) per character.
- Overall time complexity: O(n).

Space complexity

- Only using two variables (line, tot).
- Space complexity: O(1).

Thought process and trade-offs

- Simulation approach: straightforward modeling of paper writing process.
- ASCII arithmetic: standard technique for character-to-index mapping.
- Single pass: optimal, no preprocessing needed.
- Clear logic: easy to verify correctness.
- Edge cases: single character, exact 100 units, all handled naturally.

## Approach: String Manipulation (Implemented)

### Strategy

The solution uses string manipulation to solve the problem efficiently.

```python
  line = 1
  tot = 0
  for char in s:
      count = widths[ord(char) - ord('a')]
      if count + tot > 100:
          line += 1
          tot = count
      else:
          tot += count
  return [line, tot]
  ```

### How It Works

- ASCII arithmetic: standard technique for character-to-index mapping.
- Single pass: optimal, no preprocessing needed.
- Clear logic: easy to verify correctness.
- Edge cases: single character, exact 100 units, all handled naturally.

### Why String Manipulation Works

- ord(char) - ord('a') maps 'a' to 0, 'b' to 1, etc., indexing widths array.
- Simulates line wrapping: when current line can't fit character, start new line.
- New line begins with current character (tot = count).
- Final state gives total lines and width of last line.

Time complexity

- Let n = length of string s.
- Process each character once: O(1) per character.
- Overall time complexity: O(n).

Space complexity

- Only using two variables (line, tot).
- Space complexity: O(1).

Thought process and trade-offs

- Simulation approach: straightforward modeling of paper writing process.
- ASCII arithmetic: standard technique for character-to-index mapping.
- Single pass: optimal, no preprocessing needed.
- Clear logic: easy to verify correctness.
- Edge cases: single character, exact 100 units, all handled naturally.

### Complexity Analysis

- **Time Complexity**: - Let n = length of string s. - Process each character once: O(1) per character. - Overall time complexity: O(n). Space complexity - Only using two variables (line, tot). - Space complexity: O(1). Thought process and trade-offs - Simulation approach: straightforward modeling of paper writing process. - ASCII arithmetic: standard technique for character-to-index mapping. - Single pass: optimal, no preprocessing needed. - Clear logic: easy to verify correctness. - Edge cases: single character, exact 100 units, all handled naturally.
- **Space Complexity**: - Only using two variables (line, tot). - Space complexity: O(1). Thought process and trade-offs - Simulation approach: straightforward modeling of paper writing process. - ASCII arithmetic: standard technique for character-to-index mapping. - Single pass: optimal, no preprocessing needed. - Clear logic: easy to verify correctness. - Edge cases: single character, exact 100 units, all handled naturally.

### Advantages

- Efficient string manipulation solution
- Clear and maintainable code

### Disadvantages

- May require additional space
