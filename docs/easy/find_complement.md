# Find the Complement of an Integer

## Problem Summary

- Given a positive integer `num`, return its complement.
- The complement of an integer is the integer you get when you flip all the bits in its binary representation.
- Only flip bits that represent the magnitude; do not flip the sign bit (treat as unsigned).
- Example: num = 5 (binary 101) → complement is 2 (binary 010).

Approach (bitwise XOR with mask)

- Determine the bit length of `num` using `num.bit_length()`. This gives the position of the most significant bit.
- Create a mask with all 1s up to that bit position: `mask = (1 << bit_length) - 1`.
  - Example: if bit_length = 3, then 1 << 3 = 8 (binary 1000), mask = 8 - 1 = 7 (binary 0111).
- XOR the number with the mask: `num ^ mask`. This flips all bits up to the MSB.
  - Example: 5 (binary 101) ^ 7 (binary 111) = 2 (binary 010).

Why this works (thought process)

- XOR with 1 flips a bit; XOR with 0 leaves it unchanged.
- A mask of all 1s in the relevant positions, when XORed with the number, flips exactly those bits.
- We create a mask with 1s only up to the MSB of the original number, ensuring we flip the right bits.

Time and space complexity

- Time: O(1) — `bit_length()` is O(log num) in theory but typically O(1) on modern hardware for fixed-width integers.
  - Bit shift and XOR are O(1) operations.
- Space: O(1) — only a few integer variables used.

Edge cases and correctness

- num = 0 → bit_length = 0, mask = 0, complement = 0 ^ 0 = 0. (Expected per test: returns 1 if treating as special case; check problem definition.)
- num = 1 → bit_length = 1, mask = 1, complement = 1 ^ 1 = 0. ✓
- Large num: algorithm scales logarithmically in magnitude; Python handles arbitrary-precision integers.
- Only works for non-negative integers (unsigned interpretation).

Alternative approaches

- Iterative bit flipping: iterate through each bit, flip it, rebuild the number. O(log num) time, less elegant.
- String manipulation: convert to binary string, replace '0'→'1' and '1'→'0', convert back. O(log num) time and space, less efficient.

Example testcases (from repository)

- findComplement(5) = 2 (101 → 010)
- findComplement(1) = 0 (1 → 0)
- findComplement(0) = 1 (special case or 0 → 1)
- findComplement(10) = 5 (1010 → 0101)
- findComplement(7) = 0 (111 → 000)

Notes

- The solution is elegant and optimal.
- It assumes unsigned interpretation (no sign bit), so negative numbers are not handled.
- If you need to handle negative numbers or two's complement, modify the mask or approach accordingly.

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

### How It Works

Problem summary

- Given a positive integer `num`, return its complement.
- The complement of an integer is the integer you get when you flip all the bits in its binary representation.
- Only flip bits that represent the magnitude; do not flip the sign bit (treat as unsigned).
- Example: num = 5 (binary 101) → complement is 2 (binary 010).

Approach (bitwise XOR with mask)

- Determine the bit length of `num` using `num.bit_length()`. This gives the position of the most significant bit.
- Create a mask with all 1s up to that bit position: `mask = (1 << bit_length) - 1`.
  - Example: if bit_length = 3, then 1 << 3 = 8 (binary 1000), mask = 8 - 1 = 7 (binary 0111).
- XOR the number with the mask: `num ^ mask`. This flips all bits up to the MSB.
  - Example: 5 (binary 101) ^ 7 (binary 111) = 2 (binary 010).

Why this works (thought process)

- XOR with 1 flips a bit; XOR with 0 leaves it unchanged.
- A mask of all 1s in the relevant positions, when XORed with the number, flips exactly those bits.
- We create a mask with 1s only up to the MSB of the original number, ensuring we flip the right bits.

Time and space complexity

- Time: O(1) — `bit_length()` is O(log num) in theory but typically O(1) on modern hardware for fixed-width integers.
  - Bit shift and XOR are O(1) operations.
- Space: O(1) — only a few integer variables used.

Edge cases and correctness

- num = 0 → bit_length = 0, mask = 0, complement = 0 ^ 0 = 0. (Expected per test: returns 1 if treating as special case; check problem definition.)
- num = 1 → bit_length = 1, mask = 1, complement = 1 ^ 1 = 0. ✓
- Large num: algorithm scales logarithmically in magnitude; Python handles arbitrary-precision integers.
- Only works for non-negative integers (unsigned interpretation).

Alternative approaches

- Iterative bit flipping: iterate through each bit, flip it, rebuild the number. O(log num) time, less elegant.
- String manipulation: convert to binary string, replace '0'→'1' and '1'→'0', convert back. O(log num) time and space, less efficient.

Example testcases (from repository)

- findComplement(5) = 2 (101 → 010)
- findComplement(1) = 0 (1 → 0)
- findComplement(0) = 1 (special case or 0 → 1)
- findComplement(10) = 5 (1010 → 0101)
- findComplement(7) = 0 (111 → 000)

Notes

- The solution is elegant and optimal.
- It assumes unsigned interpretation (no sign bit), so negative numbers are not handled.
- If you need to handle negative numbers or two's complement, modify the mask or approach accordingly.

### Why Iteration Works

- XOR with 1 flips a bit; XOR with 0 leaves it unchanged.
- A mask of all 1s in the relevant positions, when XORed with the number, flips exactly those bits.
- We create a mask with 1s only up to the MSB of the original number, ensuring we flip the right bits.

Time and space complexity

- Time: O(1) — `bit_length()` is O(log num) in theory but typically O(1) on modern hardware for fixed-width integers.
  - Bit shift and XOR are O(1) operations.
- Space: O(1) — only a few integer variables used.

Edge cases and correctness

- num = 0 → bit_length = 0, mask = 0, complement = 0 ^ 0 = 0. (Expected per test: returns 1 if treating as special case; check problem definition.)
- num = 1 → bit_length = 1, mask = 1, complement = 1 ^ 1 = 0. ✓
- Large num: algorithm scales logarithmically in magnitude; Python handles arbitrary-precision integers.
- Only works for non-negative integers (unsigned interpretation).

Alternative approaches

- Iterative bit flipping: iterate through each bit, flip it, rebuild the number. O(log num) time, less elegant.
- String manipulation: convert to binary string, replace '0'→'1' and '1'→'0', convert back. O(log num) time and space, less efficient.

Example testcases (from repository)

- findComplement(5) = 2 (101 → 010)
- findComplement(1) = 0 (1 → 0)
- findComplement(0) = 1 (special case or 0 → 1)
- findComplement(10) = 5 (1010 → 0101)
- findComplement(7) = 0 (111 → 000)

Notes

- The solution is elegant and optimal.
- It assumes unsigned interpretation (no sign bit), so negative numbers are not handled.
- If you need to handle negative numbers or two's complement, modify the mask or approach accordingly.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(1) — `bit_length()` is O(log num) in theory but typically O(1) on modern hardware for fixed-width integers.   - Bit shift and XOR are O(1) operations. - Space: O(1) — only a few integer variables used. Edge cases and correctness - num = 0 → bit_length = 0, mask = 0, complement = 0 ^ 0 = 0. (Expected per test: returns 1 if treating as special case; check problem definition.) - num = 1 → bit_length = 1, mask = 1, complement = 1 ^ 1 = 0. ✓ - Large num: algorithm scales logarithmically in magnitude; Python handles arbitrary-precision integers. - Only works for non-negative integers (unsigned interpretation). Alternative approaches - Iterative bit flipping: iterate through each bit, flip it, rebuild the number. O(log num) time, less elegant. - String manipulation: convert to binary string, replace '0'→'1' and '1'→'0', convert back. O(log num) time and space, less efficient. Example testcases (from repository) - findComplement(5) = 2 (101 → 010) - findComplement(1) = 0 (1 → 0) - findComplement(0) = 1 (special case or 0 → 1) - findComplement(10) = 5 (1010 → 0101) - findComplement(7) = 0 (111 → 000) Notes - The solution is elegant and optimal. - It assumes unsigned interpretation (no sign bit), so negative numbers are not handled. - If you need to handle negative numbers or two's complement, modify the mask or approach accordingly.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
