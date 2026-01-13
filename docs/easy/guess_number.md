# Guess Number Higher or Lower

## Problem Summary

- You are playing a guessing game where a number is picked from the range [1, n].
- You have access to a pre-defined API `guess(num)` that returns:
  - -1 if num is higher than the picked number
  - 1 if num is lower than the picked number
  - 0 if num equals the picked number
- Find and return the picked number.

Approach (binary search)

- Use binary search on the range [1, n] to efficiently find the target number.
- Initialize `left = 1, right = n` (note: implementation uses left = 0 but should be 1).
- While `left <= right`:
  - Compute `mid = (left + right) // 2`.
  - Call `guess(mid)`:
    - If result is 0 → found the number, return mid.
    - If result is 1 → target is higher, search right half: `left = mid + 1`.
    - If result is -1 → target is lower, search left half: `right = mid - 1`.
- The loop guarantees finding the target.

Why this works (thought process)

- The problem exhibits a monotonic search space: all numbers below the target return 1, the target returns 0, all numbers above return -1.
- Binary search efficiently narrows down the search space by half at each step.
- The API `guess()` provides the comparison needed to decide which half to search.

Time and space complexity

- Time: O(log n) — at each step, the search space is halved. Maximum iterations = log₂(n).
- Space: O(1) — only a few integer variables used; iterative implementation uses no recursion stack.

Implementation note

- The current code uses `left = 0` but the problem states the range is [1, n]. The correct initialization should be `left = 1`.
- Additionally, when `guess(mid) == -1`, the code sets `right = mid`. This should be `right = mid - 1` to exclude mid (since mid is too high).

**Corrected implementation:**

```python
def guessNumber(self, n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        else:  # result == -1
            right = mid - 1
    return -1  # should never reach here if input is valid
```

Edge cases

- n = 1 → only one number to guess, return 1 immediately.
- Target is at the boundary (1 or n) → binary search handles correctly.
- Target is in the middle → standard binary search case.
- Very large n (up to 2³¹ - 1) → binary search remains efficient with ~31 iterations max.

Why binary search over linear search

- Linear search: O(n) time — call `guess()` up to n times.
- Binary search: O(log n) time — call `guess()` only ~log n times.
- Example: n = 1 billion → binary search needs ~30 calls vs. up to 1 billion for linear search.

Example scenarios

- n = 10, picked = 6:
  - mid = 5, guess(5) = 1 → search [6, 10]
  - mid = 8, guess(8) = -1 → search [6, 7]
  - mid = 6, guess(6) = 0 → return 6
- n = 1, picked = 1:
  - mid = 1, guess(1) = 0 → return 1
- n = 2, picked = 1:
  - mid = 1, guess(1) = 0 → return 1

Loop invariant

- At each iteration, the picked number lies within [left, right].
- When `left == right`, we've narrowed down to the exact number.
- The API guarantees exactly one correct answer, so the loop will always find it.

Alternative approaches

- Ternary search: divides range into three parts instead of two. O(log₃ n) time, but requires more `guess()` calls per iteration. Binary search is simpler and equally efficient.
- Exponential search + binary search: useful if the range is unbounded, but not applicable here since n is given.

Thought process / design choices

- Binary search is the standard and optimal approach for this problem.
- Iterative implementation is preferred to avoid recursion overhead.
- Careful handling of mid calculation to avoid integer overflow (use `left + (right - left) // 2` for very large ranges, though Python handles big integers).

Common pitfalls

- Starting `left` from 0 instead of 1 → incorrect range (problem states [1, n]).
- Not excluding `mid` when adjusting boundaries → should use `right = mid - 1` when mid is too high, and `left = mid + 1` when mid is too low.
- Using `left < right` instead of `left <= right` → may miss the target when left == right.
- Calling `guess(mid)` multiple times → inefficient; store result in a variable and check once.

Notes

- This is a classic binary search problem disguised as a game.
- The solution is optimal in terms of time complexity; no faster algorithm exists.
- The problem tests understanding of binary search and API usage.

## Approach: Binary Search (Implemented)

### Strategy

The solution uses binary search to solve the problem efficiently.

```python
def guessNumber(self, n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        else:  # result == -1
            right = mid - 1
    return -1  # should never reach here if input is valid
```

### How It Works

Problem summary

- You are playing a guessing game where a number is picked from the range [1, n].
- You have access to a pre-defined API `guess(num)` that returns:
  - -1 if num is higher than the picked number
  - 1 if num is lower than the picked number
  - 0 if num equals the picked number
- Find and return the picked number.

Approach (binary search)

- Use binary search on the range [1, n] to efficiently find the target number.
- Initialize `left = 1, right = n` (note: implementation uses left = 0 but should be 1).
- While `left <= right`:
  - Compute `mid = (left + right) // 2`.
  - Call `guess(mid)`:
    - If result is 0 → found the number, return mid.
    - If result is 1 → target is higher, search right half: `left = mid + 1`.
    - If result is -1 → target is lower, search left half: `right = mid - 1`.
- The loop guarantees finding the target.

Why this works (thought process)

- The problem exhibits a monotonic search space: all numbers below the target return 1, the target returns 0, all numbers above return -1.
- Binary search efficiently narrows down the search space by half at each step.
- The API `guess()` provides the comparison needed to decide which half to search.

Time and space complexity

- Time: O(log n) — at each step, the search space is halved. Maximum iterations = log₂(n).
- Space: O(1) — only a few integer variables used; iterative implementation uses no recursion stack.

Implementation note

- The current code uses `left = 0` but the problem states the range is [1, n]. The correct initialization should be `left = 1`.
- Additionally, when `guess(mid) == -1`, the code sets `right = mid`. This should be `right = mid - 1` to exclude mid (since mid is too high).

**Corrected implementation:**

```python
def guessNumber(self, n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        else:  # result == -1
            right = mid - 1
    return -1  # should never reach here if input is valid
```

Edge cases

- n = 1 → only one number to guess, return 1 immediately.
- Target is at the boundary (1 or n) → binary search handles correctly.
- Target is in the middle → standard binary search case.
- Very large n (up to 2³¹ - 1) → binary search remains efficient with ~31 iterations max.

Why binary search over linear search

- Linear search: O(n) time — call `guess()` up to n times.
- Binary search: O(log n) time — call `guess()` only ~log n times.
- Example: n = 1 billion → binary search needs ~30 calls vs. up to 1 billion for linear search.

Example scenarios

- n = 10, picked = 6:
  - mid = 5, guess(5) = 1 → search [6, 10]
  - mid = 8, guess(8) = -1 → search [6, 7]
  - mid = 6, guess(6) = 0 → return 6
- n = 1, picked = 1:
  - mid = 1, guess(1) = 0 → return 1
- n = 2, picked = 1:
  - mid = 1, guess(1) = 0 → return 1

Loop invariant

- At each iteration, the picked number lies within [left, right].
- When `left == right`, we've narrowed down to the exact number.
- The API guarantees exactly one correct answer, so the loop will always find it.

Alternative approaches

- Ternary search: divides range into three parts instead of two. O(log₃ n) time, but requires more `guess()` calls per iteration. Binary search is simpler and equally efficient.
- Exponential search + binary search: useful if the range is unbounded, but not applicable here since n is given.

Thought process / design choices

- Binary search is the standard and optimal approach for this problem.
- Iterative implementation is preferred to avoid recursion overhead.
- Careful handling of mid calculation to avoid integer overflow (use `left + (right - left) // 2` for very large ranges, though Python handles big integers).

Common pitfalls

- Starting `left` from 0 instead of 1 → incorrect range (problem states [1, n]).
- Not excluding `mid` when adjusting boundaries → should use `right = mid - 1` when mid is too high, and `left = mid + 1` when mid is too low.
- Using `left < right` instead of `left <= right` → may miss the target when left == right.
- Calling `guess(mid)` multiple times → inefficient; store result in a variable and check once.

Notes

- This is a classic binary search problem disguised as a game.
- The solution is optimal in terms of time complexity; no faster algorithm exists.
- The problem tests understanding of binary search and API usage.

### Why Binary Search Works

- The problem exhibits a monotonic search space: all numbers below the target return 1, the target returns 0, all numbers above return -1.
- Binary search efficiently narrows down the search space by half at each step.
- The API `guess()` provides the comparison needed to decide which half to search.

Time and space complexity

- Time: O(log n) — at each step, the search space is halved. Maximum iterations = log₂(n).
- Space: O(1) — only a few integer variables used; iterative implementation uses no recursion stack.

Implementation note

- The current code uses `left = 0` but the problem states the range is [1, n]. The correct initialization should be `left = 1`.
- Additionally, when `guess(mid) == -1`, the code sets `right = mid`. This should be `right = mid - 1` to exclude mid (since mid is too high).

**Corrected implementation:**

```python
def guessNumber(self, n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        else:  # result == -1
            right = mid - 1
    return -1  # should never reach here if input is valid
```

Edge cases

- n = 1 → only one number to guess, return 1 immediately.
- Target is at the boundary (1 or n) → binary search handles correctly.
- Target is in the middle → standard binary search case.
- Very large n (up to 2³¹ - 1) → binary search remains efficient with ~31 iterations max.

Why binary search over linear search

- Linear search: O(n) time — call `guess()` up to n times.
- Binary search: O(log n) time — call `guess()` only ~log n times.
- Example: n = 1 billion → binary search needs ~30 calls vs. up to 1 billion for linear search.

Example scenarios

- n = 10, picked = 6:
  - mid = 5, guess(5) = 1 → search [6, 10]
  - mid = 8, guess(8) = -1 → search [6, 7]
  - mid = 6, guess(6) = 0 → return 6
- n = 1, picked = 1:
  - mid = 1, guess(1) = 0 → return 1
- n = 2, picked = 1:
  - mid = 1, guess(1) = 0 → return 1

Loop invariant

- At each iteration, the picked number lies within [left, right].
- When `left == right`, we've narrowed down to the exact number.
- The API guarantees exactly one correct answer, so the loop will always find it.

Alternative approaches

- Ternary search: divides range into three parts instead of two. O(log₃ n) time, but requires more `guess()` calls per iteration. Binary search is simpler and equally efficient.
- Exponential search + binary search: useful if the range is unbounded, but not applicable here since n is given.

Thought process / design choices

- Binary search is the standard and optimal approach for this problem.
- Iterative implementation is preferred to avoid recursion overhead.
- Careful handling of mid calculation to avoid integer overflow (use `left + (right - left) // 2` for very large ranges, though Python handles big integers).

Common pitfalls

- Starting `left` from 0 instead of 1 → incorrect range (problem states [1, n]).
- Not excluding `mid` when adjusting boundaries → should use `right = mid - 1` when mid is too high, and `left = mid + 1` when mid is too low.
- Using `left < right` instead of `left <= right` → may miss the target when left == right.
- Calling `guess(mid)` multiple times → inefficient; store result in a variable and check once.

Notes

- This is a classic binary search problem disguised as a game.
- The solution is optimal in terms of time complexity; no faster algorithm exists.
- The problem tests understanding of binary search and API usage.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(log n) — at each step, the search space is halved. Maximum iterations = log₂(n). - Space: O(1) — only a few integer variables used; iterative implementation uses no recursion stack. Implementation note - The current code uses `left = 0` but the problem states the range is [1, n]. The correct initialization should be `left = 1`. - Additionally, when `guess(mid) == -1`, the code sets `right = mid`. This should be `right = mid - 1` to exclude mid (since mid is too high). **Corrected implementation:** ```python def guessNumber(self, n: int) -> int:     left, right = 1, n     while left <= right:         mid = (left + right) // 2         result = guess(mid)         if result == 0:             return mid         elif result == 1:             left = mid + 1         else:  # result == -1             right = mid - 1     return -1  # should never reach here if input is valid ``` Edge cases - n = 1 → only one number to guess, return 1 immediately. - Target is at the boundary (1 or n) → binary search handles correctly. - Target is in the middle → standard binary search case. - Very large n (up to 2³¹ - 1) → binary search remains efficient with ~31 iterations max. Why binary search over linear search - Linear search: O(n) time — call `guess()` up to n times. - Binary search: O(log n) time — call `guess()` only ~log n times. - Example: n = 1 billion → binary search needs ~30 calls vs. up to 1 billion for linear search. Example scenarios - n = 10, picked = 6:   - mid = 5, guess(5) = 1 → search [6, 10]   - mid = 8, guess(8) = -1 → search [6, 7]   - mid = 6, guess(6) = 0 → return 6 - n = 1, picked = 1:   - mid = 1, guess(1) = 0 → return 1 - n = 2, picked = 1:   - mid = 1, guess(1) = 0 → return 1 Loop invariant - At each iteration, the picked number lies within [left, right]. - When `left == right`, we've narrowed down to the exact number. - The API guarantees exactly one correct answer, so the loop will always find it. Alternative approaches - Ternary search: divides range into three parts instead of two. O(log₃ n) time, but requires more `guess()` calls per iteration. Binary search is simpler and equally efficient. - Exponential search + binary search: useful if the range is unbounded, but not applicable here since n is given. Thought process / design choices - Binary search is the standard and optimal approach for this problem. - Iterative implementation is preferred to avoid recursion overhead. - Careful handling of mid calculation to avoid integer overflow (use `left + (right - left) // 2` for very large ranges, though Python handles big integers). Common pitfalls - Starting `left` from 0 instead of 1 → incorrect range (problem states [1, n]). - Not excluding `mid` when adjusting boundaries → should use `right = mid - 1` when mid is too high, and `left = mid + 1` when mid is too low. - Using `left < right` instead of `left <= right` → may miss the target when left == right. - Calling `guess(mid)` multiple times → inefficient; store result in a variable and check once. Notes - This is a classic binary search problem disguised as a game. - The solution is optimal in terms of time complexity; no faster algorithm exists. - The problem tests understanding of binary search and API usage.

### Advantages

- Efficient binary search solution
- Clear and maintainable code

### Disadvantages

- May require additional space
