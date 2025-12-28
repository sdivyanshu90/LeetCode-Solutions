# Jewels and Stones

Problem summary

- Given string jewels (types that are jewels) and string stones (stones you have).
- Count how many stones you have that are also jewels.
- Characters are case-sensitive: 'a' and 'A' are different types.
- Example: jewels = "aA", stones = "aAAbbbb" -> 3 (three A's and a's).

Current implementation (in repository)

- Implementation uses generator with membership check:
  - Iterates through each stone.
  - Checks if stone is in jewels string.
  - Uses sum with generator expression to count matches.
- Example code:
  ```python
  return sum(1 for stone in stones if stone in jewels)
  ```

Why this works

- Membership check `stone in jewels` returns True if stone is a jewel type.
- Generator expression `1 for stone in stones if...` produces 1 for each match.
- sum() aggregates all 1s to get total count.
- Case-sensitive string comparison handles 'a' vs 'A' correctly.

Time complexity

- Let n = len(stones), m = len(jewels).
- For each stone: check membership in jewels string is O(m).
- Overall time complexity: O(n × m).

Space complexity

- Generator expression: O(1) space (lazy evaluation).
- Space complexity: O(1).

Thought process and trade-offs

- One-liner solution: concise and Pythonic.
- Optimization: convert jewels to set for O(1) lookup - reduces to O(n) time.
- Example: `jewels_set = set(jewels); return sum(1 for stone in stones if stone in jewels_set)`.
- Current approach: simple but not optimal for large jewels string.
- For small inputs (typical constraint): difference negligible.
- Trade-off: code brevity vs. algorithmic efficiency.
