# Intersection of Two Arrays — Explanation, Approach, Complexity

**Problem Summary**

- Given two integer arrays `nums1` and `nums2`, return an array of their intersection.
- Each element in the result must be unique (no duplicates).
- The order of elements in the result does not matter.
- Difference from "Intersection II": this problem requires unique elements only, while Intersection II preserves multiplicities.

**Approach Used (Set intersection)**

- Convert both arrays to sets and take the set intersection `set(nums1) & set(nums2)`.
- Convert the resulting set back to a list and return.
- This leverages Python's built-in set operations for clean, concise code.

Implementation:

```python
return list(set(nums1) & set(nums2))
```

**Why It Works**

- Sets automatically deduplicate elements, ensuring each value appears at most once.
- The set intersection operator `&` returns all elements present in both sets.
- Converting to a list satisfies the expected return type.

**Complexity**

- Let n = len(nums1), m = len(nums2).
- Time: O(n + m) average case — building both sets is linear; intersection is average O(min(n, m)) with hash-based sets.
- Space: O(n + m) for the two sets; output size is at most O(min(n, m)).

**Edge Cases**

- One or both arrays empty → return []
- No common elements → return []
- All elements common (with duplicates) → return unique values only
- Negative numbers and zeros → handled naturally by sets
- Single-element arrays → correctly identifies if they match

**Example Testcases (from repository)**

- [1,2,2,1], [2,2] → [2] (duplicates removed)
- [1,3,5], [2,4,6] → [] (no common elements)
- [1,2,3], [1,2,3] → [1,2,3] (all common, unique)
- [], [1,2,3] → [] (empty array)
- [1,1,1,2,2], [2,2,3,3] → [2] (only 2 is common)

**Alternative Approaches**

1. **Sort + two pointers:**

   ```python
   def intersection(self, nums1, nums2):
       nums1.sort()
       nums2.sort()
       i = j = 0
       result = []
       while i < len(nums1) and j < len(nums2):
           if nums1[i] < nums2[j]:
               i += 1
           elif nums1[i] > nums2[j]:
               j += 1
           else:
               if not result or result[-1] != nums1[i]:
                   result.append(nums1[i])
               i += 1
               j += 1
       return result
   ```

   - Time: O(n log n + m log m) for sorting
   - Space: O(1) extra (excluding output)
   - Better when input arrays are already sorted or when space is constrained

2. **Hash set with single scan:**
   - Build a set from the smaller array, scan the larger array checking membership.
   - Time: O(n + m), Space: O(min(n, m))

**Thought Process / Design Choices**

- The set-based approach is optimal for clarity and typical use cases.
- Python's built-in set intersection is highly optimized and readable.
- For very large inputs where one array is much smaller, consider building a set only from the smaller array.
- Result order is unspecified; if a specific order is needed, sort the output.

**Common Pitfalls**

- Forgetting to deduplicate → would return elements multiple times (use set or check before appending).
- Comparing values instead of using set operations → more verbose and error-prone.
- Assuming sorted output → the problem does not require sorted results unless specified.
