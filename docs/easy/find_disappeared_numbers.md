# Find All Numbers Disappeared in an Array — Explanation, Approach, Complexity

Problem summary

- Given an array `nums` of n integers where 1 ≤ nums[i] ≤ n, find all integers in the range [1, n] that do not appear in the array.
- Return a list of missing numbers in sorted order.

Approach (set-based lookup)

- Create a set `set_nums` from the input array for O(1) average lookup.
- Iterate through all integers from 1 to n (length of array).
- For each integer i, check if it exists in the set.
  - If i is not in the set, append it to the result list.
- Return the result list.

Why this works (thought process)

- The range [1, n] is well-defined (exactly n possible values).
- Using a set provides constant-time membership checks.
- By iterating from 1 to n, we check every possible value and collect those missing.
- This approach is simple, readable, and efficient for typical input sizes.

Time and space complexity

- Time: O(n) — creating the set is O(n) and iterating through 1 to n is O(n).
- Space: O(n) for the set in the worst case (all n distinct values); O(k) for the result, where k = number of missing numbers.

Alternative approaches

- In-place marking (optimal space): use the array itself to mark visited numbers (negate value at index nums[i]-1). O(n) time, O(1) extra space.
  ```python
  for num in nums:
      index = abs(num) - 1
      nums[index] = -abs(nums[index])
  return [i + 1 for i in range(len(nums)) if nums[i] > 0]
  ```
- Hash set (current approach): straightforward and clear.
- Mathematical (sum approach): missing = (n\*(n+1)//2) - sum(nums), but only works when one element is missing and requires O(1) space. Doesn't extend well to multiple missing numbers.

Edge cases

- All numbers present: [1, 2, 3, ...] → return [] (no missing numbers).
- All numbers missing except one: [1] → return [2, 3, ..., n].
- Duplicates in input: handled naturally; set stores unique values only.
- Single element array: [1] → return [] or [n-1] depending on n.

Example testcases (from repository)

- [4,3,2,7,8,2,3,1] → [5, 6]
- [1,1] → [2]
- [2,2] → [1]
- [1,2,3,4,5] → []
- [5,4,3,2,1] → []

Proof of correctness

- By iterating through all values in [1, n] and checking membership in the set, we guarantee finding all and only the missing values.
- The iteration order (1 to n) ensures the result is naturally sorted.

Thought process / design choices

- Chose set-based approach for clarity and standard practice.
- If space is critical and in-place modification is allowed, use the marking approach.
- The current solution prioritizes readability over optimal space usage.

Notes

- The solution is straightforward and works well for most competitive programming contexts.
- For very large n, the in-place approach saves O(n) space.
- The result is naturally sorted because we iterate from 1 to n in order.
