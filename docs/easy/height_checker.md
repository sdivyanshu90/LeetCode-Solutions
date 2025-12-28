# Height Checker

Problem summary

- Given an array heights, count how many indices have different values compared to the sorted version.
- Example: [1,1,4,2,1,3] -> sorted is [1,1,1,2,3,4] -> indices 2,4,5 differ -> return 3.

Current implementation (in repository)

- Implementation uses custom radix sort:
  - Creates copy of heights array.
  - Applies radix sort to the copy.
  - Compares original with sorted version element by element.
  - Counts positions where values differ.
  - Returns the count.
- Example code:
  ```python
  sorted_heights = heights[:]
  self.radix_sort(sorted_heights)
  count = sum(1 for i in range(len(heights)) if heights[i] != sorted_heights[i])
  ```

Why this works

- Sorted array represents expected heights in non-decreasing order.
- Comparing index by index counts students in wrong positions.
- Radix sort correctly sorts the array for comparison.
- Copy preserves original array for comparison.

Time complexity

- Let n = number of heights, k = number of digits in max height.
- Radix sort: O(n × k) where k is typically small (constant for reasonable heights).
- Comparison: O(n).
- Overall time complexity: O(n × k) ≈ O(n) for bounded integers.

Space complexity

- Sorted copy of array: O(n).
- Radix sort buckets: O(10) = O(1) for decimal digits.
- Overall space complexity: O(n).

Thought process and trade-offs

- Radix sort implementation: demonstrates understanding of sorting algorithms beyond built-ins.
- For practical purposes, using Python's built-in sort (Timsort) would be simpler: `sorted_heights = sorted(heights)`.
- Built-in sort: O(n log n) time, much simpler code.
- Current approach: educational but unnecessarily complex for this problem.
- Trade-off: algorithmic demonstration vs. practical simplicity.
