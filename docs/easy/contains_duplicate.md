# Contains Duplicate

Problem summary

- Given an integer array `nums`, determine if any value appears at least twice.
- Return `True` if any duplicate exists, otherwise `False`.

Approach used (set comparison)

- Convert the list to a set and compare lengths:
  - If `len(set(nums)) != len(nums)` then duplicates exist.
- This is concise and leverages Python's built-in set implementation for uniqueness.

Alternative (early-exit) approach

- Iterate through `nums` and maintain a seen set:
  - For each value, if it's already in `seen` return `True`.
  - Otherwise add it to `seen`.
  - Return `False` after the loop.
- This can exit early when a duplicate is found and avoids building the full set when duplicates are common.

Why this works

- A set stores unique elements; comparing sizes detects whether any collisions occurred.
- The streaming variant detects the first duplicate as soon as it appears.

Time and space complexity

- Time: O(n) average, where n = len(nums). Building or scanning the set requires linear work.
- Space: O(n) worst-case for the set of seen elements.

Trade-offs and thought process

- One-liner `len(set(nums)) != len(nums)` is clear and often fast for typical inputs.
- Use the streaming approach when you expect many duplicates early or want to avoid allocating a full set for very large inputs.
- For memory-constrained environments or where elements are huge, consider sorting in-place (O(n log n) time, O(1) extra space if allowed) and scanning adjacent pairs.

Edge cases

- Empty list -> `False`
- Single-element list -> `False`
- All elements identical -> `True`
- Negative numbers, zero, and large integers are handled naturally.

Example testcases (from repo)

- [1,2,3,1] -> True
- [1,2,3,4] -> False
- [] -> False
- [7,7,7,7] -> True

Recommended implementation (streaming, early-exit)

```python
def containsDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```
