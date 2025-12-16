# Find the Difference — Explanation, Approach, Complexity

Problem summary

- Given two strings `s` and `t` where `t` is `s` with one extra character added (possibly rearranged), find and return that extra character.
- Example: s = "abcd", t = "abcde" → "e"

Current approach (character frequency counting)

- For each character in `t`, count its occurrences in both `s` and `t`.
- If the count in `t` is different from the count in `s`, that character is the difference.
- Return the first character found with different counts.

Why this works

- Since `t` is `s` with one extra character added, exactly one character will have a higher frequency in `t` than in `s`.
- Iterating through `t` and comparing counts ensures we find that character.

Time complexity

- Current implementation: O(n²) — for each of m characters in `t`, we call `count()` which scans both strings (O(n) each where n = len(s) + 1).
- This is inefficient for large strings.

Space complexity

- O(1) — no extra data structures beyond a few variables.

**⚠️ Inefficiency notice and optimizations**

The current solution is **inefficient** for large inputs due to repeated `count()` calls. Here are better approaches:

**Approach 1: Character frequency map (Recommended)**

```python
def findTheDifference(self, s: str, t: str) -> str:
    from collections import Counter
    count_s = Counter(s)
    count_t = Counter(t)
    for char in count_t:
        if count_t[char] != count_s[char]:
            return char
```

- Time: O(n) — single pass for each Counter, then iterate distinct chars.
- Space: O(k) where k = number of distinct characters (at most 26 for lowercase English).

**Approach 2: XOR bitwise (Clever)**

```python
def findTheDifference(self, s: str, t: str) -> str:
    result = 0
    for char in s:
        result ^= ord(char)
    for char in t:
        result ^= ord(char)
    return chr(result)
```

- Time: O(n) — two passes through the strings.
- Space: O(1) — only a single integer.
- Idea: XOR cancels out all characters that appear in both strings; only the extra character remains.

**Approach 3: Sum of ASCII values**

```python
def findTheDifference(self, s: str, t: str) -> str:
    return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))
```

- Time: O(n).
- Space: O(1).
- Idea: the difference in total ASCII values is the extra character's ASCII value.

Edge cases

- Empty `s` → `t` has exactly one character; return it.
- Single character difference → handled correctly.
- Repeated characters → frequency comparison handles duplicates.
- Unicode characters → works with any character encoding.

Example testcases (from repository)

- "abcd", "abcde" → "e"
- "", "y" → "y"
- "a", "aa" → "a"
- "aabbcc", "abcbcad" → "d"
- "zzzz", "zzzzz" → "z"

Recommendation

- **Use Approach 2 (XOR)** for the best balance of simplicity, O(n) time, and O(1) space.
- **Use Approach 1 (Counter)** if readability is prioritized over space.
- Avoid the current implementation for large inputs.

Notes

- The problem guarantees exactly one extra character, so we don't need to handle multiple differences.
- The extra character could be at any position (beginning, middle, or end) after rearrangement.
