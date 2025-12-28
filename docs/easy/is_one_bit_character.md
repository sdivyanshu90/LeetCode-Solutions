# 1-bit and 2-bit Characters

Problem summary

- Given binary array where last element is 0, determine if last character is a one-bit character.
- One-bit character: represented by 0.
- Two-bit character: represented by 10 or 11.
- Example: [1,0,0] -> True (10 followed by 0).

Current implementation (in repository)

- Implementation counts consecutive 1's before the last 0:
  - Starts from second-to-last position (index len-2).
  - Counts consecutive 1's moving backwards.
  - If count is even, last 0 is one-bit character (1's are paired).
  - If count is odd, last 0 is part of two-bit character (one 1 unpaired).
- Example code:
  ```python
  ones = 0
  i = len(bits) - 2
  while i >= 0 and bits[i] == 1:
      ones += 1
      i -= 1
  return ones % 2 == 0
  ```

Why this works

- Key insight: only need to check 1's immediately before the final 0.
- Even number of 1's: all pair up as 11, final 0 stands alone.
- Odd number of 1's: first (odd one) pairs with final 0 as 10.
- Example: ...11110 -> 11, 11, 10 (odd, last 0 is two-bit).
- Example: ...1110 -> 11, 10 (even, last 0 is one-bit).

Time complexity

- Let n = length of array.
- Worst case: all 1's except last 0, counts n-1 ones: O(n).
- Best case: no 1's before last 0: O(1).
- Overall time complexity: O(n).

Space complexity

- Only using counter variable and index.
- Space complexity: O(1).

Thought process and trade-offs

- Reverse counting approach: elegant solution leveraging problem structure.
- Key insight: don't need to parse entire array, only consecutive 1's before end.
- Alternative: parse from beginning, tracking state - O(n) time, more complex.
- Current approach: simpler and equally efficient.
- Modulo operation determines parity: ones % 2 == 0 means even.
