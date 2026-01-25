# Remove Outermost Parentheses

## Problem Summary

Given a valid parentheses string `s`, remove the outermost parentheses of every primitive decomposition. A primitive string is a non-empty valid parentheses string that cannot be split into two non-empty valid strings.

**Example**: `"(()())(())"` → `"()()()"` (remove outer `()` from `(()())` and `(())`)

## Approach: Frequency Counting (Implemented)

### Strategy

The solution uses frequency counting to solve the problem efficiently.

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

### How It Works

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

### Why Frequency Counting Works

- **Depth tracking**: `opened` identifies nesting level
- **Outermost detection**: Level 0 for `(` and level 1 for `)` mark boundaries
- **Single pass**: Processes each character exactly once
- **Valid input guarantee**: Problem states input is valid parentheses

### Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the string. Single pass through all characters.
- **Space Complexity**: O(n) for the result list. The final string also requires O(n) space.

### Advantages

- Efficient frequency counting solution
- Clear and maintainable code

### Disadvantages

- May require additional space
