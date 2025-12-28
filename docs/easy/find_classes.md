# Classes More Than 5 Students

Problem summary

- Given a DataFrame `courses` with student enrollments, find classes with at least 5 students.
- Each row represents one student's enrollment in a class.
- Return DataFrame with class names that have 5 or more students.

Current implementation (in repository)

- Implementation uses value_counts and filtering:
  - Uses `value_counts()` on class column to count enrollments per class.
  - Filters counts where value >= 5.
  - Resets index to convert Series to DataFrame.
  - Selects only the class column for final result.
- Example code:
  ```python
  class_counts = courses['class'].value_counts()
  classes_more_than_5 = class_counts[class_counts >= 5].reset_index()
  return classes_more_than_5[['class']]
  ```

Why this works

- `value_counts()` aggregates and counts occurrences of each class.
- Boolean filtering `[class_counts >= 5]` selects only classes meeting criteria.
- `reset_index()` converts Series back to DataFrame with proper column structure.
- Column selection `[['class']]` ensures output has only required column.

Time complexity

- Let n = number of rows in DataFrame.
- `value_counts()`: O(n) for counting all rows.
- Filtering: O(k) where k is number of unique classes, k <= n.
- Overall time complexity: O(n).

Space complexity

- Series of class counts: O(k) where k is number of unique classes.
- Result DataFrame: O(m) where m is number of qualifying classes, m <= k.
- Overall space complexity: O(k).

Thought process and trade-offs

- Pandas built-in aggregation: efficient and readable.
- Alternative: groupby with count - similar performance, slightly more verbose.
- Alternative SQL: `SELECT class FROM courses GROUP BY class HAVING COUNT(*) >= 5`.
- Current approach leverages pandas strengths for data aggregation.
- Trade-off: pandas dependency required, but standard for DataFrame problems.
