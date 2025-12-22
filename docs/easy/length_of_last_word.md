# Length of Last Word

## Problem Summary

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string. A **word** is a maximal substring consisting of non-space characters only.

**LeetCode Problem**: [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

## Approach 1: Split and Access Last Element (Implemented)

### Strategy

The implemented solution uses Python's built-in **string splitting**:

1. Split the string by whitespace using `split()`
2. Access the last element of the resulting list
3. Return the length of that last word

**Code**:

```python
def lengthOfLastWord(self, s: str) -> int:
    ans = s.split()
    return len(ans[len(ans)-1])
```

**Simplified version**:

```python
def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])
```

### How It Works

**Example 1**: `s = "Hello World"`

```
s.split() → ["Hello", "World"]
Last element: "World"
Length: 5
```

**Example 2**: `s = "   fly me   to   the moon  "`

```
s.split() → ["fly", "me", "to", "the", "moon"]
Last element: "moon"
Length: 4
```

**Example 3**: `s = "luffy is still joyboy"`

```
s.split() → ["luffy", "is", "still", "joyboy"]
Last element: "joyboy"
Length: 6
```

### Why `split()` is Powerful

Python's `split()` without arguments:

- Splits on **any whitespace** (spaces, tabs, newlines)
- **Removes empty strings** from result
- Automatically handles multiple consecutive spaces
- Handles leading and trailing spaces

### Complexity Analysis

- **Time Complexity**: O(n) - Must scan entire string to split
- **Space Complexity**: O(n) - Creates list of words

### Edge Cases Handled

- **Trailing spaces**: `"Hello World  "` → Handled by `split()`
- **Leading spaces**: `"  Hello World"` → Handled by `split()`
- **Multiple spaces**: `"a  b    c"` → `split()` handles correctly
- **Single word**: `"Python"` → Returns length of that word
- **Tabs/newlines**: `"Hello\tWorld"` → `split()` handles all whitespace

## Approach 2: Reverse Iteration

Iterate from the end of the string, skipping trailing spaces:

```python
def lengthOfLastWord(self, s: str) -> int:
    length = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count characters in last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length
```

### How It Works

1. Start from the end of string
2. Skip all trailing spaces
3. Count characters until we hit a space or beginning
4. Return the count

### Example

```
s = "   fly me   to   the moon  "
                         ^
Start here, skip spaces

s = "   fly me   to   the moon  "
                         ^
                         n
Count: 1

s = "   fly me   to   the moon  "
                        ^
                       on
Count: 2

... continue until space
Count: 4 (moon)
```

### Complexity

- **Time**: O(n) - Worst case, iterate entire string
- **Space**: O(1) - Only counter variable

### Advantages

- **Space efficient**: No extra data structures
- **Early termination**: Can stop once last word is found
- **Clear logic**: Easy to understand step by step

## Approach 3: Strip and Split from Right

Use `rstrip()` to remove trailing spaces, then split:

```python
def lengthOfLastWord(self, s: str) -> int:
    s = s.rstrip()
    return len(s) - s.rfind(' ') - 1
```

Or alternatively:

```python
def lengthOfLastWord(self, s: str) -> int:
    words = s.rstrip().split()
    return len(words[-1]) if words else 0
```

### How It Works

- `rstrip()`: Remove trailing whitespace
- `rfind(' ')`: Find last space from right
- Calculate length from last space to end

### Complexity

- **Time**: O(n)
- **Space**: O(1) if using `rfind`, O(n) if splitting

### When to Use

- When you want explicit handling of trailing spaces
- Combines built-in methods elegantly

## Approach 4: Regular Expressions

Use regex to find the last word:

```python
import re

def lengthOfLastWord(self, s: str) -> int:
    match = re.findall(r'\S+', s)
    return len(match[-1]) if match else 0
```

Or more specifically:

```python
import re

def lengthOfLastWord(self, s: str) -> int:
    match = re.search(r'\S+\s*$', s)
    return len(match.group().rstrip()) if match else 0
```

### Pattern Explanation

- `\S+`: One or more non-whitespace characters
- `\s*$`: Zero or more spaces at end of string
- `findall(r'\S+', s)`: Find all words

### Complexity

- **Time**: O(n)
- **Space**: O(n) for matches list

### Drawbacks

- Overkill for this problem
- Less readable
- Import overhead
- Slower than simple string operations

## Approach 5: Manual Parsing

Manually parse character by character:

```python
def lengthOfLastWord(self, s: str) -> int:
    length = 0
    in_word = False

    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            in_word = True
            length += 1
        elif in_word:
            break

    return length
```

### Complexity

- **Time**: O(n)
- **Space**: O(1)

### When to Use

- Educational purposes (understanding the algorithm)
- When you can't use built-in methods
- Similar to Approach 2 but with different structure

## Comparison of Approaches

| Approach          | Time | Space | Pros                                      | Cons             |
| ----------------- | ---- | ----- | ----------------------------------------- | ---------------- |
| Split             | O(n) | O(n)  | Concise, Pythonic, handles all whitespace | Uses extra space |
| Reverse Iteration | O(n) | O(1)  | Space efficient, early termination        | More code        |
| Strip + rfind     | O(n) | O(1)  | Elegant, built-in methods                 | Less obvious     |
| Regex             | O(n) | O(n)  | Powerful pattern matching                 | Overkill, slower |
| Manual Parsing    | O(n) | O(1)  | Educational                               | More verbose     |

## Edge Cases & Considerations

1. **Trailing Spaces**:

   - `"Hello World  "` → 5
   - `split()` automatically handles this

2. **Leading Spaces**:

   - `"  Hello World"` → 5
   - `split()` removes leading spaces

3. **Multiple Spaces Between Words**:

   - `"a  b    c"` → 1 (length of "c")
   - `split()` handles multiple spaces correctly

4. **Single Word**:

   - `"Python"` → 6
   - Works correctly

5. **Only Spaces**:

   - `"     "` → Would cause error in implemented version!
   - `split()` returns empty list, accessing `[-1]` raises IndexError
   - **Bug in implementation** (see Common Pitfalls)

6. **Empty String**:

   - `""` → Would cause error!
   - Same issue as only spaces

7. **Tabs and Newlines**:

   - `"Hello\tWorld"` → 5
   - `split()` handles all whitespace types

8. **Single Character**:
   - `"a"` → 1
   - Works correctly

## Common Pitfalls

1. **Not Handling Empty Result from Split**:

   ```python
   # WRONG: Will raise IndexError if s is only spaces or empty
   ans = s.split()
   return len(ans[len(ans)-1])

   # CORRECT: Check if list is not empty
   ans = s.split()
   return len(ans[-1]) if ans else 0
   ```

2. **Using Index Instead of Negative Indexing**:

   ```python
   # Less Pythonic
   return len(ans[len(ans)-1])

   # More Pythonic
   return len(ans[-1])
   ```

3. **Not Using Split's Power**:

   ```python
   # WRONG: Only splits on single space
   ans = s.split(' ')  # Leaves empty strings

   # CORRECT: Splits on all whitespace and removes empties
   ans = s.split()
   ```

4. **Forgetting Trailing Spaces in Manual Approach**:

   - Must skip trailing spaces before counting
   - Reverse iteration approach handles this

5. **Off-by-One Errors**:
   - When using `rfind()`, remember it returns -1 if not found
   - Must handle this edge case

## Bug Fix for Implemented Solution

The current implementation has a bug with empty strings or strings with only spaces:

```python
# Current (buggy)
def lengthOfLastWord(self, s: str) -> int:
    ans = s.split()
    return len(ans[len(ans)-1])  # IndexError if ans is empty

# Fixed version
def lengthOfLastWord(self, s: str) -> int:
    ans = s.split()
    return len(ans[-1]) if ans else 0

# Even cleaner
def lengthOfLastWord(self, s: str) -> int:
    words = s.split()
    return len(words[-1]) if words else 0
```

## Optimization Notes

For this problem, the **split approach is optimal** in Python:

- Clean and readable
- One line of code: `return len(s.split()[-1]) if s.split() else 0`
- Handles all edge cases automatically
- Pythonic and idiomatic

The O(n) space is acceptable for typical inputs, and the clarity is worth it.

For **space optimization**, use the reverse iteration approach:

- O(1) space
- Still O(n) time
- More code but more efficient memory usage

## Recommended Solution

```python
def lengthOfLastWord(self, s: str) -> int:
    words = s.split()
    return len(words[-1]) if words else 0
```

This is:

- **Concise**: 2 lines
- **Correct**: Handles all edge cases
- **Clear**: Easy to understand
- **Pythonic**: Uses built-in methods idiomatically

## Test Cases

```python
# Regular cases
lengthOfLastWord("Hello World")                    # 5
lengthOfLastWord("   fly me   to   the moon  ")   # 4
lengthOfLastWord("luffy is still joyboy")          # 6

# Edge cases - single word
lengthOfLastWord("Python")                         # 6
lengthOfLastWord("a")                              # 1

# Edge cases - spaces
lengthOfLastWord("Hello World  ")                  # 5 (trailing spaces)
lengthOfLastWord("  Hello World")                  # 5 (leading spaces)
lengthOfLastWord("a  b    c")                      # 1 (multiple spaces)

# Edge cases - empty/spaces only
lengthOfLastWord("")                               # 0
lengthOfLastWord("     ")                          # 0

# Special characters (whitespace)
lengthOfLastWord("Hello\tWorld")                   # 5 (tab)
lengthOfLastWord("Hello\nWorld")                   # 5 (newline)

# Multiple words
lengthOfLastWord("a b c d e f g")                  # 1

# Long word at end
lengthOfLastWord("short supercalifragilisticexpialidocious")  # 34
```

## Thought Process

The problem asks for the length of the last word in a string.

**Key observations**:

1. A "word" is non-space characters
2. We only care about the **last** word
3. Trailing spaces should be ignored
4. Multiple spaces between words don't matter

**Approach considerations**:

- **Simple approach**: Split the string into words, get the last one
- **Space-efficient**: Iterate from the end, count until space

**Python advantage**:

- `split()` without arguments handles all whitespace types
- Automatically removes empty strings
- Makes the solution trivial: `len(s.split()[-1])`

**Trade-off**:

- Split approach: O(n) space, but cleaner code
- Reverse iteration: O(1) space, but more code

For Python and typical inputs, the split approach is preferred for its clarity and Pythonic style.

## Related Problems

- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)
- [434. Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)
