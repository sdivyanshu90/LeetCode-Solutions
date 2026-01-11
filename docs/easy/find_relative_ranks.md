# Find Relative Ranks

## Problem Summary

- Given an array `score` of athlete scores, return an array of rankings where each athlete's ranking is displayed as:
  - "Gold Medal" for 1st place
  - "Silver Medal" for 2nd place
  - "Bronze Medal" for 3rd place
  - String representation of the rank (4th, 5th, etc.)
- The output array should be in the same order as the input (maintain original indices).

Approach (counting sort via index mapping)

- Find the maximum score in the array.
- Create a counting array `score_to_index` of size M+1 (where M = max score) to map each score to its original index.
  - `score_to_index[score[i]] = i + 1` (store 1-based index; 0 indicates absence).
- Iterate from the maximum score down to 0:
  - If a score exists at index i, retrieve its original index and assign the appropriate rank.
  - For top 3 places, assign medal names; for rank 4 and beyond, assign the rank as a string.
- Return the ranking array.

Why this works (thought process)

- Instead of sorting (O(n log n)), we use counting sort (O(n + M)).
- By iterating from max score downward, we naturally process scores in descending order (highest to lowest).
- The index mapping preserves the original positions while allowing us to rank scores without moving array elements.
- This is optimal when the score range is small relative to n.

Time and space complexity

- Time: O(n + M), where n = len(score) and M = max(score).
  - Finding max: O(n)
  - Building index map: O(n)
  - Ranking: O(M)
  - Overall: O(n + M)
- Space: O(M) for the `score_to_index` array. If M >> n, this could be inefficient (see alternatives).

Comparison with sorting approach

- Sorting approach: O(n log n) time, O(n) space for the sorted order.
- Counting sort approach: O(n + M) time, O(M) space.
- Use counting sort when M ≤ n log n (score range is small).
- Use sorting when M >> n (score range is very large).

Edge cases and robustness

- Single athlete → return ["Gold Medal"].
- All scores identical → all get the same ranking based on original order (handled naturally).
- Duplicate scores → each athlete retains their original index; tied athletes all get different ranks based on their first position encountered in descending iteration.
- Very large scores → space complexity becomes an issue if scores are in the billions. Consider sorting in that case.

Example testcases (from repository)

- [5, 4, 3, 2, 1] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
- [10, 3, 8, 9, 4] → ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
- [1, 2, 3, 4, 5] → ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]
- [100, 90, 90, 80] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4"]
- [50] → ["Gold Medal"]

Alternative approaches

- Sorting with indices: sort scores with original indices, then rank. O(n log n) time, O(n) space. Simpler to understand, better for large score ranges.
  ```python
  indexed_scores = [(score[i], i) for i in range(len(score))]
  indexed_scores.sort(reverse=True)
  result = [None] * len(score)
  for rank, (_, original_idx) in enumerate(indexed_scores, 1):
      if rank <= 3:
          result[original_idx] = MEDALS[rank - 1]
      else:
          result[original_idx] = str(rank)
  return result
  ```
- Using Counter + max: less efficient, doesn't leverage score range.

Thought process / design choices

- The current approach exploits the fact that scores are non-negative integers with a bounded range.
- It avoids expensive sorting and instead trades space for time.
- The helper method `find_max()` is simple; could use built-in `max()` for brevity.

Common pitfalls

- Off-by-one errors when mapping indices (store i+1, subtract 1 when retrieving).
- Forgetting to check if `score_to_index[i] != 0` (uninitialized entries are 0).
- Handling duplicates: the current approach assigns different ranks based on first encounter in descending order (which is correct for this problem).

Improvements / notes

- Replace the manual `find_max()` with `max(score)` for cleaner code.
- If scores can be negative or have a very wide range, use the sorting approach instead.
- If memory is tight and score range is huge, sorting is preferable.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  indexed_scores = [(score[i], i) for i in range(len(score))]
  indexed_scores.sort(reverse=True)
  result = [None] * len(score)
  for rank, (_, original_idx) in enumerate(indexed_scores, 1):
      if rank <= 3:
          result[original_idx] = MEDALS[rank - 1]
      else:
          result[original_idx] = str(rank)
  return result
  ```

### How It Works

Problem summary

- Given an array `score` of athlete scores, return an array of rankings where each athlete's ranking is displayed as:
  - "Gold Medal" for 1st place
  - "Silver Medal" for 2nd place
  - "Bronze Medal" for 3rd place
  - String representation of the rank (4th, 5th, etc.)
- The output array should be in the same order as the input (maintain original indices).

Approach (counting sort via index mapping)

- Find the maximum score in the array.
- Create a counting array `score_to_index` of size M+1 (where M = max score) to map each score to its original index.
  - `score_to_index[score[i]] = i + 1` (store 1-based index; 0 indicates absence).
- Iterate from the maximum score down to 0:
  - If a score exists at index i, retrieve its original index and assign the appropriate rank.
  - For top 3 places, assign medal names; for rank 4 and beyond, assign the rank as a string.
- Return the ranking array.

Why this works (thought process)

- Instead of sorting (O(n log n)), we use counting sort (O(n + M)).
- By iterating from max score downward, we naturally process scores in descending order (highest to lowest).
- The index mapping preserves the original positions while allowing us to rank scores without moving array elements.
- This is optimal when the score range is small relative to n.

Time and space complexity

- Time: O(n + M), where n = len(score) and M = max(score).
  - Finding max: O(n)
  - Building index map: O(n)
  - Ranking: O(M)
  - Overall: O(n + M)
- Space: O(M) for the `score_to_index` array. If M >> n, this could be inefficient (see alternatives).

Comparison with sorting approach

- Sorting approach: O(n log n) time, O(n) space for the sorted order.
- Counting sort approach: O(n + M) time, O(M) space.
- Use counting sort when M ≤ n log n (score range is small).
- Use sorting when M >> n (score range is very large).

Edge cases and robustness

- Single athlete → return ["Gold Medal"].
- All scores identical → all get the same ranking based on original order (handled naturally).
- Duplicate scores → each athlete retains their original index; tied athletes all get different ranks based on their first position encountered in descending iteration.
- Very large scores → space complexity becomes an issue if scores are in the billions. Consider sorting in that case.

Example testcases (from repository)

- [5, 4, 3, 2, 1] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
- [10, 3, 8, 9, 4] → ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
- [1, 2, 3, 4, 5] → ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]
- [100, 90, 90, 80] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4"]
- [50] → ["Gold Medal"]

Alternative approaches

- Sorting with indices: sort scores with original indices, then rank. O(n log n) time, O(n) space. Simpler to understand, better for large score ranges.
  ```python
  indexed_scores = [(score[i], i) for i in range(len(score))]
  indexed_scores.sort(reverse=True)
  result = [None] * len(score)
  for rank, (_, original_idx) in enumerate(indexed_scores, 1):
      if rank <= 3:
          result[original_idx] = MEDALS[rank - 1]
      else:
          result[original_idx] = str(rank)
  return result
  ```
- Using Counter + max: less efficient, doesn't leverage score range.

Thought process / design choices

- The current approach exploits the fact that scores are non-negative integers with a bounded range.
- It avoids expensive sorting and instead trades space for time.
- The helper method `find_max()` is simple; could use built-in `max()` for brevity.

Common pitfalls

- Off-by-one errors when mapping indices (store i+1, subtract 1 when retrieving).
- Forgetting to check if `score_to_index[i] != 0` (uninitialized entries are 0).
- Handling duplicates: the current approach assigns different ranks based on first encounter in descending order (which is correct for this problem).

Improvements / notes

- Replace the manual `find_max()` with `max(score)` for cleaner code.
- If scores can be negative or have a very wide range, use the sorting approach instead.
- If memory is tight and score range is huge, sorting is preferable.

### Why Iteration Works

- Instead of sorting (O(n log n)), we use counting sort (O(n + M)).
- By iterating from max score downward, we naturally process scores in descending order (highest to lowest).
- The index mapping preserves the original positions while allowing us to rank scores without moving array elements.
- This is optimal when the score range is small relative to n.

Time and space complexity

- Time: O(n + M), where n = len(score) and M = max(score).
  - Finding max: O(n)
  - Building index map: O(n)
  - Ranking: O(M)
  - Overall: O(n + M)
- Space: O(M) for the `score_to_index` array. If M >> n, this could be inefficient (see alternatives).

Comparison with sorting approach

- Sorting approach: O(n log n) time, O(n) space for the sorted order.
- Counting sort approach: O(n + M) time, O(M) space.
- Use counting sort when M ≤ n log n (score range is small).
- Use sorting when M >> n (score range is very large).

Edge cases and robustness

- Single athlete → return ["Gold Medal"].
- All scores identical → all get the same ranking based on original order (handled naturally).
- Duplicate scores → each athlete retains their original index; tied athletes all get different ranks based on their first position encountered in descending iteration.
- Very large scores → space complexity becomes an issue if scores are in the billions. Consider sorting in that case.

Example testcases (from repository)

- [5, 4, 3, 2, 1] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
- [10, 3, 8, 9, 4] → ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
- [1, 2, 3, 4, 5] → ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]
- [100, 90, 90, 80] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4"]
- [50] → ["Gold Medal"]

Alternative approaches

- Sorting with indices: sort scores with original indices, then rank. O(n log n) time, O(n) space. Simpler to understand, better for large score ranges.
  ```python
  indexed_scores = [(score[i], i) for i in range(len(score))]
  indexed_scores.sort(reverse=True)
  result = [None] * len(score)
  for rank, (_, original_idx) in enumerate(indexed_scores, 1):
      if rank <= 3:
          result[original_idx] = MEDALS[rank - 1]
      else:
          result[original_idx] = str(rank)
  return result
  ```
- Using Counter + max: less efficient, doesn't leverage score range.

Thought process / design choices

- The current approach exploits the fact that scores are non-negative integers with a bounded range.
- It avoids expensive sorting and instead trades space for time.
- The helper method `find_max()` is simple; could use built-in `max()` for brevity.

Common pitfalls

- Off-by-one errors when mapping indices (store i+1, subtract 1 when retrieving).
- Forgetting to check if `score_to_index[i] != 0` (uninitialized entries are 0).
- Handling duplicates: the current approach assigns different ranks based on first encounter in descending order (which is correct for this problem).

Improvements / notes

- Replace the manual `find_max()` with `max(score)` for cleaner code.
- If scores can be negative or have a very wide range, use the sorting approach instead.
- If memory is tight and score range is huge, sorting is preferable.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n + M), where n = len(score) and M = max(score).   - Finding max: O(n)   - Building index map: O(n)   - Ranking: O(M)   - Overall: O(n + M) - Space: O(M) for the `score_to_index` array. If M >> n, this could be inefficient (see alternatives). Comparison with sorting approach - Sorting approach: O(n log n) time, O(n) space for the sorted order. - Counting sort approach: O(n + M) time, O(M) space. - Use counting sort when M ≤ n log n (score range is small). - Use sorting when M >> n (score range is very large). Edge cases and robustness - Single athlete → return ["Gold Medal"]. - All scores identical → all get the same ranking based on original order (handled naturally). - Duplicate scores → each athlete retains their original index; tied athletes all get different ranks based on their first position encountered in descending iteration. - Very large scores → space complexity becomes an issue if scores are in the billions. Consider sorting in that case. Example testcases (from repository) - [5, 4, 3, 2, 1] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"] - [10, 3, 8, 9, 4] → ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"] - [1, 2, 3, 4, 5] → ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"] - [100, 90, 90, 80] → ["Gold Medal", "Silver Medal", "Bronze Medal", "4"] - [50] → ["Gold Medal"] Alternative approaches - Sorting with indices: sort scores with original indices, then rank. O(n log n) time, O(n) space. Simpler to understand, better for large score ranges.   ```python   indexed_scores = [(score[i], i) for i in range(len(score))]   indexed_scores.sort(reverse=True)   result = [None] * len(score)   for rank, (_, original_idx) in enumerate(indexed_scores, 1):       if rank <= 3:           result[original_idx] = MEDALS[rank - 1]       else:           result[original_idx] = str(rank)   return result   ``` - Using Counter + max: less efficient, doesn't leverage score range. Thought process / design choices - The current approach exploits the fact that scores are non-negative integers with a bounded range. - It avoids expensive sorting and instead trades space for time. - The helper method `find_max()` is simple; could use built-in `max()` for brevity. Common pitfalls - Off-by-one errors when mapping indices (store i+1, subtract 1 when retrieving). - Forgetting to check if `score_to_index[i] != 0` (uninitialized entries are 0). - Handling duplicates: the current approach assigns different ranks based on first encounter in descending order (which is correct for this problem). Improvements / notes - Replace the manual `find_max()` with `max(score)` for cleaner code. - If scores can be negative or have a very wide range, use the sorting approach instead. - If memory is tight and score range is huge, sorting is preferable.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
