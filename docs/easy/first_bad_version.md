# First Bad Version — Explanation, Approach, Complexity

Problem summary

- You are a product manager with n versions. Each version is either good or bad.
- There is exactly one version that is the first bad version; all versions after it are also bad.
- Given an API `isBadVersion(version)` that returns True if the version is bad, find the first bad version number.

Approach (binary search)

- Use binary search on the range [1, n] to find the boundary where versions transition from good to bad.
- Initialize `left = 1, right = n`.
- While `left < right`:
  - Compute `mid = left + (right - left) // 2` (avoids integer overflow).
  - If `isBadVersion(mid)` is False (good version), search the right half: `left = mid + 1`.
  - If `isBadVersion(mid)` is True (bad version), search the left half (including mid): `right = mid`.
- Return `left` when the loop exits (this is the first bad version).

Why this works (thought process)

- The problem exhibits a monotonic property: all versions before the first bad version are good, and all versions after are bad.
- Binary search exploits this monotonicity to efficiently narrow down the search space.
- The condition `left < right` ensures we exit when left and right converge, pointing to the first bad version.
- The formula `mid = left + (right - left) // 2` prevents integer overflow (compared to `(left + right) // 2`).

Time and space complexity

- Time: O(log n) — at each step we halve the search range. Maximum iterations = log₂(n).
- Space: O(1) — only a few integer variables used; the recursion is iterative.

Why binary search over linear search

- Linear search: O(n) time — calls isBadVersion() up to n times. Inefficient for large n.
- Binary search: O(log n) time — calls isBadVersion() only ~log n times. Much faster.
- Example: n = 2 billion → binary search requires ~30 calls; linear search would require up to 2 billion.

Edge cases and robustness

- n = 1 → only one version; if bad, return 1.
- First version is bad (bad_version = 1) → binary search finds it immediately.
- Last version is bad (bad_version = n) → binary search finds it correctly.
- All versions are bad except the first → finds version 2 correctly.
- Very large n (up to 2^31 - 1) → `left + (right - left) // 2` avoids overflow; Python handles big integers anyway.

Example testcases (from repository)

- n = 5, first_bad = 4 → output: 4
- n = 50, first_bad = 50 → output: 50 (last version)
- n = 100, first_bad = 1 → output: 1 (first version)
- n = 2, first_bad = 2 → output: 2
- n = 2, first_bad = 1 → output: 1
- n = 1, first_bad = 1 → output: 1
- n = 13, first_bad = 8 → output: 8
- n = 20, first_bad = 10 → output: 10
- n = 2126753390, first_bad = 1702766719 → output: 1702766719 (large numbers test)

Loop invariant

- At each iteration:
  - All versions in [1, left-1] are known to be good.
  - All versions in [right, n] are known to be bad (or include the first bad).
  - The answer lies in [left, right].
- When `left == right`, we've found the first bad version.

Key insight: `left` and `right` movement

- If `mid` is good: we know [1, mid] are all good, so move left = mid + 1.
- If `mid` is bad: we don't know if mid is the first bad or if there's an earlier one, so include mid in the search: right = mid.
- This ensures left never skips over the first bad version.

Thought process / design choices

- Binary search is the standard and optimal approach for this problem.
- Iterative is preferred over recursive to avoid stack overflow for large n.
- The formula `left + (right - left) // 2` is a best practice to prevent overflow.

Common pitfalls

- Using `(left + right) // 2` instead of `left + (right - left) // 2` → can overflow (though Python integers are arbitrary precision).
- Using `left <= right` instead of `left < right` → may cause infinite loop or incorrect termination.
- Confusing when to update left vs. right → remember: if bad, we narrow to the left (keep mid); if good, narrow to the right (exclude mid).
- Returning `right` instead of `left` → both converge to the same value, but left is conventional.

Notes

- This is a classic "find the boundary" binary search problem.
- The approach generalizes to other monotonic search problems (e.g., find the first occurrence of a target).
- The solution is optimal in terms of time complexity; no faster algorithm exists for this problem.
