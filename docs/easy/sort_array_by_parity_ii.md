# Sort Array By Parity II

## Problem Summary

Given an array `nums` of even length where half are even and half are odd, return an array where every even index contains an even number and every odd index contains an odd number.

**Example**: `[4,2,5,7]` → `[4,5,2,7]` or `[2,5,4,7]` (evens at indices 0,2 and odds at indices 1,3)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    even_idx = 0
    odd_idx = 1

    for num in nums:
        if num % 2 == 0:
            res[even_idx] = num
            even_idx += 2
        else:
            res[odd_idx] = num
            odd_idx += 2

    return res
```

### How It Works

The algorithm uses two index pointers:

1. **even_idx**: Starts at 0, increments by 2 (tracks indices 0, 2, 4, ...)
2. **odd_idx**: Starts at 1, increments by 2 (tracks indices 1, 3, 5, ...)
3. For each number:
   - If even: place at `even_idx`, advance by 2
   - If odd: place at `odd_idx`, advance by 2

**Example** for `[4,2,5,7]`:

```
Initial: res=[0,0,0,0], even_idx=0, odd_idx=1

num=4 (even): res[0]=4, even_idx=2 → res=[4,0,0,0]
num=2 (even): res[2]=2, even_idx=4 → res=[4,0,2,0]
num=5 (odd): res[1]=5, odd_idx=3 → res=[4,5,2,0]
num=7 (odd): res[3]=7, odd_idx=5 → res=[4,5,2,7]
```

### Why Two Pointers Works

- **Separate tracks**: Even and odd indices never interfere
- **Single pass**: Processes each element exactly once
- **Guaranteed fit**: Problem guarantees equal counts of even/odd numbers
- **Direct placement**: No swapping or searching needed

### Complexity Analysis

- **Time Complexity**: O(n) where n is the array length. Single pass through the input.
- **Space Complexity**: O(n) for the result array. Uses O(1) auxiliary space for the index pointers.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
