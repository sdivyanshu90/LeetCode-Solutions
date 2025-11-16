# Two Sum

Problem summary

- Given an integer array `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
- Exactly one valid answer may exist. A number cannot be used twice (indices must be distinct).
- Return an empty list if no valid pair exists (the provided solution does this for robustness).

Approach used (single-pass hash map)

1. Iterate the array once, keeping a hash map `seen` that maps a value -> its index encountered so far.
2. For each element `num` at index `i`, compute `complement = target - num`.
3. Check if `complement` is already in `seen`.
   - If yes, a solution is found: return `[seen[complement], i]`.
   - Otherwise, store `seen[num] = i` and continue.
4. If iteration ends with no match, return `[]`.

Why this works

- The map stores previously seen numbers and their indices. If the complement of the current number was seen earlier, those two numbers sum to `target`.
- Because indices are stored for earlier occurrences only, returned indices are guaranteed to be distinct.

Time and space complexity

- Time complexity: O(n), where n = len(nums). Each element is visited once; map lookups and inserts are O(1) on average.
- Space complexity: O(n) worst-case for the hash map (when no pair is found or all elements are unique).

Correctness details and edge cases

- Duplicates: The solution handles duplicates correctly because the map stores the earliest index; when a duplicate forms a pair, the complement check will succeed.
  - Example: `nums = [3,3], target = 6` -> first 3 stored, second 3 finds complement 3 in map -> returns `[0,1]`.
- Single-element arrays: returns `[]` (no valid pair).
- No-solution arrays: returns `[]`.
- Large inputs: works efficiently for large arrays due to linear time and constant-average-time map ops.
- Negative numbers and zero: handled naturally by arithmetic and map checks.

Alternative approaches (trade-offs)

- Brute force (two nested loops): O(n^2) time, O(1) space — too slow for large n.
- Two-pass hashmap: first build map of value->index, then for each element check complement; still O(n) time but slightly more work or careful handling of duplicates is needed.
- Sorting-based two-pointer: O(n log n) time, but indices are lost unless additional bookkeeping is done — more complex to return original indices.

Thought process (concise)

- Goal: O(n) time and O(n) extra space acceptable.
- A map from value to index provides O(1) complement checks.
- Single-pass solution is simplest and minimizes operations (insert only when needed).

Example testcases (the same ones in tests)

1. [2,7,11,15], target=9 -> [0,1]
2. [-1,-2,-3,-4,-5], target=-8 -> [2,4]
3. [1,2,3,4,5], target=10 -> []
4. [1000000,5000000,7000000,2000000], target=12000000 -> [1,2]
5. [3,2,4,3], target=6 -> [0,3] or [1,2]
6. large range example -> finds pair near the end efficiently
7. [1], target=2 -> []
8. [1,1,1,1], target=2 -> [0,1]
9. [0,4,-4,3,2], target=0 -> [1,2]
10. [-7,1,5,-4], target=-3 -> [0,3]

Potential improvements

- Add explicit type and input validation if used outside contest/LeetCode environment.
- Return the first found pair as currently implemented; if multiple deterministic selection is required, adapt strategy (e.g., prefer smallest indices).
