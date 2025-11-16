# Add Binary

Problem summary

- Given two binary strings `a` and `b`, return their sum as a binary string.
- Example: a = "11", b = "1" -> "100".

Current implementation (in repository)

- Implementation uses Python's built-in base conversion and formatting:
  - Convert binary strings to integers: `int(a, 2)` and `int(b, 2)`.
  - Sum the integers.
  - Convert the sum back to binary string using format specifier `:b`.
- Example code:
  ```python
  return f"{int(a, 2) + int(b, 2):b}"
  ```

Why this works

- Converting binary string -> integer interprets the full binary number correctly.
- Python integers are arbitrary-precision, so the conversion and addition produce the exact numeric sum.
- Formatting with `:b` serialises the integer back to a binary representation without the `0b` prefix.

Time complexity

- Let n = max(len(a), len(b)).
- Parsing each binary string into an integer (`int(s, 2)`) costs O(len(s)) time (scan and accumulate). So combined parsing is O(n).
- Addition of two Python big integers costs O(n) in typical implementations (linear in number of machine words / digits).
- Formatting the integer back to binary (`format(..., "b")`) costs O(n).
- Overall time complexity: O(n).

Space complexity

- The algorithm constructs big integer objects and the result string; space is O(n) (for input-to-integer intermediate representation and the output string).
- Auxiliary space beyond inputs and output is O(1).

Thought process and trade-offs

- Simplicity and readability: using Python's built-ins yields a one-liner that is easy to read and maintain.
- Correctness: arbitrary precision integers handle very long inputs without overflow.
- Performance: for typical input sizes the one-liner is efficient and simpler than a manual implementation.
- Potential downside: converting to big integers allocates memory proportional to the string length; for extremely long inputs this may be heavier than a streaming/manual approach, but asymptotically both are O(n).

Manual (bitwise) approach (O(n), constant extra memory aside from output)

- You can implement the addition manually to avoid intermediate big-int objects:
  - Use two indices starting from the end of `a` and `b` (least-significant bit).
  - Maintain carry (0 or 1).
  - At each step add corresponding bits plus carry, append result bit.
  - After processing, reverse the result list and join into a string.
- This approach has the same O(n) time and O(n) output space, but avoids big-int allocation and may be preferable in environments where you want fine-grained control.

Manual implementation example

```python
def add_binary_manual(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += ord(a[i]) - 48  # '0' -> 48
            i -= 1
        if j >= 0:
            total += ord(b[j]) - 48
            j -= 1
        res.append(str(total & 1))
        carry = total >> 1
    return ''.join(reversed(res))
```

Edge cases

- Both inputs "0" -> return "0".
- Leading zeros in inputs: `int()` handles them; manual method also handles them.
- Different lengths: both implementations handle unequal lengths naturally.

Recommendation

- Keep the current one-liner for readability and conciseness.
- If you need to micro-optimize memory allocations for very long strings, use the manual approach above.
