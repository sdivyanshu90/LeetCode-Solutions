# Binary Prefix Divisible By 5

## Problem Summary

Given a binary array `nums`, return an array of booleans where `answer[i]` is `true` if the binary number formed by the first `i+1` elements (prefix) is divisible by 5, otherwise `false`.

## Current Implementation

The solution maintains a running value representing the decimal number formed by the binary prefix, keeping only the remainder when divided by 5:

```python
def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    answer = list()
    prefix = 0
    for num in nums:
        prefix = ((prefix << 1) + num) % 5
        answer.append(prefix == 0)
    return answer
```

## How It Works

- **Binary to decimal conversion**: Each iteration shifts the current prefix left by 1 bit (`prefix << 1`) and adds the new bit (`+ num`)
- **Modulo optimization**: Instead of tracking the full number, only track `prefix % 5` to avoid overflow with large inputs
- **Divisibility check**: A number is divisible by 5 when `prefix % 5 == 0`

**Example**: `nums = [0,1,1]`

- i=0: prefix = (0 << 1) + 0 = 0, 0 % 5 = 0 → True
- i=1: prefix = (0 << 1) + 1 = 1, 1 % 5 = 1 → False
- i=2: prefix = (1 << 1) + 1 = 3, 3 % 5 = 3 → False

Result: `[True, False, False]`

## Why This Works

- The modulo operation preserves divisibility: `(a % 5) == 0` if and only if `a` is divisible by 5
- Using modulo prevents integer overflow for very long binary arrays
- Left shift by 1 is equivalent to multiplying by 2 in binary

## Time Complexity

O(n) where n is the length of the input array. We iterate through the array once.

## Space Complexity

O(n) for the answer array. If we don't count the output, the auxiliary space is O(1).

## Trade-offs

- **Efficient**: The modulo approach prevents overflow and keeps computation constant per element
- **Simple**: Single-pass solution with clear logic
- **Optimal**: Cannot improve on O(n) time since we must examine each element
