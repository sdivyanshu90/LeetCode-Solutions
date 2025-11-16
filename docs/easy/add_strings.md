# Add Strings

Problem summary

- Given two non-negative integers num1 and num2 represented as decimal strings, return their sum as a string.
- You must not convert the entire strings to integers (solution in repository uses manual digit addition).

Approach (digit-by-digit addition, right-to-left)

- Use two indices i = len(num1)-1 and j = len(num2)-1 to traverse digits from least significant to most.
- Maintain a carry (0 or greater).
- While i >= 0 or j >= 0 or carry:
  - Take digit1 = int(num1[i]) if i >= 0 else 0
  - Take digit2 = int(num2[j]) if j >= 0 else 0
  - total = digit1 + digit2 + carry
  - append (total % 10) to result buffer
  - carry = total // 10
  - decrement i, j as appropriate
- Reverse the result buffer and join to produce the output string.

Why this works

- This mirrors manual addition of decimal numbers from least significant digit, propagating carry.
- No integer overflow risk; works for arbitrarily long inputs.

Time complexity

- Let n = max(len(num1), len(num2)).
- Each digit is processed exactly once: O(n).

Space complexity

- Result buffer stores at most n+1 digits (when final carry adds a new digit): O(n).
- Auxiliary space besides output is O(1).

Thought process and trade-offs

- Manual addition avoids big-integer conversions and is memory-predictable.
- Using list append + reverse is efficient in Python (amortized O(1) append).
- Converting single-character digits via int() is simple and fast; for micro-optimization use ord(...) - 48.

Edge cases handled

- Different lengths (missing digits treated as 0).
- Leading zeros in inputs.
- Final carry producing an extra digit (e.g., "999" + "1" -> "1000").
- Both inputs "0" -> "0".

Examples (from repository tests)

- "11" + "123" -> "134"
- "999" + "1" -> "1000"
- "12345678901234567890" + "98765432109876543210" -> "111111111011111111100"

Notes / improvements

- The current implementation is optimal for this problem. If you need to avoid int() conversions of single chars, replace with ord() subtraction.
