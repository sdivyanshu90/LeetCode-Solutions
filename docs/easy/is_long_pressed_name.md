# Long Pressed Name

## Problem Summary

- Given two strings name and typed, return true if typed could be name with some characters long-pressed.
- Long-press: accidentally typing a character multiple times.
- Example: name = "alex", typed = "aaleex" -> True (a and e long-pressed).

Current implementation (in repository)

- Implementation uses two-pointer technique:
  - Pointers i for name, j for typed.
  - Iterates through typed string.
  - If characters match, advance both pointers.
  - If no match, check if it's a repeated character from previous typed character.
  - If neither condition met, return False.
  - At end, check if all of name was consumed.
- Example code:
  ```python
  while j < len(typed):
      if i < len(name) and name[i] == typed[j]:
          i += 1
      elif j == 0 or typed[j] != typed[j - 1]:
          return False
      j += 1
  return i == len(name)
  ```

Why this works

- Two pointers track progress through both strings.
- Matching characters advance both (normal typing).
- Extra characters in typed must match previous typed character (long-press).
- First character of typed can't be extra (j == 0 check).
- Final check ensures all of name was matched (no missing characters).

Time complexity

- Let n = len(name), m = len(typed).
- Single pass through typed: O(m).
- Each operation is O(1).
- Overall time complexity: O(m).

Space complexity

- Only using two pointer variables.
- Space complexity: O(1).

Thought process and trade-offs

- Two-pointer approach: optimal for string matching problems.
- Handles edge cases: empty strings, first character, mismatches.
- Alternative: group consecutive characters and compare groups - more complex, same complexity.
- Current approach: simple and efficient.
- Note: `typed[j] != typed[j - 1]` ensures extra character is actually a long-press repetition.

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
  while j < len(typed):
      if i < len(name) and name[i] == typed[j]:
          i += 1
      elif j == 0 or typed[j] != typed[j - 1]:
          return False
      j += 1
  return i == len(name)
  ```

### How It Works

- Handles edge cases: empty strings, first character, mismatches.
- Alternative: group consecutive characters and compare groups - more complex, same complexity.
- Current approach: simple and efficient.
- Note: `typed[j] != typed[j - 1]` ensures extra character is actually a long-press repetition.

### Why Two Pointers Works

- Two pointers track progress through both strings.
- Matching characters advance both (normal typing).
- Extra characters in typed must match previous typed character (long-press).
- First character of typed can't be extra (j == 0 check).
- Final check ensures all of name was matched (no missing characters).

Time complexity

- Let n = len(name), m = len(typed).
- Single pass through typed: O(m).
- Each operation is O(1).
- Overall time complexity: O(m).

Space complexity

- Only using two pointer variables.
- Space complexity: O(1).

Thought process and trade-offs

- Two-pointer approach: optimal for string matching problems.
- Handles edge cases: empty strings, first character, mismatches.
- Alternative: group consecutive characters and compare groups - more complex, same complexity.
- Current approach: simple and efficient.
- Note: `typed[j] != typed[j - 1]` ensures extra character is actually a long-press repetition.

### Complexity Analysis

- **Time Complexity**: - Let n = len(name), m = len(typed). - Single pass through typed: O(m). - Each operation is O(1). - Overall time complexity: O(m). Space complexity - Only using two pointer variables. - Space complexity: O(1). Thought process and trade-offs - Two-pointer approach: optimal for string matching problems. - Handles edge cases: empty strings, first character, mismatches. - Alternative: group consecutive characters and compare groups - more complex, same complexity. - Current approach: simple and efficient. - Note: `typed[j] != typed[j - 1]` ensures extra character is actually a long-press repetition.
- **Space Complexity**: - Only using two pointer variables. - Space complexity: O(1). Thought process and trade-offs - Two-pointer approach: optimal for string matching problems. - Handles edge cases: empty strings, first character, mismatches. - Alternative: group consecutive characters and compare groups - more complex, same complexity. - Current approach: simple and efficient. - Note: `typed[j] != typed[j - 1]` ensures extra character is actually a long-press repetition.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
