# Valid Parentheses

## Problem Summary

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of closing bracket
2. Closing brackets must appear in the correct order
3. Every closing bracket has a corresponding opening bracket of the same type

**LeetCode Problem**: [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Approach: Stack with Hash Map (Implemented)

### Strategy

The implemented solution uses **a stack to track opening brackets and a hash map to validate closing brackets**:

1. Create an empty stack to store opening brackets
2. Create a mapping of closing brackets to opening brackets
3. Iterate through each character in the string:
   - If it's a closing bracket (in mapping), check if the stack has a matching opening bracket
   - If it's an opening bracket, push it onto the stack
4. After processing all characters, stack must be empty (all brackets matched)

**Code**:

```python
def isValid(self, s: str) -> bool:
    stack = []
    mapping = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in mapping:  # It's a closing bracket
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:  # It's an opening bracket
            stack.append(char)

    return not stack  # True if stack is empty
```

### How It Works

**Key insight**: Use a stack to remember opening brackets. When you see a closing bracket, check if it matches the most recent opening bracket (top of stack).

**Example 1**: `s = "()"`

```
Initial: stack = [], mapping = {")":"(", "}":"{", "]":"["}

char = '(':
  Not in mapping, it's opening
  stack.append('(')
  stack = ['(']

char = ')':
  In mapping, it's closing
  top_element = stack.pop() = '('
  mapping[')'] = '('
  '(' == '(' ✓ Match!
  stack = []

End: stack is empty
Return: not [] = True ✓
```

**Example 2**: `s = "()[]{}"`

```
Initial: stack = []

char = '(':
  stack = ['(']

char = ')':
  top_element = stack.pop() = '('
  mapping[')'] = '('
  '(' == '(' ✓
  stack = []

char = '[':
  stack = ['[']

char = ']':
  top_element = stack.pop() = '['
  mapping[']'] = '['
  '[' == '[' ✓
  stack = []

char = '{':
  stack = ['{']

char = '}':
  top_element = stack.pop() = '{'
  mapping['}'] = '{'
  '{' == '{' ✓
  stack = []

End: stack is empty
Return: not [] = True ✓
```

**Example 3**: `s = "([)]"` (Mismatched order)

```
Initial: stack = []

char = '(':
  stack = ['(']

char = '[':
  stack = ['(', '[']

char = ')':
  In mapping, it's closing ')'
  top_element = stack.pop() = '['
  mapping[')'] = '('
  '(' != '[' ✗ Mismatch!
  Return: False ✓
```

**Example 4**: `s = "{[]}"` (Nested correctly)

```
Initial: stack = []

char = '{':
  stack = ['{']

char = '[':
  stack = ['{', '[']

char = ']':
  top_element = stack.pop() = '['
  mapping[']'] = '['
  '[' == '[' ✓
  stack = ['{']

char = '}':
  top_element = stack.pop() = '{'
  mapping['}'] = '{'
  '{' == '{' ✓
  stack = []

End: stack is empty
Return: not [] = True ✓
```

**Example 5**: `s = "((())"` (Extra opening)

```
Initial: stack = []

char = '(':
  stack = ['(']

char = '(':
  stack = ['(', '(']

char = '(':
  stack = ['(', '(', '(']

char = ')':
  top_element = stack.pop() = '('
  mapping[')'] = '('
  '(' == '(' ✓
  stack = ['(', '(']

char = ')':
  top_element = stack.pop() = '('
  mapping[')'] = '('
  '(' == '(' ✓
  stack = ['(']

End: stack = ['('] (not empty!)
Return: not ['('] = False ✓
```

**Example 6**: `s = "())"` (Extra closing)

```
Initial: stack = []

char = '(':
  stack = ['(']

char = ')':
  top_element = stack.pop() = '('
  mapping[')'] = '('
  '(' == '(' ✓
  stack = []

char = ')':
  In mapping, closing bracket
  top_element = stack.pop() if stack else "#"
  stack is empty, so top_element = "#"
  mapping[')'] = '('
  '(' != "#" ✗ Mismatch!
  Return: False ✓
```

### Why Stack Works

**The matching problem**:

```
When we see a closing bracket:
  - It must match the MOST RECENT opening bracket
  - Not just any opening bracket
  - Stack is perfect for this (LIFO - Last In First Out)

Example: "([)]"
  '(' - push
  '[' - push (top is '[')
  ')' - must match '[' (top of stack)
       But ')' matches '(', not '['
       This is wrong! ✗
```

**Visual representation**:

```
Valid: "()"
  ( → stack: [
  ) → match with top →  stack: empty ✓

Invalid: "([)]"
  ( → stack: [(
  [ → stack: [(, [
  ) → need to match [, but ) matches ( ✗

Valid: "([)]" should actually be "([])"
  ( → stack: [(
  [ → stack: [(, [
  ] → match [ ✓  stack: [(
  ) → match ( ✓  stack: empty ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through string
  - Each character processed once
  - Stack operations (push, pop) are O(1)
  - Hash map lookup is O(1)
  - n = length of string
- **Space Complexity**: O(n)
  - Stack stores up to n characters
  - In worst case: all opening brackets (e.g., "((((")
  - Need O(n) to store them
  - n = length of string

### Advantages

- **Optimal time**: O(n) single pass
- **Clear logic**: Stack naturally solves matching problem
- **Handles all bracket types**: Generic mapping works for any brackets
- **Efficient**: All operations are O(1)

### Disadvantages

- **Uses extra space**: O(n) for stack
- **Not in-place**: Can't solve without additional memory

## Alternative Approach 1: Counter-based (Limited)

Track only if brackets are balanced (not matching types):

```python
def isValid(self, s: str) -> bool:
    # Only works if all brackets are same type
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # More closing than opening
                return False

    return count == 0
```

### How It Works

Count opening and closing brackets. If closing exceeds opening at any point, invalid.

**Example**: `s = "()"`

```
count = 0

char = '(':
  count = 1

char = ')':
  count = 0

End: count == 0
Return: True ✓
```

### Complexity

- **Time**: O(n) - single pass
- **Space**: O(1) - only counter variable

### Limitations

- **Only for single bracket type**: Can't handle multiple types
- **Doesn't verify matching types**: "(}" would return True
- **Not general solution**: Limited use case

## Alternative Approach 2: Recursive

Use recursion to match brackets:

```python
def isValid(self, s: str) -> bool:
    # Find innermost matching pair and remove it
    # Repeat until string is empty or no match found

    while len(s) > 0:
        prev_len = len(s)
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")

        # If nothing was replaced, invalid
        if len(s) == prev_len:
            return False

    return True
```

### How It Works

Remove matching pairs repeatedly. If anything remains, invalid.

**Example**: `s = "([)]"`

```
Original: "([)]"

Replace "()": No match
Replace "[]": No match
Replace "{}": No match

Nothing changed, return False ✓
```

**Example**: `s = "([])"`

```
Original: "([])

Replace "()": "([]))" → "[]"
              Wait, let me trace more carefully...
              After first replace "()": "([)])" contains "()", which is at positions...
              Actually there's no "()" substring contiguously

Let me retry with correct example: "([])"

Original: "([])"

Replace "()": No match in "([])"
Replace "[]": "([])" → "()" (replace "[]")
Replace "{}": No match

s = "()"

Replace "()": "()" → ""
Replace "[]": No match
Replace "{}": No match

s = ""

String is empty, return True ✓
```

### Complexity

- **Time**: O(n²) - potentially n replacements, each O(n)
- **Space**: O(n) - new strings created

### Advantages

- **Intuitive**: Think in terms of removing pairs
- **No data structures**: No explicit stack

### Disadvantages

- **Slow**: Multiple passes, string creation
- **String operations**: Expensive replace operations
- **Not optimal**: O(n²) vs O(n)

## Alternative Approach 3: Dictionary Depth Tracking

Track depth of each bracket type:

```python
def isValid(self, s: str) -> bool:
    depth = {"(": 0, "[": 0, "{": 0}
    opening = {"(", "[", "{"}
    closing = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in opening:
            depth[char] += 1
        else:
            if char not in closing or depth[closing[char]] == 0:
                return False
            depth[closing[char]] -= 1

    return all(v == 0 for v in depth.values())
```

### Complexity

- **Time**: O(n) - single pass
- **Space**: O(1) - fixed size dictionary (only 3 types)

### Disadvantages

- **Doesn't validate order**: "([)]" would pass (only checks counts)
- **More complex**: Needs dictionary for each type
- **Doesn't catch nesting errors**: Missing order validation

## Comparison of Approaches

| Approach            | Time  | Space | Handles Types | Validates Order | Best For                 |
| ------------------- | ----- | ----- | ------------- | --------------- | ------------------------ |
| Stack (Implemented) | O(n)  | O(n)  | ✓ Yes         | ✓ Yes           | **Optimal solution**     |
| Counter             | O(n)  | O(1)  | ✗ No          | ✗ No            | Single bracket type only |
| String Replace      | O(n²) | O(n)  | ✓ Yes         | ✓ Yes           | Educational only         |
| Dictionary Depth    | O(n)  | O(1)  | ✓ Yes         | ✗ No            | Count validation only    |

**Winner**: Stack approach for correctness and optimal complexity

## Edge Cases & Considerations

1. **Empty string**:

   - `s = ""` → `True`
   - Empty string is valid (no mismatches) ✓

2. **Single bracket (unmatched)**:

   - `s = "("` → `False`
   - Stack has one element at end ✓
   - `s = ")"` → `False`
   - Stack empty when encountering ')' ✓

3. **Only opening brackets**:

   - `s = "((("` → `False`
   - Stack not empty at end ✓

4. **Only closing brackets**:

   - `s = ")))"` → `False`
   - Stack empty when trying to pop ✓

5. **Proper nesting**:

   - `s = "{[()]}"` → `True`
   - Each bracket closes at correct time ✓

6. **Improper nesting**:

   - `s = "([)]"` → `False`
   - Closing bracket doesn't match top of stack ✓

7. **Multiple mismatches**:

   - `s = "{[}]"` → `False`
   - First mismatch detected at '}' ✓

8. **Mixed types balanced but wrong**:

   - `s = "([)]"` → `False`
   - Not about count, about order ✓

9. **Deeply nested**:

   - `s = "((((((((())))))))"` → `True`
   - Stack handles deep nesting ✓

10. **Very long string**:
    - `s = "(" * 10000 + ")" * 10000` → `True`
    - O(n) algorithm handles efficiently ✓

## Common Pitfalls

1. **Forgetting to check if stack is empty before popping**:

   ```python
   # WRONG: Crashes on extra closing bracket
   top_element = stack.pop()

   # CORRECT: Check first or provide default
   top_element = stack.pop() if stack else "#"
   ```

2. **Using same opening bracket for all closing brackets**:

   ```python
   # WRONG: All brackets treated as same
   if char == ')' or char == ']' or char == '}':
       if stack.pop() != '(':
           return False

   # CORRECT: Use mapping for each type
   mapping = {")":"(", "]":"[", "}":"{"}
   ```

3. **Checking stack.empty() as string**:

   ```python
   # WRONG: non-empty list is truthy
   if not stack:  # This is correct in Python

   # But writing it as:
   if len(stack) != 0:  # More verbose but also correct

   # WRONG: Returning stack instead of bool
   return stack  # Returns list or empty list, not True/False

   # CORRECT:
   return not stack  # Returns True if empty, False if not
   ```

4. **Assuming stack must match immediately**:

   ```python
   # CORRECT: Stack processes characters in order
   # '(' added first, ')' checks against it
   # No "skipping" of brackets
   ```

5. **Not handling all bracket types in mapping**:

   ```python
   # WRONG: Missing bracket types
   mapping = {")":"("}  # Only handles ()

   # CORRECT: Include all types
   mapping = {")":"(", "}":"{", "]":"["}
   ```

6. **Modifying string during iteration**:

   ```python
   # WRONG: Replace in the string being iterated
   for char in s:
       s = s.replace(...)  # Doesn't affect current iteration

   # CORRECT: Stack doesn't modify input
   ```

## Optimization Notes

The implemented solution is **optimal for this problem**:

- **Time**: O(n) - must check every character
- **Space**: O(n) - worst case needs to store all opening brackets
- **Single pass**: Can't improve further

**Interview tips**:

- Start with stack solution (natural fit)
- Explain why stack is LIFO for matching
- Walk through example with multiple bracket types
- Discuss how to handle edge cases (empty, extra closing)
- Mention space-time trade-off with alternatives
- Note that string replacement is slower

**Key insight for interviews**:

```
Why stack is perfect for bracket matching:

Problem: Brackets must match AND be in correct order

Stack property (LIFO):
  - Last opening bracket should be closed first
  - Stack naturally remembers most recent opening
  - Perfect match for "last-in-first-out" brackets

Example: "([)]"
  Process '(' → push to stack
  Process '[' → push to stack
  Process ')' → must match '[' on top
             but ')' matches '(', not '[']
             → Invalid!

If it was "([])":
  Process '(' → push
  Process '[' → push
  Process ']' → matches '[' on top ✓
  Process ')' → matches '(' on top ✓
```

## Problem Variants

This is a gateway problem to other matching problems:

| Variant                                    | Challenge                           |
| ------------------------------------------ | ----------------------------------- |
| Score of Parentheses                       | Calculate score based on nesting    |
| Minimum Add to Valid                       | Find how many chars to add          |
| Remove Invalid Parentheses                 | Find longest valid substring        |
| Longest Valid Parentheses                  | Find longest valid substring length |
| Check If Word is Valid After Substitutions | Handle string substitutions         |

## Visual Example

```
Valid: "()"
  Stack: []
  ( → Stack: ['(']
  ) → Top = '(', mapping[')'] = '('
     Match! ✓
     Pop → Stack: []
  Result: Empty stack = Valid ✓


Invalid: "([)]"
  Stack: []
  ( → Stack: ['(']
  [ → Stack: ['(', '[']
  ) → Top = '[', mapping[')'] = '('
     '[' != '(' ✗
     Mismatch! Return False
  Result: Invalid ✓


Valid: "{[()]}"
  Stack: []
  { → Stack: ['{']
  [ → Stack: ['{', '[']
  ( → Stack: ['{', '[', '(']
  ) → Top = '(', mapping[')'] = '('
     Match! Pop
     Stack: ['{', '[']
  ] → Top = '[', mapping[']'] = '['
     Match! Pop
     Stack: ['{']
  } → Top = '{', mapping['}'] = '{'
     Match! Pop
     Stack: []
  Result: Empty stack = Valid ✓


Invalid: "((())"
  Stack: []
  ( → Stack: ['(']
  ( → Stack: ['(', '(']
  ( → Stack: ['(', '(', '(']
  ) → Match ✓ Stack: ['(', '(']
  ) → Match ✓ Stack: ['(']
  End: Stack not empty!
  Result: Invalid ✓
```

## Test Cases

```python
# Basic cases
isValid("()")                      # True
isValid("()[]{}")                  # True
isValid("(]")                      # False

# Nesting
isValid("([)]")                    # False (wrong order)
isValid("([{<>}])")                # True (proper nesting) - if < > allowed
isValid("{[]}")                    # True

# Multiple same types
isValid("((()))")                  # True
isValid("((())")                   # False (missing closing)

# Extra brackets
isValid("())")                     # False (extra closing)
isValid("(())")                    # True

# Edge cases
isValid("")                        # True (empty)
isValid("(")                       # False (only opening)
isValid(")")                       # False (only closing)

# Complex valid
isValid("([{}])")                  # True
isValid("{[]()}")                  # True

# All same type
isValid("(()()())")                # True
isValid("(((())))")                # True

# Deeply nested
isValid("[[[[[")                   # False

# Long valid sequence
isValid("()[]" * 1000)             # True

# Large input
isValid("(" * 5000 + ")" * 5000)  # True
```

## Thought Process

**Problem analysis**:

- Three types of brackets: (), [], {}
- Each closing bracket must match corresponding opening
- Brackets must be in correct nesting order
- No crossing allowed

**Key observations**:

1. Most recent opening bracket should be closed first
2. Can't skip brackets - must close from inside out
3. Need to track matching pairs

**Naive approach**:

```
Check all pairs:
  If see '(', find matching ')'
  If see '[', find matching ']'

But this is slow and complex
```

**Better approach - Stack**:

```
Stack is LIFO (Last In First Out)
This matches bracket nesting (innermost first)

For each closing bracket:
  Check if it matches most recent opening
  Most recent = top of stack

If all brackets matched and stack empty → Valid
```

**Why stack**:

- Brackets nest like function calls (LIFO)
- Stack is natural data structure for LIFO
- Push opening brackets, pop when closing
- If mismatch at any point → Invalid
- If stack not empty at end → Invalid

**Interview strategy**:

1. Explain bracket matching requirement
2. Note that nesting is LIFO
3. Suggest stack as natural solution
4. Walk through example with multiple types
5. Code the solution
6. Analyze time/space
7. Discuss how to handle edge cases

This problem teaches:

- Stack data structure usage
- LIFO principle application
- Hash map for lookups
- Edge case handling
- Character processing

## Related Problems

- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
- [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)
- [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/)
- [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)
- [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
