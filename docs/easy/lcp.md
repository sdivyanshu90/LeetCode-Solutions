# Longest Common Prefix

## Problem Summary

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

**LeetCode Problem**: [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Approach 1: Horizontal Scanning (Implemented)

### Strategy

The implemented solution uses a **horizontal scanning approach**:

1. Start with the first string as the initial prefix
2. For each subsequent string, reduce the prefix until it matches the beginning of that string
3. Shorten the prefix by removing the last character in each iteration
4. If the prefix becomes empty, return `""` (no common prefix)
5. Return the final prefix after checking all strings

**Code**:

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
```

### How It Works

**Example 1**: `strs = ["flower", "flow", "flight"]`

```
Initial: prefix = "flower"

String 2: "flow"
  - "flow"[:6] = "flow" ≠ "flower"
  - Shorten: prefix = "flowe"
  - "flow"[:5] = "flow" ≠ "flowe"
  - Shorten: prefix = "flow"
  - "flow"[:4] = "flow" == "flow" ✓

String 3: "flight"
  - "flight"[:4] = "flig" ≠ "flow"
  - Shorten: prefix = "flo"
  - "flight"[:3] = "fli" ≠ "flo"
  - Shorten: prefix = "fl"
  - "flight"[:2] = "fl" == "fl" ✓

Result: "fl"
```

**Example 2**: `strs = ["dog", "racecar", "car"]`

```
Initial: prefix = "dog"

String 2: "racecar"
  - "racecar"[:3] = "rac" ≠ "dog"
  - Shorten: prefix = "do"
  - "racecar"[:2] = "ra" ≠ "do"
  - Shorten: prefix = "d"
  - "racecar"[:1] = "r" ≠ "d"
  - Shorten: prefix = ""
  - Empty prefix, return ""

Result: ""
```

### Complexity Analysis

- **Time Complexity**: O(S) where S is the sum of all characters in all strings
  - In the worst case, we compare every character
  - For n strings with average length m: O(n × m)
- **Space Complexity**: O(1) - Only storing the prefix (which is a substring of input)

### Edge Cases Handled

- **Empty array**: `strs = []` → `""` (handled by initial check)
- **Single string**: `strs = ["a"]` → `"a"` (loop doesn't execute)
- **Empty string in array**: `strs = ["", "b"]` → `""` (prefix becomes empty quickly)
- **Identical strings**: `strs = ["abc", "abc"]` → `"abc"` (prefix matches fully)
- **No common prefix**: Returns `""` when prefix is reduced to empty

## Approach 2: Vertical Scanning

Compare characters at each position across all strings:

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]

    return strs[0]
```

### How It Works

- Compare character at position 0 across all strings
- If all match, move to position 1
- Continue until we find a mismatch or reach end of shortest string
- Return the prefix up to that position

### Example

```
strs = ["flower", "flow", "flight"]

i=0: char='f'
  - flow[0]='f' ✓
  - flight[0]='f' ✓

i=1: char='l'
  - flow[1]='l' ✓
  - flight[1]='l' ✓

i=2: char='o'
  - flow[2]='o' ✓
  - flight[2]='i' ✗

Return: strs[0][:2] = "fl"
```

### Complexity

- **Time**: O(S) - Same as horizontal scanning
- **Space**: O(1)

### Advantage

- Early termination: Stops as soon as first mismatch is found
- More intuitive for some people

## Approach 3: Divide and Conquer

Recursively divide the array and find LCP of subarrays:

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    def lcp_of_two(str1, str2):
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:min_len]

    def divide_and_conquer(left, right):
        if left == right:
            return strs[left]

        mid = (left + right) // 2
        lcp_left = divide_and_conquer(left, mid)
        lcp_right = divide_and_conquer(mid + 1, right)

        return lcp_of_two(lcp_left, lcp_right)

    return divide_and_conquer(0, len(strs) - 1)
```

### How It Works

1. Divide array into two halves
2. Recursively find LCP of each half
3. Find LCP of the two results

### Example

```
strs = ["flower", "flow", "flight", "fling"]

Divide:
  Left: ["flower", "flow"] → LCP = "flow"
  Right: ["flight", "fling"] → LCP = "fli"

Combine: LCP("flow", "fli") = "fl"
```

### Complexity

- **Time**: O(S) - Each character compared once across divide/conquer tree
- **Space**: O(m × log n) - Recursion stack depth log n, each storing string of length m

### When to Use

- Conceptually interesting (divide and conquer practice)
- Parallelizable (can compute left and right independently)
- Not practically better for this problem

## Approach 4: Trie (Advanced)

Build a trie and traverse until branching occurs:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    # Build trie
    root = TrieNode()
    for word in strs:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    # Find LCP by traversing until branch or end
    prefix = []
    node = root
    while len(node.children) == 1 and not node.is_end:
        char = list(node.children.keys())[0]
        prefix.append(char)
        node = node.children[char]

    return "".join(prefix)
```

### Complexity

- **Time**: O(S) - Insert all strings, then traverse
- **Space**: O(S) - Trie stores all unique prefixes

### When to Use

- When you need the trie for other purposes
- Educational exercise
- Overkill for this specific problem

## Approach 5: Binary Search

Binary search on the length of the prefix:

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    def is_common_prefix(length):
        prefix = strs[0][:length]
        for string in strs[1:]:
            if not string.startswith(prefix):
                return False
        return True

    min_len = min(len(s) for s in strs)
    left, right = 0, min_len

    while left <= right:
        mid = (left + right) // 2
        if is_common_prefix(mid):
            left = mid + 1
        else:
            right = mid - 1

    return strs[0][:right]
```

### Complexity

- **Time**: O(S × log m) where m is length of shortest string
- **Space**: O(1)

### When to Use

- Interesting application of binary search
- Can be faster when strings are very long and LCP is short
- Generally not better than simpler approaches

## Comparison of Approaches

| Approach         | Time       | Space      | Pros                     | Cons                        |
| ---------------- | ---------- | ---------- | ------------------------ | --------------------------- |
| Horizontal Scan  | O(S)       | O(1)       | Simple, clean, efficient | May check unnecessary chars |
| Vertical Scan    | O(S)       | O(1)       | Early termination        | Similar to horizontal       |
| Divide & Conquer | O(S)       | O(m log n) | Parallelizable           | Extra space, complex        |
| Trie             | O(S)       | O(S)       | Elegant data structure   | Overkill, extra space       |
| Binary Search    | O(S log m) | O(1)       | Interesting approach     | Usually not faster          |

**S** = sum of all characters, **m** = average string length, **n** = number of strings

## Edge Cases & Considerations

1. **Empty Array**:

   - `strs = []` → `""`
   - Handled by initial check

2. **Single String**:

   - `strs = ["hello"]` → `"hello"`
   - Loop never executes, returns first string

3. **Empty String in Array**:

   - `strs = ["", "abc"]` → `""`
   - Empty string causes prefix to become empty immediately

4. **All Identical Strings**:

   - `strs = ["abc", "abc", "abc"]` → `"abc"`
   - Prefix never gets shortened

5. **No Common Prefix**:

   - `strs = ["dog", "racecar", "car"]` → `""`
   - Prefix becomes empty, return `""`

6. **Prefix is Entire First String**:

   - `strs = ["abc", "abcdef", "abcxyz"]` → `"abc"`
   - Works correctly

7. **Very Long Strings**:

   - Algorithm handles efficiently
   - Early termination when prefix is found

8. **One Character Prefix**:
   - `strs = ["a", "ab", "abc"]` → `"a"`
   - Correctly finds single character

## Common Pitfalls

1. **Not Checking for Empty Array**:

   ```python
   # WRONG: Will throw error on empty input
   prefix = strs[0]
   # CORRECT: Check first
   if not strs:
       return ""
   ```

2. **Index Out of Bounds**:

   ```python
   # WRONG: string might be shorter than len(prefix)
   if string[i] != prefix[i]:
       ...
   # CORRECT: Use slicing or check length
   if string[:len(prefix)] != prefix:
       ...
   ```

3. **Infinite Loop**:

   ```python
   # WRONG: Forgetting to shorten prefix
   while string[:len(prefix)] != prefix:
       pass  # Infinite loop!
   # CORRECT: Shorten prefix
   while string[:len(prefix)] != prefix:
       prefix = prefix[:-1]
   ```

4. **Not Checking Empty Prefix**:

   ```python
   # WRONG: Continues even when no common prefix
   while string[:len(prefix)] != prefix:
       prefix = prefix[:-1]
   # CORRECT: Early return on empty prefix
   while string[:len(prefix)] != prefix:
       prefix = prefix[:-1]
       if not prefix:
           return ""
   ```

5. **Off-by-One in Slicing**:
   - Python slicing is forgiving, but be careful with indices
   - `string[:len(prefix)]` is safe even if string is shorter

## Optimization Notes

The horizontal scanning approach is **efficient and practical**:

- O(S) time - must examine each character at least once
- O(1) space - only stores prefix (substring of input)
- Early termination when prefix becomes empty
- Simple and readable

Potential micro-optimizations:

1. **Find shortest string first**: Use it as initial prefix

   ```python
   prefix = min(strs, key=len)
   ```

   This avoids unnecessary shortening.

2. **Check length first**: If any string is empty, return `""`

   ```python
   if any(len(s) == 0 for s in strs):
       return ""
   ```

3. **Vertical scanning**: Can be faster if LCP is short compared to string lengths

For most practical purposes, the implemented solution is optimal.

## Test Cases

```python
# Basic cases
longestCommonPrefix(["flower","flow","flight"])       # "fl"
longestCommonPrefix(["dog","racecar","car"])          # ""

# Edge cases
longestCommonPrefix([])                                # ""
longestCommonPrefix(["a"])                             # "a"
longestCommonPrefix(["", "b"])                         # ""

# All identical
longestCommonPrefix(["test", "test", "test"])         # "test"

# Prefix is entire first string
longestCommonPrefix(["abc", "abcdef", "abcxyz"])      # "abc"

# Single character
longestCommonPrefix(["a", "ab", "abc"])               # "a"
longestCommonPrefix(["c", "c"])                        # "c"

# No common prefix
longestCommonPrefix(["throne", "dungeon"])            # ""

# Long common prefix
longestCommonPrefix(["interspecies","interstellar","interstate"])  # "inters"

# Partial match
longestCommonPrefix(["ab", "a"])                      # "a"

# Many strings
longestCommonPrefix(["a", "a", "a", "a", "a"])        # "a"

# Two strings, one prefix of other
longestCommonPrefix(["flower", "flow"])               # "flow"
```

## Thought Process

The problem asks for the longest string that is a prefix of all strings in the array.

**Key observations**:

1. The LCP cannot be longer than the shortest string
2. If we find the LCP of first two strings, we can compare it with the third, and so on
3. We can start with the first string and progressively shorten it

**Approach selection**:

- **Horizontal scanning**: Start with first string as prefix, reduce until it matches all
- **Vertical scanning**: Compare character by character across all strings
- Both are O(S) time and O(1) space

The implemented horizontal scanning approach is intuitive:

1. Assume first string is the prefix
2. Check each subsequent string
3. If it doesn't start with current prefix, shorten prefix
4. Repeat until prefix matches or becomes empty

This gives us a clean, efficient solution that's easy to understand and implement.

## Related Problems

- [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)
- [1662. Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)
- [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
- [524. Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)
