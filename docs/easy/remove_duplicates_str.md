# Remove All Adjacent Duplicates In String

## Problem Summary

Given a string `s`, repeatedly remove all adjacent duplicate characters until no more removals can be made. Return the final string.

**Example**: `"abbaca"` → `"ca"` (remove "bb", then "aa")

## Current Implementation

The solution uses a stack-based approach to efficiently remove adjacent duplicates in a single pass:

```python
def removeDuplicates(self, s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
```

## How It Works

The stack naturally handles cascading removals:

1. Iterate through each character
2. If stack top equals current character, pop (remove adjacent duplicate)
3. Otherwise, push character onto stack
4. Join remaining stack elements to form result

**Example walkthrough** for `"abbaca"`:

```
char 'a': stack=[] → push → stack=['a']
char 'b': stack=['a'], 'b'!='a' → push → stack=['a','b']
char 'b': stack=['a','b'], 'b'=='b' → pop → stack=['a']
char 'a': stack=['a'], 'a'=='a' → pop → stack=[]
char 'c': stack=[], push → stack=['c']
char 'a': stack=['c'], 'a'!='c' → push → stack=['c','a']
Result: "ca"
```

## Why This Works

- Stack LIFO property ensures we always check the most recent unmatched character
- Popping when duplicate found handles immediate and cascading removals
- Single pass processes all characters exactly once
- No need for multiple passes or string rebuilding

## Time Complexity

O(n) where n is the length of the string. Each character is pushed and popped at most once.

## Space Complexity

O(n) for the stack in worst case (no duplicates). Best case O(1) when all characters cancel out.

## Trade-offs

- **Efficient**: Single pass solution vs naive repeated scanning
- **Clean**: Stack naturally models the problem structure
- **Optimal**: Cannot do better than O(n) since we must examine each character
- **Alternative**: Could use string as stack (less efficient due to immutability in some languages, but Python's list is efficient)
