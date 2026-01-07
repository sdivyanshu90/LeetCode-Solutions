# Count Binary Substrings

## Problem Summary

- Given a binary string s, count the number of substrings with equal consecutive 0's and 1's.
- Characters must be grouped (all 0's together, all 1's together).
- Example: "00110011" -> 6 substrings: "0011", "01", "1100", "10", "0011", "01".

Current implementation (in repository)

- Implementation groups consecutive same characters:
  - Creates array tracking length of each consecutive group of same characters.
  - Iterates through string comparing adjacent characters.
  - When character changes, starts new group; otherwise increments current group count.
  - For adjacent groups, minimum of their lengths gives number of valid substrings.
  - Sums all such counts.
- Example code:
  ```python
  groups = [1]
  for i in range(1, len(s)):
      if s[i - 1] != s[i]:
          groups.append(1)
      else:
          groups[-1] += 1
  res = sum(min(groups[i - 1], groups[i]) for i in range(1, len(groups)))
  ```

Why this works

- Valid substrings span exactly two adjacent groups (one of 0's, one of 1's).
- For adjacent groups of lengths a and b, min(a, b) valid substrings can be formed.
- Example: "000" and "11" can form "01" and "0011" (2 substrings = min(3, 2)).
- Summing over all adjacent pairs counts all valid substrings.

Time complexity

- Let n = length of string s.
- First pass to create groups: O(n).
- Number of groups k <= n.
- Summing adjacent pairs: O(k).
- Overall time complexity: O(n).

Space complexity

- Groups array: O(k) where k is number of groups, k <= n.
- Space complexity: O(n) worst case (alternating pattern like "010101").

Thought process and trade-offs

- Grouping approach: avoids checking every possible substring (which would be O(n²)).
- Key insight: only adjacent groups can form valid substrings.
- Alternative brute force: check all substrings - O(n²) time, much slower.
- Current approach is optimal: single pass to group, single pass to count.
- Space optimization possible: can calculate result while grouping (one pass, O(1) extra space), but current approach is clearer.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  groups = [1]
  for i in range(1, len(s)):
      if s[i - 1] != s[i]:
          groups.append(1)
      else:
          groups[-1] += 1
  res = sum(min(groups[i - 1], groups[i]) for i in range(1, len(groups)))
  ```

### How It Works

- Key insight: only adjacent groups can form valid substrings.
- Alternative brute force: check all substrings - O(n²) time, much slower.
- Current approach is optimal: single pass to group, single pass to count.
- Space optimization possible: can calculate result while grouping (one pass, O(1) extra space), but current approach is clearer.

### Why Iteration Works

- Valid substrings span exactly two adjacent groups (one of 0's, one of 1's).
- For adjacent groups of lengths a and b, min(a, b) valid substrings can be formed.
- Example: "000" and "11" can form "01" and "0011" (2 substrings = min(3, 2)).
- Summing over all adjacent pairs counts all valid substrings.

Time complexity

- Let n = length of string s.
- First pass to create groups: O(n).
- Number of groups k <= n.
- Summing adjacent pairs: O(k).
- Overall time complexity: O(n).

Space complexity

- Groups array: O(k) where k is number of groups, k <= n.
- Space complexity: O(n) worst case (alternating pattern like "010101").

Thought process and trade-offs

- Grouping approach: avoids checking every possible substring (which would be O(n²)).
- Key insight: only adjacent groups can form valid substrings.
- Alternative brute force: check all substrings - O(n²) time, much slower.
- Current approach is optimal: single pass to group, single pass to count.
- Space optimization possible: can calculate result while grouping (one pass, O(1) extra space), but current approach is clearer.

### Complexity Analysis

- **Time Complexity**: - Let n = length of string s. - First pass to create groups: O(n). - Number of groups k <= n. - Summing adjacent pairs: O(k). - Overall time complexity: O(n). Space complexity - Groups array: O(k) where k is number of groups, k <= n. - Space complexity: O(n) worst case (alternating pattern like "010101"). Thought process and trade-offs - Grouping approach: avoids checking every possible substring (which would be O(n²)). - Key insight: only adjacent groups can form valid substrings. - Alternative brute force: check all substrings - O(n²) time, much slower. - Current approach is optimal: single pass to group, single pass to count. - Space optimization possible: can calculate result while grouping (one pass, O(1) extra space), but current approach is clearer.
- **Space Complexity**: - Groups array: O(k) where k is number of groups, k <= n. - Space complexity: O(n) worst case (alternating pattern like "010101"). Thought process and trade-offs - Grouping approach: avoids checking every possible substring (which would be O(n²)). - Key insight: only adjacent groups can form valid substrings. - Alternative brute force: check all substrings - O(n²) time, much slower. - Current approach is optimal: single pass to group, single pass to count. - Space optimization possible: can calculate result while grouping (one pass, O(1) extra space), but current approach is clearer.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
