# Valid Anagram

## Problem Summary

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of another, using all original letters exactly once.

**Example**: `"anagram"` and `"nagaram"` are anagrams

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True
```

### How It Works

### Strategy

**Approach 1 (Active): Frequency comparison via count()**

- Check if lengths differ → return False immediately.
- Iterate through each unique character in `s`.
- For each character, compare `s.count(char)` with `t.count(char)`.
- If any count differs, return False; otherwise return True.

Implementation:

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True
```

**Why It Works**

- Anagrams have identical character frequencies.
- By checking that every character in `s` has the same count in `t`, and that lengths match, we verify they're anagrams.
- Using `set(s)` ensures we only check each unique character once.

**Complexity (Approach 1)**

- Time: O(n²) worst case — for each of k unique chars, `count()` scans the string (O(n)). If k = n (all unique), this is O(n²).
- Space: O(k) for the set of unique characters.

**Alternative Approaches (commented in file)**

**Approach 2: Fixed-size frequency array (ASCII)**

```python
count1 = [0] * 256
count2 = [0] * 256
for char in s:
    count1[ord(char)] += 1
for char in t:
    count2[ord(char)] += 1
return count1 == count2 if len(s) == len(t) else False
```

- Time: O(n + 256) = O(n)
- Space: O(1) (fixed 256-element arrays)
- Best for ASCII-only strings

**Approach 3: Character set check**

```python
for char in "abcdefghijklmnopqrstuvwxyz":
    if s.count(char) != t.count(char):
        return False
return set(s) == set(t)
```

- Time: O(26n) = O(n) for lowercase English letters only
- Assumes input is lowercase English alphabet

**Approach 4: Stack/list removal**

```python
stack = list(s)
for char in t:
    if char in stack:
        stack.remove(char)
return len(stack) == 0
```

- Time: O(n²) due to `list.remove()` being O(n) per call
- Space: O(n)
- Inefficient; not recommended

**Approach 5: Sorting (most concise)**

```python
return sorted(s) == sorted(t)
```

- Time: O(n log n) for sorting
- Space: O(n) for sorted lists
- Clean and simple; optimal for most practical cases

**Recommended Approaches**

1. **Sorting** (Approach 5): Most concise, O(n log n), works for all Unicode. Best choice for clean code.
2. **Counter from collections**: `Counter(s) == Counter(t)` — O(n), clean, pythonic.
3. **Fixed array** (Approach 2): O(n), best performance for ASCII-only, manual but efficient.

**Edge Cases**

- Empty strings → both empty returns True
- Different lengths → return False immediately
- Case sensitivity → "Listen" ≠ "silent" (capital L)
- Unicode/special chars → most approaches handle correctly
- All unique vs. all repeated characters → all approaches handle

**Example Testcases (from repository)**

- "anagram", "nagaram" → True
- "rat", "car" → False
- "hello", "hell" → False (different lengths)
- "Listen", "silent" → False (case-sensitive)
- "", "" → True (both empty)
- "astronomer", "moonstarer" → True

**Thought Process / Design Choices**

- Current active approach (Approach 1) works but is O(n²).
- Approach 5 (sorting) is simpler and faster for typical inputs: `return sorted(s) == sorted(t)`.
- For performance-critical code with ASCII only, use Approach 2.
- For Unicode with good performance, use `Counter(s) == Counter(t)` from collections.

**Common Pitfalls**

- Forgetting to check length first → wastes computation.
- Using `set(s) == set(t)` alone → ignores character frequencies (e.g., "ab" vs. "aab").
- Case sensitivity → convert to lowercase if problem allows: `sorted(s.lower()) == sorted(t.lower())`.

### Why Stack Works

The stack approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient stack solution
- Clear and maintainable code

### Disadvantages

- May require additional space
