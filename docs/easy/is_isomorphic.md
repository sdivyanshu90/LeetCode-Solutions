# Isomorphic Strings

## Problem Summary

**Problem Summary**
- Given two strings `s` and `t`, determine if they are isomorphic.
- Two strings are isomorphic if the characters in `s` can be replaced to get `t`.
- Each character in `s` must map to exactly one character in `t` (bijection).
- No two characters in `s` may map to the same character in `t`, and vice versa.
- Example: "egg" and "add" are isomorphic (e→a, g→d); "foo" and "bar" are not (o cannot map to both a and r).

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
```

### How It Works

**Problem Summary**

- Given two strings `s` and `t`, determine if they are isomorphic.
- Two strings are isomorphic if the characters in `s` can be replaced to get `t`.
- Each character in `s` must map to exactly one character in `t` (bijection).
- No two characters in `s` may map to the same character in `t`, and vice versa.
- Example: "egg" and "add" are isomorphic (e→a, g→d); "foo" and "bar" are not (o cannot map to both a and r).

**Approach (Set cardinality comparison)**

- Use Python's `zip(s, t)` to create pairs of corresponding characters.
- Compare three set cardinalities:
  - `len(set(zip(s, t)))` — number of unique (s[i], t[i]) pairs
  - `len(set(s))` — number of unique characters in s
  - `len(set(t))` — number of unique characters in t
- Return `True` if all three are equal, `False` otherwise.

Implementation:

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
```

**Why It Works**

- For isomorphic strings, each unique character in `s` maps to exactly one unique character in `t`.
- If `len(set(zip(s, t)))` equals both `len(set(s))` and `len(set(t))`, it means:
  - No character in `s` maps to multiple characters in `t` (checked by `len(set(zip(s, t))) == len(set(s))`)
  - No two characters in `s` map to the same character in `t` (checked by `len(set(t))` equality)
  - The mapping is bijective (one-to-one correspondence)

**Examples Demonstrating the Logic**

1. "egg" and "add" → zip pairs: {(e,a), (g,d), (g,d)} → 2 unique pairs, 2 unique in s, 2 unique in t → True
2. "foo" and "bar" → zip pairs: {(f,b), (o,a), (o,r)} → 3 unique pairs, 2 unique in s, 3 unique in t → False
3. "abca" and "bdbc" → zip pairs: {(a,b), (b,d), (c,b), (a,c)} → 4 unique pairs, 3 unique in s, 3 unique in t → False

**Complexity**

- Time: O(n) where n = len(s) = len(t)
  - Creating zip: O(n)
  - Creating sets: O(n) each
  - Comparing lengths: O(1)
- Space: O(n) for the sets

**Edge Cases**

- Empty strings → return True (vacuously isomorphic)
- Single character → return True
- Different lengths → the problem guarantees equal lengths; if not, zip truncates to shorter length
- Identical strings → return True (identity mapping)
- Unicode characters → works correctly with any characters

**Alternative Approaches**

**Approach 1: Hash map bidirectional mapping**

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True
```

- Time: O(n), Space: O(k) where k = number of unique characters
- More explicit but verbose; easier to understand for beginners

**Approach 2: Single pass with transformation check**

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    return [s.index(c) for c in s] == [t.index(c) for c in t]
```

- Time: O(n²) due to repeated `index()` calls
- Space: O(n)
- Less efficient but very concise

**Thought Process / Design Choices**

- The set cardinality approach is elegant and Pythonic.
- It leverages the mathematical property that a bijection exists iff the cardinalities match.
- One-liner solution with optimal O(n) complexity.
- More intuitive than tracking explicit mappings once you understand the set logic.

**Common Pitfalls**

- Only checking one direction of mapping → must verify both s→t and t→s are injective.
- Not handling repeated characters correctly → the set approach naturally handles this.
- Assuming different lengths → problem typically guarantees equal lengths.
- Using `set(s) == set(t)` alone → incorrect, as "ab" and "aa" would pass but aren't isomorphic.

**Example Testcases (from repository)**

- "egg", "add" → True
- "foo", "bar" → False (2 unique in s, 3 unique in t)
- "paper", "title" → True
- "badc", "baba" → False (4 unique in s, 2 unique in t)
- "", "" → True
- "a", "b" → True
- "abca", "bdbc" → False (a maps to both b and c)

**Key Insight**

- Isomorphism requires a bijective (one-to-one and onto) mapping.
- Checking that the number of unique pairs equals the number of unique characters in each string verifies this bijection.

### Why Hash Map Works

The hash map approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space
