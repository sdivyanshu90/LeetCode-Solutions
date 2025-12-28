# Remove Outermost Parentheses

## Problem Summary

Given a valid parentheses string `s`, remove the outermost parentheses of every primitive decomposition. A primitive string is a non-empty valid parentheses string that cannot be split into two non-empty valid strings.

**Example**: `"(()())(())"` → `"()()()"` (remove outer `()` from `(()())` and `(())`)

## Current Implementation

The solution uses a counter to track nesting depth and only adds parentheses that are not outermost:

```python
def removeOuterParentheses(self, s: str) -> str:
    res, opened = [], 0
    for para in s:
        if para == "(" and opened > 0:
            res.append(para)
        if para == ")" and opened > 1:
            res.append(para)
        opened += 1 if para == "(" else -1
    return "".join(res)
```

## How It Works

The algorithm maintains a counter `opened` to track parenthesis depth:

1. **Opening parenthesis `(`**: Add to result only if `opened > 0` (not outermost)
2. **Closing parenthesis `)`**: Add to result only if `opened > 1` (not outermost)
3. **Update counter**: Increment for `(`, decrement for `)`

The key insight: outermost `(` has `opened=0`, outermost `)` has `opened=1` (before decrement).

**Example walkthrough** for `"(()())(())"`:

```
'(': opened=0, don't add, opened→1
'(': opened=1, add '(', opened→2
')': opened=2, add ')', opened→1
'(': opened=1, add '(', opened→2
')': opened=2, add ')', opened→1
')': opened=1, don't add, opened→0
'(': opened=0, don't add, opened→1
'(': opened=1, add '(', opened→2
')': opened=2, add ')', opened→1
')': opened=1, don't add, opened→0
Result: "()()()"
```

## Why This Works

- **Depth tracking**: `opened` identifies nesting level
- **Outermost detection**: Level 0 for `(` and level 1 for `)` mark boundaries
- **Single pass**: Processes each character exactly once
- **Valid input guarantee**: Problem states input is valid parentheses

## Time Complexity

O(n) where n is the length of the string. Single pass through all characters.

## Space Complexity

O(n) for the result list. The final string also requires O(n) space.

## Trade-offs

- **Efficient**: Single pass with simple counter logic
- **Clear**: The depth counter makes the logic intuitive
- **Optimal**: Cannot do better than O(n) time since we must examine each character
- **Assumes valid input**: Doesn't validate parentheses (per problem constraints)
