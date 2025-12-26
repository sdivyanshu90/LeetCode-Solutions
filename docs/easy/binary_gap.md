# Binary Gap

Problem summary

- Given a positive integer n, find the longest distance between any two consecutive 1's in its binary representation.
- If there are no two consecutive 1's, return 0.
- Example: n = 22 (binary: 10110) -> distance between positions 1 and 2 is 1, between 2 and 4 is 2, so return 2.

Current implementation (in repository)

- Implementation converts to binary string and finds indices:
  - Converts n to binary string using `bin(n)[2:]` (removing '0b' prefix).
  - Collects all indices where '1' appears in the binary string.
  - Iterates through consecutive pairs of indices to find maximum distance.
  - Returns the maximum gap found.
- Example code:
  ```python
  bin_n = bin(n)[2:]
  for i in range(len(bin_n)):
      if bin_n[i] == "1":
          idx.append(i)
  res = max(res, idx[i] - idx[i - 1])
  ```

Why this works

- Binary string representation makes it easy to identify '1' positions.
- Storing indices of all '1's allows computing distances between consecutive ones.
- Maximum of all consecutive gaps gives the longest binary gap.
- If fewer than 2 ones exist, the loop doesn't execute and returns 0.

Time complexity

- Let m = number of bits in n (approximately log₂(n)).
- Converting to binary: O(m).
- Finding '1' indices: O(m) for scanning the binary string.
- Computing max gap: O(k) where k is the number of '1's, k <= m.
- Overall time complexity: O(m) = O(log n).

Space complexity

- Binary string: O(m) = O(log n).
- Indices array: O(k) where k is the number of '1's.
- Overall space complexity: O(log n).

Thought process and trade-offs

- String-based approach: simple and readable, leverages Python's built-in binary conversion.
- Alternative bitwise approach (commented in code): processes bits directly using bit manipulation, slightly more efficient in space but less readable.
- Trade-off: string approach is clearer for understanding the problem, while bitwise is more "low-level" efficient.
- For typical integer sizes, both approaches are fast enough.
