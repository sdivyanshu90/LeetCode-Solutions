# Reverse Only Letters

## Problem Summary

Given a string `s`, reverse only the letters while keeping all non-letter characters in their original positions.

**Example**: `"ab-cd"` → `"dc-ba"` (letters reversed, dash stays in position)

## Current Implementation

The solution uses a two-pointer approach to swap letters while skipping non-letters:

```python
def reverseOnlyLetters(self, s: str) -> str:
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return "".join(s)
```

## How It Works

The algorithm uses two pointers converging from both ends:

1. **Left pointer** (`i`) starts at beginning, **right pointer** (`j`) at end
2. Skip non-letter characters by advancing appropriate pointer
3. When both pointers are at letters, swap them
4. Move both pointers inward and repeat

**Example walkthrough** for `"ab-cd"`:

```
Initial: ['a','b','-','c','d'], i=0, j=4
i=0('a'), j=4('d'): both letters → swap → ['d','b','-','c','a'], i=1, j=3
i=1('b'), j=3('c'): both letters → swap → ['d','c','-','b','a'], i=2, j=2
i=2, j=2: i>=j, stop
Result: "dc-ba"
```

## Why This Works

- **Two-pointer technique**: Efficiently processes array from both ends
- **Conditional advancement**: Skip non-letters without affecting position
- **In-place swaps**: Only letter positions change
- **Preserves non-letters**: They're never moved or swapped

## Time Complexity

O(n) where n is the length of the string. Each character is visited at most once by either pointer.

## Space Complexity

O(n) for converting string to list (strings are immutable in Python). The algorithm itself uses O(1) auxiliary space for pointers.

## Trade-offs

- **Clean logic**: Two-pointer pattern is straightforward and elegant
- **Efficient**: Single pass through the string
- **String to list conversion**: Necessary in Python due to immutability, adds O(n) space
- **Alternative**: Could collect letters separately, reverse them, and reconstruct (also O(n) time and space)
