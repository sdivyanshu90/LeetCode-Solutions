# Find Max Consecutive Ones

## Problem Summary

- Given a binary array `nums` (containing only 0s and 1s), return the maximum number of consecutive 1s in the array.
- Example: [1, 1, 0, 1, 1, 1] → 3 (the longest run of 1s has length 3).

Approach (single-pass counting)

- Use two variables:
  - `count`: tracks the current consecutive 1s run length.
  - `res`: tracks the maximum run length seen so far.
- Iterate through the array:
  - If `num == 0`: update `res` with the maximum of current `res` and `count`, then reset `count = 0`.
  - If `num == 1`: increment `count`.
- After the loop, return `max(res, count)` to handle the case where the maximum run ends at the array's end.

Why this works (thought process)

- A 0 acts as a delimiter between runs of 1s.
- By tracking the current run length and updating the maximum whenever a 0 is encountered, we find the longest run.
- The final `max(res, count)` handles the edge case where the array ends with consecutive 1s (the last run is never terminated by a 0).

Time and space complexity

- Time: O(n), where n = len(nums). Single pass through the array with constant work per element.
- Space: O(1) — only a few integer variables used; no extra data structures.

Edge cases

- Empty array [] → return 0.
- All zeros [0, 0, 0] → return 0 (no 1s).
- All ones [1, 1, 1, 1] → return 4 (requires the final `max(res, count)` to capture the complete run).
- Single element: [1] → return 1, [0] → return 0.
- Alternating [1, 0, 1, 0] → return 1 (each 1 is isolated).

Example testcases (from repository)

- [1, 1, 0, 1, 1, 1] → 3
- [1, 0, 1, 1, 0, 1] → 2
- [0, 0, 0] → 0
- [1, 1, 1, 1, 1] → 5
- [] → 0

Alternative approaches

- Using split(): `return max(len(run) for run in ''.join(map(str, nums)).split('0')) if nums else 0`. Works but involves string conversion.
- Itertools groupby: group consecutive identical values, filter for 1s, find max length. More elegant but slightly more overhead.
- Regex: find all runs of 1s and return max length. Overkill for this problem.

Thought process / design choices

- The current approach is optimal: O(n) time and O(1) space.
- Simple, readable, and efficient; no unnecessary data structures.
- The final `max(res, count)` is crucial and easy to miss—handles the trailing run of 1s.

Common pitfalls

- Forgetting the final `max(res, count)` → would miss the maximum run if it ends at the array's end.
- Not initializing `res` to 0 → would fail on all-zero or empty arrays.
- Resetting `count` after every 1 instead of after encountering a 0 → would not accumulate consecutive 1s.

Notes

- This is a classic greedy/one-pass problem.
- If you need to return the indices of the maximum run, track the start and end positions during iteration.
- If you need all runs (not just the maximum), use the groupby or split approach.

## Approach: Greedy (Implemented)

### Strategy

The solution uses greedy to solve the problem efficiently.

### How It Works

Problem summary

- Given a binary array `nums` (containing only 0s and 1s), return the maximum number of consecutive 1s in the array.
- Example: [1, 1, 0, 1, 1, 1] → 3 (the longest run of 1s has length 3).

Approach (single-pass counting)

- Use two variables:
  - `count`: tracks the current consecutive 1s run length.
  - `res`: tracks the maximum run length seen so far.
- Iterate through the array:
  - If `num == 0`: update `res` with the maximum of current `res` and `count`, then reset `count = 0`.
  - If `num == 1`: increment `count`.
- After the loop, return `max(res, count)` to handle the case where the maximum run ends at the array's end.

Why this works (thought process)

- A 0 acts as a delimiter between runs of 1s.
- By tracking the current run length and updating the maximum whenever a 0 is encountered, we find the longest run.
- The final `max(res, count)` handles the edge case where the array ends with consecutive 1s (the last run is never terminated by a 0).

Time and space complexity

- Time: O(n), where n = len(nums). Single pass through the array with constant work per element.
- Space: O(1) — only a few integer variables used; no extra data structures.

Edge cases

- Empty array [] → return 0.
- All zeros [0, 0, 0] → return 0 (no 1s).
- All ones [1, 1, 1, 1] → return 4 (requires the final `max(res, count)` to capture the complete run).
- Single element: [1] → return 1, [0] → return 0.
- Alternating [1, 0, 1, 0] → return 1 (each 1 is isolated).

Example testcases (from repository)

- [1, 1, 0, 1, 1, 1] → 3
- [1, 0, 1, 1, 0, 1] → 2
- [0, 0, 0] → 0
- [1, 1, 1, 1, 1] → 5
- [] → 0

Alternative approaches

- Using split(): `return max(len(run) for run in ''.join(map(str, nums)).split('0')) if nums else 0`. Works but involves string conversion.
- Itertools groupby: group consecutive identical values, filter for 1s, find max length. More elegant but slightly more overhead.
- Regex: find all runs of 1s and return max length. Overkill for this problem.

Thought process / design choices

- The current approach is optimal: O(n) time and O(1) space.
- Simple, readable, and efficient; no unnecessary data structures.
- The final `max(res, count)` is crucial and easy to miss—handles the trailing run of 1s.

Common pitfalls

- Forgetting the final `max(res, count)` → would miss the maximum run if it ends at the array's end.
- Not initializing `res` to 0 → would fail on all-zero or empty arrays.
- Resetting `count` after every 1 instead of after encountering a 0 → would not accumulate consecutive 1s.

Notes

- This is a classic greedy/one-pass problem.
- If you need to return the indices of the maximum run, track the start and end positions during iteration.
- If you need all runs (not just the maximum), use the groupby or split approach.

### Why Greedy Works

- A 0 acts as a delimiter between runs of 1s.
- By tracking the current run length and updating the maximum whenever a 0 is encountered, we find the longest run.
- The final `max(res, count)` handles the edge case where the array ends with consecutive 1s (the last run is never terminated by a 0).

Time and space complexity

- Time: O(n), where n = len(nums). Single pass through the array with constant work per element.
- Space: O(1) — only a few integer variables used; no extra data structures.

Edge cases

- Empty array [] → return 0.
- All zeros [0, 0, 0] → return 0 (no 1s).
- All ones [1, 1, 1, 1] → return 4 (requires the final `max(res, count)` to capture the complete run).
- Single element: [1] → return 1, [0] → return 0.
- Alternating [1, 0, 1, 0] → return 1 (each 1 is isolated).

Example testcases (from repository)

- [1, 1, 0, 1, 1, 1] → 3
- [1, 0, 1, 1, 0, 1] → 2
- [0, 0, 0] → 0
- [1, 1, 1, 1, 1] → 5
- [] → 0

Alternative approaches

- Using split(): `return max(len(run) for run in ''.join(map(str, nums)).split('0')) if nums else 0`. Works but involves string conversion.
- Itertools groupby: group consecutive identical values, filter for 1s, find max length. More elegant but slightly more overhead.
- Regex: find all runs of 1s and return max length. Overkill for this problem.

Thought process / design choices

- The current approach is optimal: O(n) time and O(1) space.
- Simple, readable, and efficient; no unnecessary data structures.
- The final `max(res, count)` is crucial and easy to miss—handles the trailing run of 1s.

Common pitfalls

- Forgetting the final `max(res, count)` → would miss the maximum run if it ends at the array's end.
- Not initializing `res` to 0 → would fail on all-zero or empty arrays.
- Resetting `count` after every 1 instead of after encountering a 0 → would not accumulate consecutive 1s.

Notes

- This is a classic greedy/one-pass problem.
- If you need to return the indices of the maximum run, track the start and end positions during iteration.
- If you need all runs (not just the maximum), use the groupby or split approach.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n), where n = len(nums). Single pass through the array with constant work per element. - Space: O(1) — only a few integer variables used; no extra data structures. Edge cases - Empty array [] → return 0. - All zeros [0, 0, 0] → return 0 (no 1s). - All ones [1, 1, 1, 1] → return 4 (requires the final `max(res, count)` to capture the complete run). - Single element: [1] → return 1, [0] → return 0. - Alternating [1, 0, 1, 0] → return 1 (each 1 is isolated). Example testcases (from repository) - [1, 1, 0, 1, 1, 1] → 3 - [1, 0, 1, 1, 0, 1] → 2 - [0, 0, 0] → 0 - [1, 1, 1, 1, 1] → 5 - [] → 0 Alternative approaches - Using split(): `return max(len(run) for run in ''.join(map(str, nums)).split('0')) if nums else 0`. Works but involves string conversion. - Itertools groupby: group consecutive identical values, filter for 1s, find max length. More elegant but slightly more overhead. - Regex: find all runs of 1s and return max length. Overkill for this problem. Thought process / design choices - The current approach is optimal: O(n) time and O(1) space. - Simple, readable, and efficient; no unnecessary data structures. - The final `max(res, count)` is crucial and easy to miss—handles the trailing run of 1s. Common pitfalls - Forgetting the final `max(res, count)` → would miss the maximum run if it ends at the array's end. - Not initializing `res` to 0 → would fail on all-zero or empty arrays. - Resetting `count` after every 1 instead of after encountering a 0 → would not accumulate consecutive 1s. Notes - This is a classic greedy/one-pass problem. - If you need to return the indices of the maximum run, track the start and end positions during iteration. - If you need all runs (not just the maximum), use the groupby or split approach.

### Advantages

- Efficient greedy solution
- Clear and maintainable code

### Disadvantages

- May require additional space
