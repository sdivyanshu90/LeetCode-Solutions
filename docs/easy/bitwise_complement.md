# Bitwise Complement

## Problem Summary

- Given a positive integer n, return its bitwise complement.
- The complement flips every bit: 0 becomes 1, and 1 becomes 0.
- Example: n = 5 (binary: 101) -> complement is 010 -> return 2.

Current implementation (in repository)

- Implementation converts to binary and flips bits:
  - Converts n to binary string using `bin(n)[2:]`.
  - Uses generator expression to flip each bit: '1' becomes '0' and vice versa.
  - Joins the flipped bits into a string.
  - Converts the binary string back to integer using `int(result, 2)`.
- Example code:
  ```python
  return int(''.join('1' if bit == '0' else '0' for bit in bin(n)[2:]), 2)
  ```

Why this works

- Binary representation exposes individual bits for manipulation.
- String manipulation with conditional expression flips each bit.
- Converting back from binary string to integer produces the complement value.
- Works correctly for any positive integer including edge cases like 0 and 1.

Time complexity

- Let m = number of bits in n (approximately log₂(n)).
- Converting to binary: O(m).
- Flipping bits: O(m) for iterating and building new string.
- Converting back to integer: O(m).
- Overall time complexity: O(m) = O(log n).

Space complexity

- Binary string and flipped string each take O(m) = O(log n) space.
- Overall space complexity: O(log n).

Thought process and trade-offs

- String-based approach: concise one-liner, easy to understand.
- Alternative bitwise approach: use XOR with a mask of all 1's (2^m - 1 where m is bit length). More efficient but requires calculating bit length.
- Example: for n = 5 (101), mask = 111 (7), 5 XOR 7 = 2.
- Current approach prioritizes readability over micro-optimization.
- For small to moderate integers, performance difference is negligible.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  return int(''.join('1' if bit == '0' else '0' for bit in bin(n)[2:]), 2)
  ```

### How It Works

- Alternative bitwise approach: use XOR with a mask of all 1's (2^m - 1 where m is bit length). More efficient but requires calculating bit length.
- Example: for n = 5 (101), mask = 111 (7), 5 XOR 7 = 2.
- Current approach prioritizes readability over micro-optimization.
- For small to moderate integers, performance difference is negligible.

### Why Iteration Works

- Binary representation exposes individual bits for manipulation.
- String manipulation with conditional expression flips each bit.
- Converting back from binary string to integer produces the complement value.
- Works correctly for any positive integer including edge cases like 0 and 1.

Time complexity

- Let m = number of bits in n (approximately log₂(n)).
- Converting to binary: O(m).
- Flipping bits: O(m) for iterating and building new string.
- Converting back to integer: O(m).
- Overall time complexity: O(m) = O(log n).

Space complexity

- Binary string and flipped string each take O(m) = O(log n) space.
- Overall space complexity: O(log n).

Thought process and trade-offs

- String-based approach: concise one-liner, easy to understand.
- Alternative bitwise approach: use XOR with a mask of all 1's (2^m - 1 where m is bit length). More efficient but requires calculating bit length.
- Example: for n = 5 (101), mask = 111 (7), 5 XOR 7 = 2.
- Current approach prioritizes readability over micro-optimization.
- For small to moderate integers, performance difference is negligible.

### Complexity Analysis

- **Time Complexity**: - Let m = number of bits in n (approximately log₂(n)). - Converting to binary: O(m). - Flipping bits: O(m) for iterating and building new string. - Converting back to integer: O(m). - Overall time complexity: O(m) = O(log n). Space complexity - Binary string and flipped string each take O(m) = O(log n) space. - Overall space complexity: O(log n). Thought process and trade-offs - String-based approach: concise one-liner, easy to understand. - Alternative bitwise approach: use XOR with a mask of all 1's (2^m - 1 where m is bit length). More efficient but requires calculating bit length. - Example: for n = 5 (101), mask = 111 (7), 5 XOR 7 = 2. - Current approach prioritizes readability over micro-optimization. - For small to moderate integers, performance difference is negligible.
- **Space Complexity**: - Binary string and flipped string each take O(m) = O(log n) space. - Overall space complexity: O(log n). Thought process and trade-offs - String-based approach: concise one-liner, easy to understand. - Alternative bitwise approach: use XOR with a mask of all 1's (2^m - 1 where m is bit length). More efficient but requires calculating bit length. - Example: for n = 5 (101), mask = 111 (7), 5 XOR 7 = 2. - Current approach prioritizes readability over micro-optimization. - For small to moderate integers, performance difference is negligible.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
