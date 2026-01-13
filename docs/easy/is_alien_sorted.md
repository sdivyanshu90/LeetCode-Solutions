# Verifying an Alien Dictionary

## Problem Summary

- Given a sequence of words and an alien language's character order, determine if words are sorted lexicographically in that alien order.
- Example: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz" -> True.

Current implementation (in repository)

- Implementation maps alien order to indices:
  - Creates dictionary mapping each character to its position in alien alphabet.
  - Compares consecutive word pairs.
  - For each pair, compares character by character using the order map.
  - Returns False if earlier word is longer when prefix matches (e.g., "apple" before "app").
  - Returns False if character at same position violates alien order.
  - Returns True if all pairs pass validation.
- Example code:
  ```python
  order_map = {val: index for index, val in enumerate(order)}
  for i in range(len(words) - 1):
      for j in range(len(words[i])):
          if j >= len(words[i + 1]): return False  # word[i] longer
          if words[i][j] != words[i + 1][j]:
              if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
              break
  ```

Why this works

- Order map converts alien characters to comparable indices.
- Character-by-character comparison identifies first difference.
- If first word is longer than second when all compared characters match, order is invalid.
- Breaking on first difference avoids unnecessary comparisons.
- Checking all consecutive pairs ensures global sorted order.

Time complexity

- Let n = number of words, m = average word length.
- Building order map: O(26) = O(1).
- Comparing consecutive pairs: O(n) pairs.
- Each comparison: O(m) worst case.
- Overall time complexity: O(n × m).

Space complexity

- Order map: O(26) = O(1) for fixed alphabet size.
- Space complexity: O(1).

Thought process and trade-offs

- Order map approach: converts problem to standard lexicographic comparison.
- Alternative: create custom comparator function - same logic, different structure.
- Handles edge case: prefix relationship (shorter word must come first).
- Early termination on first difference: efficient.
- Could optimize by checking length before character comparison, but current approach is clear.

## Approach: Sorting (Implemented)

### Strategy

The solution uses sorting to solve the problem efficiently.

```python
  order_map = {val: index for index, val in enumerate(order)}
  for i in range(len(words) - 1):
      for j in range(len(words[i])):
          if j >= len(words[i + 1]): return False  # word[i] longer
          if words[i][j] != words[i + 1][j]:
              if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
              break
  ```

### How It Works

- Alternative: create custom comparator function - same logic, different structure.
- Handles edge case: prefix relationship (shorter word must come first).
- Early termination on first difference: efficient.
- Could optimize by checking length before character comparison, but current approach is clear.

### Why Sorting Works

- Order map converts alien characters to comparable indices.
- Character-by-character comparison identifies first difference.
- If first word is longer than second when all compared characters match, order is invalid.
- Breaking on first difference avoids unnecessary comparisons.
- Checking all consecutive pairs ensures global sorted order.

Time complexity

- Let n = number of words, m = average word length.
- Building order map: O(26) = O(1).
- Comparing consecutive pairs: O(n) pairs.
- Each comparison: O(m) worst case.
- Overall time complexity: O(n × m).

Space complexity

- Order map: O(26) = O(1) for fixed alphabet size.
- Space complexity: O(1).

Thought process and trade-offs

- Order map approach: converts problem to standard lexicographic comparison.
- Alternative: create custom comparator function - same logic, different structure.
- Handles edge case: prefix relationship (shorter word must come first).
- Early termination on first difference: efficient.
- Could optimize by checking length before character comparison, but current approach is clear.

### Complexity Analysis

- **Time Complexity**: - Let n = number of words, m = average word length. - Building order map: O(26) = O(1). - Comparing consecutive pairs: O(n) pairs. - Each comparison: O(m) worst case. - Overall time complexity: O(n × m). Space complexity - Order map: O(26) = O(1) for fixed alphabet size. - Space complexity: O(1). Thought process and trade-offs - Order map approach: converts problem to standard lexicographic comparison. - Alternative: create custom comparator function - same logic, different structure. - Handles edge case: prefix relationship (shorter word must come first). - Early termination on first difference: efficient. - Could optimize by checking length before character comparison, but current approach is clear.
- **Space Complexity**: - Order map: O(26) = O(1) for fixed alphabet size. - Space complexity: O(1). Thought process and trade-offs - Order map approach: converts problem to standard lexicographic comparison. - Alternative: create custom comparator function - same logic, different structure. - Handles edge case: prefix relationship (shorter word must come first). - Early termination on first difference: efficient. - Could optimize by checking length before character comparison, but current approach is clear.

### Advantages

- Efficient sorting solution
- Clear and maintainable code

### Disadvantages

- May require additional space
