# Set Mismatch

Problem summary

- Array nums should contain 1 to n but has one duplicate and one missing number.
- Return array [duplicate, missing].
- Example: [1,2,2,4] -> [2,3] (2 appears twice, 3 is missing).

Current implementation (in repository)

- Implementation uses mathematical approach:
  - Calculates expected sum: n × (n+1) / 2 (sum of 1 to n).
  - Calculates actual sum of array.
  - Finds sum of unique elements using set.
  - Duplicate = actual_sum - sum(set) (extra value added by duplication).
  - Missing = expected_sum - actual_sum + duplicate.
- Example code:
  ```python
  total_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  duplicate = actual_sum - sum(set(nums))
  missing = total_sum - actual_sum + duplicate
  ```

Why this works

- actual_sum includes duplicate value twice, so actual_sum - sum(set) isolates the duplicate.
- expected_sum - actual_sum gives (missing - duplicate).
- Adding duplicate back gives missing value.
- Mathematical properties ensure unique identification of both numbers.

Time complexity

- Let n = length of array.
- Calculating sums: O(n) for sum(nums) and sum(set(nums)).
- Creating set: O(n).
- Overall time complexity: O(n).

Space complexity

- Set stores unique elements: O(n) in worst case.
- Space complexity: O(n).

Thought process and trade-offs

- Mathematical approach: elegant and avoids modifying input.
- Alternative: mark visited elements by negating values at corresponding indices - O(1) space but modifies input.
- Alternative: sort array and find duplicate/missing by checking adjacent elements - O(n log n) time.
- Alternative: XOR-based approach - O(1) space, O(n) time, more complex to implement.
- Current approach: clear logic, acceptable O(n) space for most scenarios.
