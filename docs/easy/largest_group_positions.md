# Positions of Large Groups

Problem summary

- Given a string, find start and end indices of each large group.
- Large group: consecutive characters of same kind with length >= 3.
- Return list of [start, end] indices.
- Example: "abbxxxxzzy" -> [[3,6]] (group of 'x' from index 3 to 6).

Current implementation (in repository)

- Implementation tracks group boundaries:
  - Maintains pointer i marking start of current group.
  - Iterates with pointer j through string.
  - When character changes or reaches end, checks if group size >= 3.
  - If yes, adds [i, j] to result.
  - Updates i to start of next group.
- Example code:
  ```python
  for j in range(len(s)):
      if j == len(s) - 1 or s[j] != s[j + 1]:
          if j - i + 1 >= 3:
              res.append([i, j])
          i = j + 1
  ```

Why this works

- Two pointers track current group: i (start) and j (current position).
- Detecting group end: character changes or string ends.
- Group length: j - i + 1 (inclusive indices).
- Checking length >= 3 filters for large groups.
- Updating i to j + 1 starts tracking next group.

Time complexity

- Let n = length of string.
- Single pass through string: O(n).
- Each position processed once.
- Overall time complexity: O(n).

Space complexity

- Result list stores at most k groups where k <= n/3.
- Space complexity: O(k) = O(n) worst case.

Thought process and trade-offs

- Two-pointer approach: efficient single-pass solution.
- Combined condition `j == len(s) - 1 or s[j] != s[j + 1]` handles both end of string and character change elegantly.
- Alternative: separate loops for each group - more complex logic.
- Current approach: clean and optimal.
- No preprocessing needed: direct string traversal.
