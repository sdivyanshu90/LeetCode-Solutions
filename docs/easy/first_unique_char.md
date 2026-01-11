# First Unique Character in a String

## Problem Summary

- Given a string `s`, find the index of the first character that appears exactly once in the string.
- If no unique character exists, return -1.
- Example: s = "leetcode" → 0 (character 'l' at index 0 appears once)

Approach (two-pass frequency counting)

- **First pass**: Build a frequency map (hash) counting occurrences of each character in the string.
  - Use `hash[char] = hash.get(char, 0) + 1` to count each character.
- **Second pass**: Iterate through the string by index.
  - For each character at index i, check if its frequency is exactly 1.
  - Return the first index where `hash[s[i]] == 1`.
- If no unique character is found after the second pass, return -1.

Why this works (thought process)

- A character is unique only if it appears exactly once in the string.
- We cannot determine uniqueness on the first pass (must see the entire string).
- Two passes ensure we have complete frequency information before searching for the first unique character.
- The second pass returns the index of the first unique character (earliest occurrence).

Time and space complexity

- Time: O(n) — first pass: scan the string once (O(n)); second pass: scan the string once (O(n)). Total: O(n).
- Space: O(k) — frequency map stores at most k distinct characters, where k ≤ 26 for lowercase English letters (or up to ~1000 for Unicode).

Edge cases and robustness

- Empty string → return -1 (no characters, no unique character).
- Single character → return 0 (that character is unique by definition).
- All characters the same ([1, 1, 1, ...]) → return -1 (no unique character).
- All characters unique ([1, 2, 3, ...]) → return 0 (first character is unique).
- Unique character at the beginning, middle, or end → correctly identified by the second pass.
- Case-sensitive: 'a' and 'A' are treated as different characters.

Example testcases (from repository)

- "leetcode" → 0 (first char 'l' is unique)
- "loveleetcode" → 2 (char 'v' at index 2 is unique)
- "aabbcc" → -1 (no unique characters)
- "z" → 0 (single character is unique)
- "aabbc" → 4 (char 'c' at index 4 is unique)
- "" → -1 (empty string)
- "swiss" → 1 (char 'w' at index 1 is unique)
- "abcdef" → 0 (all unique, first is at index 0)

Alternative approaches

- Single-pass with ordered dict: use a data structure like `collections.OrderedDict` or `collections.Counter` + ordered traversal. More elegant but not necessarily faster.
  ```python
  from collections import Counter
  count = Counter(s)
  for i, char in enumerate(s):
      if count[char] == 1:
          return i
  return -1
  ```
- Using `index()` method: for each unique character, find its first and last occurrence index; if they match, it's unique. Less efficient: O(n\*k) where k is the number of distinct characters.

Thought process / design choices

- Two-pass is straightforward and avoids complex data structure overhead.
- Using a simple dict (or Counter) is idiomatic Python and efficient.
- The `.get(char, 0)` pattern is a common way to handle missing keys without explicit checks.

Common pitfalls

- Returning on the first character encountered, before building the frequency map → gives incorrect results.
- Comparing frequency to 0 instead of 1 → finds characters that don't appear (wrong condition).
- Forgetting to return -1 if no unique character is found → implicitly returns None.
- Using `hash` as variable name: while it works, shadowing the built-in `hash()` function is poor practice. Rename to `char_count` or `freq_map`.

Optimization notes

- The current implementation is optimal in terms of time complexity.
- If multiple queries are expected on the same string, precompute the frequency map once.
- For very large strings (millions of characters), the two-pass approach remains O(n) with no algorithmic improvement possible.

Notes

- The solution is clear, readable, and optimal.
- Consider renaming `hash` variable to a more descriptive name like `char_count` to avoid shadowing the built-in.
- This problem is a classic introduction to hash maps / frequency counting.

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
  from collections import Counter
  count = Counter(s)
  for i, char in enumerate(s):
      if count[char] == 1:
          return i
  return -1
  ```

### How It Works

Problem summary

- Given a string `s`, find the index of the first character that appears exactly once in the string.
- If no unique character exists, return -1.
- Example: s = "leetcode" → 0 (character 'l' at index 0 appears once)

Approach (two-pass frequency counting)

- **First pass**: Build a frequency map (hash) counting occurrences of each character in the string.
  - Use `hash[char] = hash.get(char, 0) + 1` to count each character.
- **Second pass**: Iterate through the string by index.
  - For each character at index i, check if its frequency is exactly 1.
  - Return the first index where `hash[s[i]] == 1`.
- If no unique character is found after the second pass, return -1.

Why this works (thought process)

- A character is unique only if it appears exactly once in the string.
- We cannot determine uniqueness on the first pass (must see the entire string).
- Two passes ensure we have complete frequency information before searching for the first unique character.
- The second pass returns the index of the first unique character (earliest occurrence).

Time and space complexity

- Time: O(n) — first pass: scan the string once (O(n)); second pass: scan the string once (O(n)). Total: O(n).
- Space: O(k) — frequency map stores at most k distinct characters, where k ≤ 26 for lowercase English letters (or up to ~1000 for Unicode).

Edge cases and robustness

- Empty string → return -1 (no characters, no unique character).
- Single character → return 0 (that character is unique by definition).
- All characters the same ([1, 1, 1, ...]) → return -1 (no unique character).
- All characters unique ([1, 2, 3, ...]) → return 0 (first character is unique).
- Unique character at the beginning, middle, or end → correctly identified by the second pass.
- Case-sensitive: 'a' and 'A' are treated as different characters.

Example testcases (from repository)

- "leetcode" → 0 (first char 'l' is unique)
- "loveleetcode" → 2 (char 'v' at index 2 is unique)
- "aabbcc" → -1 (no unique characters)
- "z" → 0 (single character is unique)
- "aabbc" → 4 (char 'c' at index 4 is unique)
- "" → -1 (empty string)
- "swiss" → 1 (char 'w' at index 1 is unique)
- "abcdef" → 0 (all unique, first is at index 0)

Alternative approaches

- Single-pass with ordered dict: use a data structure like `collections.OrderedDict` or `collections.Counter` + ordered traversal. More elegant but not necessarily faster.
  ```python
  from collections import Counter
  count = Counter(s)
  for i, char in enumerate(s):
      if count[char] == 1:
          return i
  return -1
  ```
- Using `index()` method: for each unique character, find its first and last occurrence index; if they match, it's unique. Less efficient: O(n\*k) where k is the number of distinct characters.

Thought process / design choices

- Two-pass is straightforward and avoids complex data structure overhead.
- Using a simple dict (or Counter) is idiomatic Python and efficient.
- The `.get(char, 0)` pattern is a common way to handle missing keys without explicit checks.

Common pitfalls

- Returning on the first character encountered, before building the frequency map → gives incorrect results.
- Comparing frequency to 0 instead of 1 → finds characters that don't appear (wrong condition).
- Forgetting to return -1 if no unique character is found → implicitly returns None.
- Using `hash` as variable name: while it works, shadowing the built-in `hash()` function is poor practice. Rename to `char_count` or `freq_map`.

Optimization notes

- The current implementation is optimal in terms of time complexity.
- If multiple queries are expected on the same string, precompute the frequency map once.
- For very large strings (millions of characters), the two-pass approach remains O(n) with no algorithmic improvement possible.

Notes

- The solution is clear, readable, and optimal.
- Consider renaming `hash` variable to a more descriptive name like `char_count` to avoid shadowing the built-in.
- This problem is a classic introduction to hash maps / frequency counting.

### Why Hash Map Works

- A character is unique only if it appears exactly once in the string.
- We cannot determine uniqueness on the first pass (must see the entire string).
- Two passes ensure we have complete frequency information before searching for the first unique character.
- The second pass returns the index of the first unique character (earliest occurrence).

Time and space complexity

- Time: O(n) — first pass: scan the string once (O(n)); second pass: scan the string once (O(n)). Total: O(n).
- Space: O(k) — frequency map stores at most k distinct characters, where k ≤ 26 for lowercase English letters (or up to ~1000 for Unicode).

Edge cases and robustness

- Empty string → return -1 (no characters, no unique character).
- Single character → return 0 (that character is unique by definition).
- All characters the same ([1, 1, 1, ...]) → return -1 (no unique character).
- All characters unique ([1, 2, 3, ...]) → return 0 (first character is unique).
- Unique character at the beginning, middle, or end → correctly identified by the second pass.
- Case-sensitive: 'a' and 'A' are treated as different characters.

Example testcases (from repository)

- "leetcode" → 0 (first char 'l' is unique)
- "loveleetcode" → 2 (char 'v' at index 2 is unique)
- "aabbcc" → -1 (no unique characters)
- "z" → 0 (single character is unique)
- "aabbc" → 4 (char 'c' at index 4 is unique)
- "" → -1 (empty string)
- "swiss" → 1 (char 'w' at index 1 is unique)
- "abcdef" → 0 (all unique, first is at index 0)

Alternative approaches

- Single-pass with ordered dict: use a data structure like `collections.OrderedDict` or `collections.Counter` + ordered traversal. More elegant but not necessarily faster.
  ```python
  from collections import Counter
  count = Counter(s)
  for i, char in enumerate(s):
      if count[char] == 1:
          return i
  return -1
  ```
- Using `index()` method: for each unique character, find its first and last occurrence index; if they match, it's unique. Less efficient: O(n\*k) where k is the number of distinct characters.

Thought process / design choices

- Two-pass is straightforward and avoids complex data structure overhead.
- Using a simple dict (or Counter) is idiomatic Python and efficient.
- The `.get(char, 0)` pattern is a common way to handle missing keys without explicit checks.

Common pitfalls

- Returning on the first character encountered, before building the frequency map → gives incorrect results.
- Comparing frequency to 0 instead of 1 → finds characters that don't appear (wrong condition).
- Forgetting to return -1 if no unique character is found → implicitly returns None.
- Using `hash` as variable name: while it works, shadowing the built-in `hash()` function is poor practice. Rename to `char_count` or `freq_map`.

Optimization notes

- The current implementation is optimal in terms of time complexity.
- If multiple queries are expected on the same string, precompute the frequency map once.
- For very large strings (millions of characters), the two-pass approach remains O(n) with no algorithmic improvement possible.

Notes

- The solution is clear, readable, and optimal.
- Consider renaming `hash` variable to a more descriptive name like `char_count` to avoid shadowing the built-in.
- This problem is a classic introduction to hash maps / frequency counting.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n) — first pass: scan the string once (O(n)); second pass: scan the string once (O(n)). Total: O(n). - Space: O(k) — frequency map stores at most k distinct characters, where k ≤ 26 for lowercase English letters (or up to ~1000 for Unicode). Edge cases and robustness - Empty string → return -1 (no characters, no unique character). - Single character → return 0 (that character is unique by definition). - All characters the same ([1, 1, 1, ...]) → return -1 (no unique character). - All characters unique ([1, 2, 3, ...]) → return 0 (first character is unique). - Unique character at the beginning, middle, or end → correctly identified by the second pass. - Case-sensitive: 'a' and 'A' are treated as different characters. Example testcases (from repository) - "leetcode" → 0 (first char 'l' is unique) - "loveleetcode" → 2 (char 'v' at index 2 is unique) - "aabbcc" → -1 (no unique characters) - "z" → 0 (single character is unique) - "aabbc" → 4 (char 'c' at index 4 is unique) - "" → -1 (empty string) - "swiss" → 1 (char 'w' at index 1 is unique) - "abcdef" → 0 (all unique, first is at index 0) Alternative approaches - Single-pass with ordered dict: use a data structure like `collections.OrderedDict` or `collections.Counter` + ordered traversal. More elegant but not necessarily faster.   ```python   from collections import Counter   count = Counter(s)   for i, char in enumerate(s):       if count[char] == 1:           return i   return -1   ``` - Using `index()` method: for each unique character, find its first and last occurrence index; if they match, it's unique. Less efficient: O(n\*k) where k is the number of distinct characters. Thought process / design choices - Two-pass is straightforward and avoids complex data structure overhead. - Using a simple dict (or Counter) is idiomatic Python and efficient. - The `.get(char, 0)` pattern is a common way to handle missing keys without explicit checks. Common pitfalls - Returning on the first character encountered, before building the frequency map → gives incorrect results. - Comparing frequency to 0 instead of 1 → finds characters that don't appear (wrong condition). - Forgetting to return -1 if no unique character is found → implicitly returns None. - Using `hash` as variable name: while it works, shadowing the built-in `hash()` function is poor practice. Rename to `char_count` or `freq_map`. Optimization notes - The current implementation is optimal in terms of time complexity. - If multiple queries are expected on the same string, precompute the frequency map once. - For very large strings (millions of characters), the two-pass approach remains O(n) with no algorithmic improvement possible. Notes - The solution is clear, readable, and optimal. - Consider renaming `hash` variable to a more descriptive name like `char_count` to avoid shadowing the built-in. - This problem is a classic introduction to hash maps / frequency counting.

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space
