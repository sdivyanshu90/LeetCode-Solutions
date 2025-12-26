# Student Attendance Record I

Problem summary

- Given a string s representing a student's attendance record.
- Characters: 'A' (absent), 'L' (late), 'P' (present).
- Return true if student is eligible for award: less than 2 absences AND no 3 or more consecutive lates.
- Example: "PPALLP" -> True, "PPALLL" -> False (3 consecutive lates).

Current implementation (in repository)

- Implementation uses simple string operations:
  - Counts total 'A' occurrences using `.count('A')` and checks if less than 2.
  - Checks if substring "LLL" exists in the string.
  - Returns True only if both conditions are satisfied (< 2 absences and no "LLL").
- Example code:
  ```python
  return s.count('A') < 2 and 'LLL' not in s
  ```

Why this works

- `.count('A')` efficiently counts all absence occurrences.
- 'LLL' substring check directly identifies 3 or more consecutive lates.
- AND operator ensures both conditions must be true for eligibility.
- Concise one-liner leverages Python's string methods.

Time complexity

- Let n = length of string s.
- Counting 'A': O(n) for scanning entire string.
- Substring search for 'LLL': O(n) worst case.
- Overall time complexity: O(n).

Space complexity

- No additional data structures created.
- Space complexity: O(1).

Thought process and trade-offs

- String method approach: extremely readable and concise.
- Alternative: single-pass with counters - track absence count and consecutive late count while iterating. Same O(n) time but single pass instead of two.
- Current approach: prioritizes readability and simplicity over micro-optimization.
- For typical attendance record lengths, two passes have negligible performance impact.
- Trade-off: clarity and maintainability vs. theoretical single-pass efficiency.
