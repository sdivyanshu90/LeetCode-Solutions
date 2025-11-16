# Count Bits

Problem summary

- Given a non-negative integer `n`, return an array `ans` of length `n + 1` where `ans[i]` is the number of 1 bits in the binary representation of `i` (0 ≤ i ≤ n).

Approach used (dynamic programming / bit relation)

- Observation: For any integer `i`, the number of set bits equals the number of set bits in `i // 2` plus `i % 2` (the least-significant bit).
- Using this recurrence yields a simple DP:
  - `bits_count[0] = 0`
  - For i from 1 to n: `bits_count[i] = bits_count[i // 2] + (i % 2)`
- This computes each entry in O(1) time using previously computed results.

Why this works (thought process)

- Right-shifting `i` (integer division by 2) removes the least-significant bit, so the count for `i` is the count for the shifted value plus 1 if the removed bit was 1.
- The recurrence leverages smaller subproblems to build results up to `n`.

Time and space complexity

- Time: O(n) — single pass filling an array of size `n + 1`, each step constant work.
- Space: O(n) — output array of size `n + 1`. Auxiliary extra space is O(1).

Edge cases

- n = 0 → returns [0].
- Large n: algorithm remains linear and uses integer arithmetic; Python handles large integers but memory for output grows linearly.
- Works for all non-negative integers.

Alternatives

- Built-in bit counting per number (e.g., bin(i).count('1')) — O(n log B) overall and slower due to string allocations.
- Using Brian Kernighan’s trick for each number — repeated loops per number, worse overall than DP.
- Leveraging highest-power-of-two or highest-bit approaches for slight micro-optimizations; complexity remains O(n).

Example

- n = 5 → [0,1,1,2,1,2]
- n = 2 → [0,1,1]

Implementation notes

- The DP formula is memory- and CPU-friendly and avoids per-number bit scanning.
- Use integer division `i // 2` and modulus `i % 2` for clarity; bit operators `i >> 1` and `i & 1` give the same result with slightly better micro performance.
