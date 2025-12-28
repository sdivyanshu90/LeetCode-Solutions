# Longest Harmonious Subsequence

Problem summary

- Given an integer array, find the length of the longest harmonious subsequence.
- A harmonious subsequence has max value - min value = exactly 1.
- Example: [1,3,2,2,5,2,3,7] -> [3,2,2,2,3] has length 5 (max=3, min=2, diff=1).

Current implementation (in repository)

- Implementation uses Counter to track frequencies:
  - Counts frequency of each value using Counter.
  - Returns 0 if only one unique value (no harmonious subsequence possible).
  - For each value, checks if value-1 exists in counter.
  - If yes, adds their frequencies (both values differ by 1).
  - Returns maximum sum found.
- Example code:
  ```python
  freq = Counter(nums)
  for val, key in freq.items():
      if val - 1 in freq:
          res = max(res, key + freq[val - 1])
  ```

Why this works

- Harmonious subsequence with difference 1 contains only two distinct values: x and x+1.
- Count of elements in such subsequence = freq[x] + freq[x+1].
- Checking val-1 instead of val+1 avoids double counting (each pair checked once).
- Counter provides O(1) lookup for checking if adjacent value exists.

Time complexity

- Let n = length of array.
- Building Counter: O(n).
- Iterating through unique values: O(k) where k is number of unique values, k <= n.
- Overall time complexity: O(n).

Space complexity

- Counter stores k unique values and their frequencies.
- Space complexity: O(k) where k <= n.

Thought process and trade-offs

- Frequency-based approach: avoids checking all possible subsequences.
- Key insight: only need to consider pairs of adjacent values (x, x+1).
- Alternative: sort array and use sliding window - O(n log n) time.
- Current approach: optimal O(n) time with O(n) space.
- Edge cases: single unique value returns 0 (no pair possible), empty array returns 0.
