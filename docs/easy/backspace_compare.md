# Backspace String Compare

## Problem Summary

- Given two strings s and t, return true if they are equal when both are typed into empty text editors.
- '#' represents a backspace character that deletes the previous character.
- Example: "ab#c" becomes "ac", "ad#c" becomes "ac" -> True.

Current implementation (in repository)

- Implementation uses a stack-based approach:
  - Defines a helper function that processes each string.
  - For each character, if it's '#', pops from the stack (removing previous character).
  - If it's not '#', pushes the character onto the stack.
  - Uses try-except to handle popping from empty stack (when '#' appears without preceding characters).
  - Compares the final strings formed from both stacks.
- Example code:
  ```python
  def helper(s) -> str:
      ls = []
      for l in s:
          if l == '#':
              ls.pop()
          else:
              ls.append(l)
  ```

Why this works

- Stack naturally models the text editor behavior: adding characters and removing with backspace.
- Processing left to right simulates typing in order.
- '#' triggers pop operation which removes the most recently added character.
- Empty stack handling (try-except) correctly handles backspaces with no characters to delete.
- Final comparison of processed strings determines if they're equal.

Time complexity

- Let n = len(s), m = len(t).
- Processing s: O(n) for iterating and stack operations (each append/pop is O(1)).
- Processing t: O(m) similarly.
- String comparison: O(min(n, m)) for final comparison.
- Overall time complexity: O(n + m).

Space complexity

- Stack for s: O(n) in worst case (no backspaces).
- Stack for t: O(m) in worst case.
- Overall space complexity: O(n + m).

Thought process and trade-offs

- Stack approach: intuitive and straightforward simulation of the problem.
- Alternative O(1) space approach: use two pointers from the end of both strings, counting backspaces and comparing characters. More complex but space-efficient.
- Current approach prioritizes readability and simplicity.
- Try-except for empty stack: Pythonic error handling, though checking stack emptiness before popping would be more explicit.

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
  def helper(s) -> str:
      ls = []
      for l in s:
          if l == '#':
              ls.pop()
          else:
              ls.append(l)
  ```

### How It Works

- Defines a helper function that processes each string.
  - For each character, if it's '#', pops from the stack (removing previous character).
  - If it's not '#', pushes the character onto the stack.
  - Uses try-except to handle popping from empty stack (when '#' appears without preceding characters).
  - Compares the final strings formed from both stacks.
- Example code:
  ```python
  def helper(s) -> str:
      ls = []
      for l in s:
          if l == '#':
              ls.pop()
          else:
              ls.append(l)
  ```

Why this works

- Stack naturally models the text editor behavior: adding characters and removing with backspace.
- Processing left to right simulates typing in order.
- '#' triggers pop operation which removes the most recently added character.
- Empty stack handling (try-except) correctly handles backspaces with no characters to delete.
- Final comparison of processed strings determines if they're equal.

Time complexity

- Let n = len(s), m = len(t).
- Processing s: O(n) for iterating and stack operations (each append/pop is O(1)).
- Processing t: O(m) similarly.
- String comparison: O(min(n, m)) for final comparison.
- Overall time complexity: O(n + m).

Space complexity

- Stack for s: O(n) in worst case (no backspaces).
- Stack for t: O(m) in worst case.
- Overall space complexity: O(n + m).

Thought process and trade-offs

- Stack approach: intuitive and straightforward simulation of the problem.
- Alternative O(1) space approach: use two pointers from the end of both strings, counting backspaces and comparing characters. More complex but space-efficient.
- Current approach prioritizes readability and simplicity.
- Try-except for empty stack: Pythonic error handling, though checking stack emptiness before popping would be more explicit.

### Why Two Pointers Works

- Stack naturally models the text editor behavior: adding characters and removing with backspace.
- Processing left to right simulates typing in order.
- '#' triggers pop operation which removes the most recently added character.
- Empty stack handling (try-except) correctly handles backspaces with no characters to delete.
- Final comparison of processed strings determines if they're equal.

Time complexity

- Let n = len(s), m = len(t).
- Processing s: O(n) for iterating and stack operations (each append/pop is O(1)).
- Processing t: O(m) similarly.
- String comparison: O(min(n, m)) for final comparison.
- Overall time complexity: O(n + m).

Space complexity

- Stack for s: O(n) in worst case (no backspaces).
- Stack for t: O(m) in worst case.
- Overall space complexity: O(n + m).

Thought process and trade-offs

- Stack approach: intuitive and straightforward simulation of the problem.
- Alternative O(1) space approach: use two pointers from the end of both strings, counting backspaces and comparing characters. More complex but space-efficient.
- Current approach prioritizes readability and simplicity.
- Try-except for empty stack: Pythonic error handling, though checking stack emptiness before popping would be more explicit.

### Complexity Analysis

- **Time Complexity**: - Let n = len(s), m = len(t). - Processing s: O(n) for iterating and stack operations (each append/pop is O(1)). - Processing t: O(m) similarly. - String comparison: O(min(n, m)) for final comparison. - Overall time complexity: O(n + m). Space complexity - Stack for s: O(n) in worst case (no backspaces). - Stack for t: O(m) in worst case. - Overall space complexity: O(n + m). Thought process and trade-offs - Stack approach: intuitive and straightforward simulation of the problem. - Alternative O(1) space approach: use two pointers from the end of both strings, counting backspaces and comparing characters. More complex but space-efficient. - Current approach prioritizes readability and simplicity. - Try-except for empty stack: Pythonic error handling, though checking stack emptiness before popping would be more explicit.
- **Space Complexity**: - Stack for s: O(n) in worst case (no backspaces). - Stack for t: O(m) in worst case. - Overall space complexity: O(n + m). Thought process and trade-offs - Stack approach: intuitive and straightforward simulation of the problem. - Alternative O(1) space approach: use two pointers from the end of both strings, counting backspaces and comparing characters. More complex but space-efficient. - Current approach prioritizes readability and simplicity. - Try-except for empty stack: Pythonic error handling, though checking stack emptiness before popping would be more explicit.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
