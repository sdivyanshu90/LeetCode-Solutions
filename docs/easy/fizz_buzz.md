# FizzBuzz

## Problem Summary

Given an integer `n`, return a list of strings representing the numbers from 1 to n with the following rules:

- For multiples of 3: replace with `"Fizz"`
- For multiples of 5: replace with `"Buzz"`
- For multiples of both 3 and 5: replace with `"FizzBuzz"`
- Otherwise: keep the number as a string

**Example**: `n = 5` → `["1", "2", "Fizz", "4", "Buzz"]`

## Approach: Iteration (Implemented)

### Strategy

The solution uses iteration to solve the problem efficiently.

```python
  rules = [(3, "Fizz"), (5, "Buzz")]
  result = []
  for i in range(1, n + 1):
      output = "".join(word for num, word in rules if i % num == 0)
      result.append(output or str(i))
  return result
  ```

### How It Works

### Strategy

Approach (iterative string building)

- Iterate from 1 to n (inclusive).
- For each number i:
  - Initialize an empty string `s`.
  - Check divisibility by 3: if `i % 3 == 0`, append "Fizz".
  - Check divisibility by 5: if `i % 5 == 0`, append "Buzz".
  - If `s` is still empty (not divisible by 3 or 5), append the string representation of i.
  - Add the result to the output list.
- Return the list.

Why this works (thought process)

- By checking divisibility conditions with modulo operators and building the string incrementally, we handle all four cases:
  - Divisible by 3 only → "Fizz"
  - Divisible by 5 only → "Buzz"
  - Divisible by both 3 and 5 → "FizzBuzz" (appended in order)
  - Divisible by neither → the number itself
- The string building approach naturally handles the "both 3 and 5" case without explicit logic.

Time and space complexity

- Time: O(n) — iterate from 1 to n, each iteration performs O(1) work (constant divisibility checks and string operations).
- Space: O(n) — output list contains n strings. Auxiliary space (excluding output) is O(1).

Edge cases and robustness

- n = 0 → return [] (no numbers from 1 to 0).
- n = 1 → return ["1"] (only the number 1).
- n = 3 → return ["1", "2", "Fizz"] (first multiple of 3).
- n = 5 → return ["1", "2", "Fizz", "4", "Buzz"].
- n = 15 → contains "FizzBuzz" at position 15 (multiple of both 3 and 5).
- Large n: algorithm remains O(n) with linear memory usage.

Example testcases (from repository)

- fizzBuzz(3) → ["1", "2", "Fizz"]
- fizzBuzz(5) → ["1", "2", "Fizz", "4", "Buzz"]
- fizzBuzz(15) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
- fizzBuzz(1) → ["1"]
- fizzBuzz(0) → []

Key insight: order of checks

- Check divisibility by 3 first (append "Fizz"), then by 5 (append "Buzz").
- This order ensures that multiples of 15 produce "FizzBuzz" (Fizz first, then Buzz).
- The check `if s == ""` ensures numbers not divisible by 3 or 5 are added as strings.

Alternative approaches

- Dictionary-based (extensible for custom rules):
  ```python
  rules = [(3, "Fizz"), (5, "Buzz")]
  result = []
  for i in range(1, n + 1):
      output = "".join(word for num, word in rules if i % num == 0)
      result.append(output or str(i))
  return result
  ```
  Benefits: easier to extend with more divisibility rules.
- Ternary operator (one-liner, less readable):
  ```python
  return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n + 1)]
  ```

Thought process / design choices

- The straightforward iterative approach is clear and efficient.
- String concatenation with `+=` is idiomatic in Python.
- The empty-string check `if s == ""` is simpler and clearer than checking both divisibility conditions with `and`.

Common pitfalls

- Checking divisibility with `==` instead of modulo (e.g., `if i == 3` → only matches the number 3, not multiples).
- Checking divisibility by 15 explicitly instead of relying on sequential checks → adds unnecessary complexity.
- Using string interpolation or formatting instead of simple concatenation → slightly less efficient.
- Forgetting to convert the number to a string with `str(i)` → type mismatch when appending to the list.

Notes

- FizzBuzz is a classic interview problem testing basic programming skills and attention to detail.
- The solution is optimal in both time and space.
- The approach generalizes well if additional rules (e.g., divisible by 7 → "Jazz") are added.

### Why Iteration Works

- By checking divisibility conditions with modulo operators and building the string incrementally, we handle all four cases:
  - Divisible by 3 only → "Fizz"
  - Divisible by 5 only → "Buzz"
  - Divisible by both 3 and 5 → "FizzBuzz" (appended in order)
  - Divisible by neither → the number itself
- The string building approach naturally handles the "both 3 and 5" case without explicit logic.

Time and space complexity

- Time: O(n) — iterate from 1 to n, each iteration performs O(1) work (constant divisibility checks and string operations).
- Space: O(n) — output list contains n strings. Auxiliary space (excluding output) is O(1).

Edge cases and robustness

- n = 0 → return [] (no numbers from 1 to 0).
- n = 1 → return ["1"] (only the number 1).
- n = 3 → return ["1", "2", "Fizz"] (first multiple of 3).
- n = 5 → return ["1", "2", "Fizz", "4", "Buzz"].
- n = 15 → contains "FizzBuzz" at position 15 (multiple of both 3 and 5).
- Large n: algorithm remains O(n) with linear memory usage.

Example testcases (from repository)

- fizzBuzz(3) → ["1", "2", "Fizz"]
- fizzBuzz(5) → ["1", "2", "Fizz", "4", "Buzz"]
- fizzBuzz(15) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
- fizzBuzz(1) → ["1"]
- fizzBuzz(0) → []

Key insight: order of checks

- Check divisibility by 3 first (append "Fizz"), then by 5 (append "Buzz").
- This order ensures that multiples of 15 produce "FizzBuzz" (Fizz first, then Buzz).
- The check `if s == ""` ensures numbers not divisible by 3 or 5 are added as strings.

Alternative approaches

- Dictionary-based (extensible for custom rules):
  ```python
  rules = [(3, "Fizz"), (5, "Buzz")]
  result = []
  for i in range(1, n + 1):
      output = "".join(word for num, word in rules if i % num == 0)
      result.append(output or str(i))
  return result
  ```
  Benefits: easier to extend with more divisibility rules.
- Ternary operator (one-liner, less readable):
  ```python
  return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n + 1)]
  ```

Thought process / design choices

- The straightforward iterative approach is clear and efficient.
- String concatenation with `+=` is idiomatic in Python.
- The empty-string check `if s == ""` is simpler and clearer than checking both divisibility conditions with `and`.

Common pitfalls

- Checking divisibility with `==` instead of modulo (e.g., `if i == 3` → only matches the number 3, not multiples).
- Checking divisibility by 15 explicitly instead of relying on sequential checks → adds unnecessary complexity.
- Using string interpolation or formatting instead of simple concatenation → slightly less efficient.
- Forgetting to convert the number to a string with `str(i)` → type mismatch when appending to the list.

Notes

- FizzBuzz is a classic interview problem testing basic programming skills and attention to detail.
- The solution is optimal in both time and space.
- The approach generalizes well if additional rules (e.g., divisible by 7 → "Jazz") are added.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n) — iterate from 1 to n, each iteration performs O(1) work (constant divisibility checks and string operations). - Space: O(n) — output list contains n strings. Auxiliary space (excluding output) is O(1). Edge cases and robustness - n = 0 → return [] (no numbers from 1 to 0). - n = 1 → return ["1"] (only the number 1). - n = 3 → return ["1", "2", "Fizz"] (first multiple of 3). - n = 5 → return ["1", "2", "Fizz", "4", "Buzz"]. - n = 15 → contains "FizzBuzz" at position 15 (multiple of both 3 and 5). - Large n: algorithm remains O(n) with linear memory usage. Example testcases (from repository) - fizzBuzz(3) → ["1", "2", "Fizz"] - fizzBuzz(5) → ["1", "2", "Fizz", "4", "Buzz"] - fizzBuzz(15) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"] - fizzBuzz(1) → ["1"] - fizzBuzz(0) → [] Key insight: order of checks - Check divisibility by 3 first (append "Fizz"), then by 5 (append "Buzz"). - This order ensures that multiples of 15 produce "FizzBuzz" (Fizz first, then Buzz). - The check `if s == ""` ensures numbers not divisible by 3 or 5 are added as strings. Alternative approaches - Dictionary-based (extensible for custom rules):   ```python   rules = [(3, "Fizz"), (5, "Buzz")]   result = []   for i in range(1, n + 1):       output = "".join(word for num, word in rules if i % num == 0)       result.append(output or str(i))   return result   ```   Benefits: easier to extend with more divisibility rules. - Ternary operator (one-liner, less readable):   ```python   return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n + 1)]   ``` Thought process / design choices - The straightforward iterative approach is clear and efficient. - String concatenation with `+=` is idiomatic in Python. - The empty-string check `if s == ""` is simpler and clearer than checking both divisibility conditions with `and`. Common pitfalls - Checking divisibility with `==` instead of modulo (e.g., `if i == 3` → only matches the number 3, not multiples). - Checking divisibility by 15 explicitly instead of relying on sequential checks → adds unnecessary complexity. - Using string interpolation or formatting instead of simple concatenation → slightly less efficient. - Forgetting to convert the number to a string with `str(i)` → type mismatch when appending to the list. Notes - FizzBuzz is a classic interview problem testing basic programming skills and attention to detail. - The solution is optimal in both time and space. - The approach generalizes well if additional rules (e.g., divisible by 7 → "Jazz") are added.

### Advantages

- Efficient iteration solution
- Clear and maintainable code

### Disadvantages

- May require additional space
