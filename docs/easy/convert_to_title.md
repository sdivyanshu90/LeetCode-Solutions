# Convert to Title

Problem summary

- Given a positive integer `columnNumber`, return its corresponding column title as appear in Excel:
  - 1 -> "A", 2 -> "B", ..., 26 -> "Z", 27 -> "AA", etc.
- Note: This is a 1-indexed base-26-like system where there is no zero digit.

Core idea / thought process

- Treat the problem as converting `columnNumber` to a base-26 representation, but because digits are 1..26 (not 0..25) we must adjust at each step.
- Subtract 1 from `columnNumber` before taking modulo 26. This converts the 1..26 range to 0..25 and lets us use 0-based indexing into the alphabet.
- Repeatedly:
  1. Decrement `columnNumber` by 1.
  2. Take `columnNumber % 26` to get the current least-significant "digit".
  3. Map that digit to a letter via ASCII: `chr(digit + ord('A'))`.
  4. Divide `columnNumber` by 26 (integer division) and continue until zero.
- Build letters from least-significant to most-significant, then reverse.

Algorithm (high level)

- Initialize empty list `title`.
- While `columnNumber > 0`:
  - `columnNumber -= 1`
  - `title.append(chr((columnNumber % 26) + ord('A')))`
  - `columnNumber //= 26`
- Return `''.join(reversed(title))`.

Why subtract 1

- Without subtracting 1, modulo and division won't align with the 1..26 digit mapping. Example: 26 should map to 'Z' — subtracting 1 yields 25 -> 'Z'.

Time complexity

- Each loop iteration removes one base-26 digit. Number of iterations = O($\log_{26}(\text{columnNumber})$) = O(log columnNumber).
- For typical analysis, this is O(log n) where n is the input number.

Space complexity

- O($\log_{26}(\text{columnNumber})$) extra space to store the resulting characters (the output itself). Auxiliary space is proportional to the number of output letters.

Edge cases and notes

- columnNumber = 0: Excel columns are 1-based; the implementation returns an empty string for 0 (current tests expect "").
- Very large columnNumber: algorithm scales logarithmically in the number of digits; Python handles big integers.
- Works for all positive integers; no floating point operations are used so results are exact.

Examples

- 1 -> "A"
- 26 -> "Z"
- 27 -> "AA"
- 52 -> "AZ"
- 701 -> "ZY"
- 702 -> "ZZ"
- 703 -> "AAA"
- 16384 -> "XFD" (Excel column boundary example)

Alternative views

- You can view this as repeated (columnNumber-1) divmod 26 operations.
- Recursive formulation is possible but iterative is simpler and avoids recursion overhead.

Correctness sketch

- At each step you determine the last letter correctly by mapping the remainder after subtracting 1. Removing that digit via integer division reduces the problem size and preserves correctness by induction.
