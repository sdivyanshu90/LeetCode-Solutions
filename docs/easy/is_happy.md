# Happy Number — Explanation, Approach, Complexity

**Problem Summary**

- A happy number is defined by the following process:
  - Starting with any positive integer, replace the number by the sum of the squares of its digits.
  - Repeat the process until the number equals 1 (happy), or it loops endlessly in a cycle that doesn't include 1 (unhappy).
- Return `True` if n is a happy number, `False` otherwise.
- Example: 19 is happy because 1² + 9² = 82, 8² + 2² = 68, 6² + 8² = 100, 1² + 0² + 0² = 1.

**Approach (Mathematical cycle detection)**

- Use the mathematical property: all unhappy numbers eventually enter a cycle containing 4.
- Loop while `n != 1` and `n != 4`:
  - Compute the sum of squares of digits using helper function `get_next(n)`.
  - Update n with the new sum.
- Return `True` if we reach 1, `False` if we reach 4 (cycle detected).

Implementation:

```python
def isHappy(self, n: int) -> bool:
    def get_next(x):
        total_sum = 0
        while x > 0:
            x, digit = divmod(x, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n != 4:
        n = get_next(n)

    return n == 1
```

**Why It Works**

- Mathematical proof: all unhappy numbers eventually reach the cycle [4, 16, 37, 58, 89, 145, 42, 20, 4].
- By checking if we reach 4, we detect entry into this cycle without needing to track all visited numbers.
- Happy numbers always converge to 1.
- This is more efficient than using a set to track all visited numbers.

**Complexity**

- Time: O(log n) — each iteration reduces the magnitude of the number. The sum of squares of digits of n has at most O(log n) digits.
- Space: O(1) — no extra data structures needed; only a few variables.

**Helper Function `get_next(x)`**

- Extracts each digit using `divmod(x, 10)` which returns (quotient, remainder).
- Squares each digit and accumulates the sum.
- More efficient than string conversion.

**Edge Cases**

- n = 1 → return True immediately (already happy)
- n = 4 → return False immediately (cycle anchor)
- Single-digit numbers: 1, 7 are happy; others (2, 3, 4, 5, 6, 8, 9) are unhappy
- Large numbers → converge quickly due to digit squaring reducing magnitude

**Alternative Approaches**

**Approach 1: Hash set cycle detection**

```python
def isHappy(self, n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
```

- Time: O(log n) average
- Space: O(log n) for the set
- More general but uses extra space

**Approach 2: Floyd's cycle detection (two pointers)**

```python
def isHappy(self, n: int) -> bool:
    def get_next(x):
        return sum(int(d) ** 2 for d in str(x))

    slow = n
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1
```

- Time: O(log n)
- Space: O(1)
- Tortoise and hare algorithm; detects cycles without extra space

**Thought Process / Design Choices**

- The mathematical property (unhappy numbers reach 4) is the key insight.
- This allows O(1) space solution without tracking visited numbers.
- Using `divmod` for digit extraction is more efficient than string conversion.
- The cycle [4, 16, 37, 58, 89, 145, 42, 20, 4] is well-known and proven.

**Example Sequences**

- Happy: 19 → 82 → 68 → 100 → 1
- Happy: 7 → 49 → 97 → 130 → 10 → 1
- Unhappy: 2 → 4 (enters cycle)
- Unhappy: 5 → 25 → 29 → 85 → 89 → 145 → 42 → 20 → 4

**Common Pitfalls**

- Not handling the cycle → infinite loop without cycle detection.
- Using string conversion inefficiently → works but slightly slower.
- Checking only for 1 without cycle detection → infinite loop on unhappy numbers.
- Not knowing the mathematical property about 4 → may use more complex cycle detection.

**Key Mathematical Insight**

- For any unhappy number, the sequence will eventually enter the cycle: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4.
- Therefore, detecting 4 is sufficient to identify unhappy numbers.
- This avoids needing to track all visited numbers in a set.
