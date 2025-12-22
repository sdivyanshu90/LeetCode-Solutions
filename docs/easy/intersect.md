# Intersection of Two Arrays II — Explanation, Approach, Complexity

**Problem Summary**

- Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result should appear as many times as it shows in both arrays.
- Order of elements in the result does not matter.

**Approach Used (Frequency Counter intersection)**

- Build frequency maps for both arrays using `collections.Counter`.
- Take the counter intersection `Counter(nums1) & Counter(nums2)` which keeps the minimum count for each common key.
- Expand the resulting counter into a list by repeating each element by its intersected count.

Snippet (as implemented):

```python
from collections import Counter

x = Counter(nums1) & Counter(nums2)
result = []
for val, cnt in x.items():
		result.extend([val] * cnt)
return result
```

**Why It Works**

- The multiset intersection of two sequences requires taking the minimum frequency of each shared value.
- `Counter` supports `&` to compute exactly that: per-key minimum of counts.
- Expanding the counter reconstructs the intersection list with correct multiplicities.

**Complexity**

- Let n = len(nums1), m = len(nums2), and k = number of distinct values.
- Time: O(n + m + k) average — building both counters is linear; intersecting counters is O(k); expanding is proportional to the output size.
- Space: O(k) for the counters; output size up to O(min(n, m)).

**Edge Cases**

- One or both arrays empty → return []
- No common elements → return []
- All elements common → return the smaller array (by multiplicity)
- Negative numbers and zeros → handled naturally by counters
- Large arrays with overlapping ranges → performance remains linear

**Alternative Approaches**

- Sort + two pointers:
  - Sort both arrays and advance pointers to collect equal values.
  - Time O(n log n + m log m), Space O(1) extra (besides output).
- Hash map single-pass (optimize space when one array is much smaller):
  - Count the smaller array; iterate the larger, decrementing counts and appending when positive.
  - Time O(n + m), Space O(min(n, m)).

**Thought Process / Design Choices**

- Using `Counter` provides concise, correct multiset logic with minimal code.
- For very large inputs or memory constraints, prefer counting only the smaller array and scanning the larger to reduce space.
- Sorting + two pointers is a classic approach but less efficient due to sorting overhead.
