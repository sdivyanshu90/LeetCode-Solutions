# Longest Palindrome

## Problem Summary

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

**LeetCode Problem**: [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

## Approach 1: Greedy with Set (Implemented)

### Strategy

The implemented solution uses a **greedy set-based approach**:

1. Use a set to track characters with odd occurrences
2. When we see a character for the second time (forming a pair), remove it from the set and add 2 to result
3. After processing all characters, if the set is not empty, we can add 1 more for the center of the palindrome
4. Return the total length

**Code**:

```python
def longestPalindrome(self, s: str) -> int:
    character_set = set()
    res = 0

    # Loop over characters in the string
    for c in s:
        # If set contains the character, match found
        if c in character_set:
            character_set.remove(c)
            # Add the two occurrences to our palindrome
            res += 2
        else:
            # Add the character to the set
            character_set.add(c)

    # If any character remains, we have at least one unmatched
    # character to make the center of an odd length palindrome.
    if character_set:
        res += 1

    return res
```

### How It Works

**Example 1**: `s = "abccccdd"`

```
Character 'a':
  - Not in set, add to set
  - Set: {'a'}, Result: 0

Character 'b':
  - Not in set, add to set
  - Set: {'a', 'b'}, Result: 0

Character 'c':
  - Not in set, add to set
  - Set: {'a', 'b', 'c'}, Result: 0

Character 'c':
  - In set! Remove from set, add 2 to result
  - Set: {'a', 'b'}, Result: 2

Character 'c':
  - Not in set, add to set
  - Set: {'a', 'b', 'c'}, Result: 2

Character 'c':
  - In set! Remove from set, add 2 to result
  - Set: {'a', 'b'}, Result: 4

Character 'd':
  - Not in set, add to set
  - Set: {'a', 'b', 'd'}, Result: 4

Character 'd':
  - In set! Remove from set, add 2 to result
  - Set: {'a', 'b'}, Result: 6

After loop: Set not empty (has 'a' or 'b'), add 1 for center
Final result: 7

Possible palindrome: "dccaccd" or "dccbccd"
```

**Example 2**: `s = "a"`

```
Character 'a':
  - Not in set, add to set
  - Set: {'a'}, Result: 0

After loop: Set not empty, add 1 for center
Final result: 1
```

### Key Insight: Pairing Strategy

**Palindrome properties**:

- Characters can be **paired** (mirrored on both sides)
- At most **one character** can have an odd count (goes in the center)

**Algorithm logic**:

- Each time we find a pair (character appears twice), we can use both in the palindrome
- Unpaired characters stay in the set
- If any unpaired characters remain, we can use one as the center

### Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the string
- **Space Complexity**: O(1) - Set can have at most 52 characters (26 lowercase + 26 uppercase)

### Edge Cases Handled

- **Single character**: `"a"` → 1 (the character itself)
- **All pairs**: `"abcdabcd"` → 8 (all can be paired, no center needed)
- **All same character**: `"aaaa"` → 4 (all pairs)
- **No pairs**: `"abc"` → 1 (use one as center)
- **Case sensitive**: `"Aa"` → 1 ('A' and 'a' are different)

## Approach 2: Count with Hash Map

Count character frequencies and build palindrome based on counts:

```python
from collections import Counter

def longestPalindrome(self, s: str) -> int:
    counts = Counter(s)
    result = 0
    odd_found = False

    for count in counts.values():
        if count % 2 == 0:
            result += count
        else:
            result += count - 1
            odd_found = True

    # Add 1 if we found any odd count (for center)
    if odd_found:
        result += 1

    return result
```

### How It Works

1. Count frequency of each character
2. For even counts: Add entire count to result (all can be paired)
3. For odd counts: Add count-1 (pair what we can, save remainder for center)
4. If any odd count exists, add 1 for center

### Example

```
s = "abccccdd"
Counts: {'a': 1, 'b': 1, 'c': 4, 'd': 2}

'a': count=1 (odd) → add 0, mark odd_found
'b': count=1 (odd) → add 0, mark odd_found
'c': count=4 (even) → add 4
'd': count=2 (even) → add 2

Result: 0 + 0 + 4 + 2 = 6
odd_found = True, so add 1
Final: 7
```

### Complexity

- **Time**: O(n) - Count characters, iterate counts
- **Space**: O(k) where k is number of unique characters (at most 52)

### When to Use

- When you want explicit frequency counting
- More intuitive for some people
- Same performance as set approach

## Approach 3: Simplified Counter

More concise version using Counter:

```python
from collections import Counter

def longestPalindrome(self, s: str) -> int:
    counts = Counter(s)
    result = sum(v // 2 * 2 for v in counts.values())

    # If result < len(s), there's at least one odd count, add 1 for center
    return result + (result < len(s))
```

### How It Works

- `v // 2 * 2`: Get the largest even number ≤ v
  - If v=4: 4//2\*2 = 4 (use all)
  - If v=3: 3//2\*2 = 2 (use 2, leave 1)
  - If v=1: 1//2\*2 = 0 (leave 1)
- If `result < len(s)`, we left some characters out → add 1 for center

### Complexity

- **Time**: O(n)
- **Space**: O(k)

### Advantages

- Very concise
- Clever trick: `result < len(s)` detects odd counts
- Same performance

## Approach 4: Bit Manipulation

Use bit vector to track odd counts:

```python
def longestPalindrome(self, s: str) -> int:
    odd_bits = 0

    for c in s:
        bit_pos = ord(c)
        odd_bits ^= (1 << bit_pos)

    # Count set bits (characters with odd counts)
    odd_count = bin(odd_bits).count('1')

    # Use all characters except odd ones, but keep one odd for center
    return len(s) - odd_count + (odd_count > 0)
```

### How It Works

- Use XOR to toggle bits (even occurrences → 0, odd → 1)
- Count set bits to find characters with odd counts
- Formula: `total - odd_chars + 1 (if any odd)`

### Complexity

- **Time**: O(n)
- **Space**: O(1) - Just an integer for bits

### Drawback

- More complex, less readable
- No real performance benefit
- Clever but not recommended for interviews

## Comparison of Approaches

| Approach           | Time | Space  | Pros                        | Cons                             |
| ------------------ | ---- | ------ | --------------------------- | -------------------------------- |
| Greedy with Set    | O(n) | O(1)\* | Clean, efficient, intuitive | Requires understanding set logic |
| Counter + Iterate  | O(n) | O(k)   | Clear logic, easy to follow | Slightly more code               |
| Simplified Counter | O(n) | O(k)   | Very concise                | Clever trick less obvious        |
| Bit Manipulation   | O(n) | O(1)   | Space efficient             | Complex, not readable            |

\*O(1) because at most 52 unique characters (26 lowercase + 26 uppercase)

## Mathematical Foundation

### Palindrome Construction Rules

For a palindrome of maximum length:

1. **Use all pairs**: Every character that appears an even number of times can be fully used
2. **Handle odd counts**: For characters with odd counts, use (count-1) and save one for center
3. **One center character**: At most one character can have an odd count in the final palindrome

### Formula

Given character frequencies:

```
Length = Σ(count // 2 * 2) + (any odd count exists ? 1 : 0)
```

Or equivalently:

```
Length = (total characters) - (odd count chars) + (at least one odd ? 1 : 0)
```

### Why It Works

**Example**: `s = "aabbbcc"`

- Frequencies: a=2, b=3, c=2
- Pairs: a=2, b=2, c=2 → total 6
- Odd remainder: b has 1 extra → add as center
- Palindrome: "cabbbac" (length 7)

The set approach efficiently tracks which characters have odd counts without explicit counting.

## Edge Cases & Considerations

1. **Single Character**:

   - `"a"` → 1
   - Character itself is a palindrome

2. **All Characters Pair**:

   - `"aabbcc"` → 6
   - No center needed, all paired

3. **No Pairs Possible**:

   - `"abc"` → 1
   - Use any one character as center

4. **All Same Character**:

   - `"aaaa"` → 4 (even count, all paired)
   - `"aaaaa"` → 5 (odd count, 4 paired + 1 center)

5. **Case Sensitivity**:

   - `"Aa"` → 1
   - 'A' and 'a' are different characters
   - Cannot pair them

6. **Mixed Even and Odd**:

   - `"abccccdd"` → 7
   - c pairs 4, d pairs 2, one of {a,b} as center

7. **Long Strings**:
   - Algorithm handles efficiently in O(n) time
   - Set size limited by alphabet size

## Common Pitfalls

1. **Forgetting the Center Character**:

   ```python
   # WRONG: Only counting pairs
   return res

   # CORRECT: Add 1 if any odd-count character remains
   if character_set:
       res += 1
   return res
   ```

2. **Treating Case-Insensitive**:

   ```python
   # WRONG: 'A' and 'a' are different
   s = s.lower()  # Don't do this!

   # CORRECT: Treat uppercase and lowercase as distinct
   ```

3. **Counting All Odd Characters for Center**:

   ```python
   # WRONG: Adding all odd count characters
   return res + len(character_set)

   # CORRECT: Only add 1 for center (not all odd chars)
   return res + (1 if character_set else 0)
   ```

4. **Using Count Instead of Pairs**:

   ```python
   # WRONG: Adding the count
   if c in character_set:
       character_set.remove(c)
       res += 1  # Wrong! Should be +2 for the pair

   # CORRECT: Add 2 for the matching pair
   res += 2
   ```

5. **Not Using Greedy Strategy**:
   - Some try to track specific characters for center
   - Greedy works: use all pairs, any leftover for center
   - Don't overthink which character goes in center

## Optimization Notes

The set-based approach is **optimal**:

- O(n) time - single pass, unavoidable
- O(1) space - limited alphabet size
- Clean and efficient

No further optimization possible without changing problem constraints.

**Micro-optimizations**:

- Set operations (add/remove) are O(1) average
- Counter approach has same complexity but more overhead
- Bit manipulation saves space but adds complexity

## Why the Set Approach is Elegant

The key insight:

- **Set tracks characters with odd counts**
- When a character appears twice consecutively in our processing, it forms a pair
- We immediately count that pair (add 2) and remove from set
- Whatever remains in the set has odd occurrences
- We can use one odd-count character as the center

This is more elegant than counting all frequencies first because:

1. Single pass
2. Minimal storage (set never has more than alphabet size)
3. Natural pairing detection

## Test Cases

```python
# Basic cases
longestPalindrome("abccccdd")        # 7 (dccaccd or similar)
longestPalindrome("a")               # 1
longestPalindrome("bb")              # 2

# Case sensitivity
longestPalindrome("Aa")              # 1 (different chars)
longestPalindrome("AaBbCc")          # 1

# All same
longestPalindrome("aaaa")            # 4 (even count)
longestPalindrome("aaaaa")           # 5 (odd count)

# No pairs
longestPalindrome("abc")             # 1
longestPalindrome("abcdef")          # 1

# All pairs
longestPalindrome("aabbcc")          # 6
longestPalindrome("abcdabcd")        # 8

# Mixed
longestPalindrome("ababa")           # 5 (aabaa or ababa)
longestPalindrome("ababbc")          # 5 (baaab or similar)
longestPalindrome("ccc")             # 3
longestPalindrome("aabbccdde")       # 9 (8 pairs + 1 center)

# Long strings
longestPalindrome("a" * 1000)        # 1000
longestPalindrome("ab" * 500)        # 1000
```

## Thought Process

The problem asks for the **length** of the longest palindrome we can build (not the palindrome itself).

**Key observations**:

1. Palindromes are symmetric - characters mirror around the center
2. Each character (except possibly center) must appear in **pairs**
3. We want to maximize length → use as many characters as possible

**Strategy**:

- **Pair characters**: For characters appearing multiple times, pair them
- **Odd counts**: If a character appears an odd number of times, pair what we can and use the remainder for center
- **At most one center**: Only one character can have an odd count in the final palindrome

**Implementation choice**:

- **Set approach**: Efficiently detects pairs without explicit counting
- **Counter approach**: More explicit but same complexity
- Set is more elegant for this specific problem

The greedy strategy works: use all possible pairs + at most one center character.

## Related Problems

- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)
- [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
