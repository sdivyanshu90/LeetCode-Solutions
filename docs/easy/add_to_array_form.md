# Add to Array-Form of Integer

Problem summary

- Given an integer represented as an array of digits (most significant digit first) and an integer k, return the sum as an array.
- Example: num = [1,2,0,0], k = 34 -> [1,2,3,4]
- The array represents the integer 1200, and 1200 + 34 = 1234.

Current implementation (in repository)

- Implementation uses digit-by-digit addition with carry:
  - Iterates through the array from right to left (least significant digit first).
  - Uses k as initial carry value.
  - For each digit, adds it to carry and extracts the result digit using modulo 10.
  - Updates carry by integer division.
  - After processing all digits, continues extracting remaining carry digits.
  - Reverses the result at the end.
- Example code:
  ```python
  carry = k
  for digit in reversed(num):
      total = digit + carry
      result.append(total % 10)
      carry = total // 10
  ```

Why this works

- Treating k as carry allows seamless addition without converting the entire array to an integer.
- Processing from right to left (least significant digit) naturally handles carry propagation.
- Modulo 10 extracts the ones digit, while integer division by 10 gets the carry.
- Continuing with carry after the array ends handles cases where k has more digits than the array.

Time complexity

- Let n = length of num array, m = number of digits in k.
- Processing num array: O(n).
- Processing remaining carry: O(m) in worst case (when k is large).
- Reversing result: O(max(n, m)).
- Overall time complexity: O(n + m).

Space complexity

- Result array stores max(n, m) + 1 digits in worst case (with final carry).
- Space complexity: O(max(n, m)).

Thought process and trade-offs

- Direct simulation of addition: intuitive and matches how we add numbers by hand.
- Efficient carry handling: using k as initial carry eliminates need to convert it to array form.
- Alternative approach: convert array to integer, add k, convert back - simpler but may overflow for very large numbers (though Python handles arbitrary precision).
- Current approach is more general and works even in languages without arbitrary precision integers.
