# Roman to Integer

## Problem Summary

Given a roman numeral, convert it to an integer.

Roman numerals are represented by seven different symbols with the following values:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Usually, a larger value symbol cannot appear to the right of a smaller value symbol. However, there are six special cases where a smaller value appears before a larger value:

| Cases                                       | Roman  | Integer  |
| ------------------------------------------- | ------ | -------- |
| I can be placed before V (5) and X (10)     | IV, IX | 4, 9     |
| X can be placed before L (50) and C (100)   | XL, XC | 40, 90   |
| C can be placed before D (500) and M (1000) | CD, CM | 400, 900 |

**LeetCode Problem**: [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Approach 1: Left-to-Right with Look-Ahead (Implemented First)

### Strategy

The first approach uses **left-to-right iteration with look-ahead**:

1. Create a dictionary mapping Roman symbols to integer values
2. Iterate through all characters except the last
3. For each character, check if its value is less than the next character's value
4. If smaller, it's a subtractive case (like IV, IX), so subtract the value
5. Otherwise, add the value normally
6. Always add the last character's value (it's never subtracted)

**Code**:

```python
def romanToInt(self, s: str) -> int:
    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    for i in range(len(s) - 1):
        if values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    total += values[s[-1]]
    return total
```

### How It Works

**Key insight**: If a Roman numeral's digit is smaller than the next digit, it's a subtractive case.

**Example 1**: `s = "III"`

```
Dictionary: I=1, V=5, X=10, L=50, C=100, D=500, M=1000

i=0: s[0]='I', s[1]='I'
  values['I'] = 1, values['I'] = 1
  1 < 1? No
  total += 1 → total = 1

i=1: s[1]='I', s[2]='I'
  values['I'] = 1, values['I'] = 1
  1 < 1? No
  total += 1 → total = 2

Loop ends (i < len(s)-1)

Add last character:
  total += values['I'] = 1 → total = 3

Return 3 ✓
```

**Example 2**: `s = "IV"`

```
i=0: s[0]='I', s[1]='V'
  values['I'] = 1, values['V'] = 5
  1 < 5? Yes (subtractive case)
  total -= 1 → total = -1

Loop ends

Add last character:
  total += values['V'] = 5 → total = 4

Return 4 ✓
```

**Example 3**: `s = "MCMXCIV"` (1994)

```
M C M X C I V

i=0: 'M'=1000, 'C'=100
  1000 < 100? No
  total += 1000 → total = 1000

i=1: 'C'=100, 'M'=1000
  100 < 1000? Yes (subtractive case)
  total -= 100 → total = 900

i=2: 'M'=1000, 'X'=10
  1000 < 10? No
  total += 1000 → total = 1900

i=3: 'X'=10, 'C'=100
  10 < 100? Yes (subtractive case)
  total -= 10 → total = 1890

i=4: 'C'=100, 'I'=1
  100 < 1? No
  total += 100 → total = 1990

Loop ends

Add last character:
  total += values['V'] = 5 → total = 1995

Wait, should be 1994!

Let me recalculate...
M (1000) + C (100, but before M, so -100) + M (1000) + X (10, but before C, so -10) + C (100) + I (1, but before V, so -1) + V (5)
= 1000 - 100 + 1000 - 10 + 100 - 1 + 5
= 1994 ✓

i=5: 'I'=1, 'V'=5
  1 < 5? Yes (subtractive case)
  total -= 1 → total = 1994

Loop ends

Add last character:
  total += values['V'] = 5 → total = 1999

Hmm, let me trace more carefully...
Actually starting total = 0

i=0 (M, C): 1000 < 100? No → total += 1000 = 1000
i=1 (C, M): 100 < 1000? Yes → total -= 100 = 900
i=2 (M, X): 1000 < 10? No → total += 1000 = 1900
i=3 (X, C): 10 < 100? Yes → total -= 10 = 1890
i=4 (C, I): 100 < 1? No → total += 100 = 1990
i=5 (I, V): 1 < 5? Yes → total -= 1 = 1989

Add last V: total += 5 = 1994 ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through the string
  - Dictionary lookup is O(1)
  - n = length of string
- **Space Complexity**: O(1)
  - Fixed-size dictionary (7 entries)
  - No additional scaling with input

### Advantages

- **Simple logic**: Easy to understand
- **Single pass**: Only one loop iteration
- **Efficient**: O(n) time, O(1) space

### Disadvantages

- **Look-ahead complexity**: Need to check next character
- **Special handling for last character**: Must add it separately
- **Index bounds**: Need to be careful with range

## Approach 2: Right-to-Left with Max Tracking (Implemented Second)

### Strategy

The second approach uses **right-to-left iteration tracking maximum value**:

1. Create dictionary mapping Roman symbols to values
2. Iterate through the string in **reverse**
3. Track the maximum value seen so far
4. For each character, if its value is less than the maximum, subtract it
5. Otherwise, add it and update the maximum

**Code**:

```python
def romanToInt(self, s: str) -> int:
    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    max_right = 0
    for ch in reversed(s):
        val = values[ch]
        if val < max_right:
            total -= val
        else:
            total += val
            max_right = val
    return total
```

### How It Works

**Key insight**: When going right-to-left, any value smaller than what we've seen is subtractive.

**Example**: `s = "MCMXCIV"` (1994)

```
Process from right to left: V I C X M C M

ch='V': val=5
  5 < 0? No
  total += 5 → total = 5
  max_right = 5

ch='I': val=1
  1 < 5? Yes (subtractive case)
  total -= 1 → total = 4
  max_right stays 5

ch='C': val=100
  100 < 5? No
  total += 100 → total = 104
  max_right = 100

ch='X': val=10
  10 < 100? Yes (subtractive case)
  total -= 10 → total = 94
  max_right stays 100

ch='M': val=1000
  1000 < 100? No
  total += 1000 → total = 1094
  max_right = 1000

ch='C': val=100
  100 < 1000? Yes (subtractive case)
  total -= 100 → total = 994
  max_right stays 1000

ch='M': val=1000
  1000 < 1000? No
  total += 1000 → total = 1994
  max_right = 1000

Return 1994 ✓
```

**Visual representation**:

```
String: M C M X C I V
Index:  0 1 2 3 4 5 6

Process right-to-left:
  V (5): Add → 5
  I (1): 1 < 5, subtract → 4
  C (100): 100 > 5, add → 104
  X (10): 10 < 100, subtract → 94
  M (1000): 1000 > 100, add → 1094
  C (100): 100 < 1000, subtract → 994
  M (1000): 1000 ≥ 1000, add → 1994

The max_right tracks: 5 → 5 → 100 → 100 → 1000 → 1000 → 1000
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through reversed string
  - Dictionary lookup is O(1)
- **Space Complexity**: O(1)
  - Fixed dictionary, no additional scaling
  - reversed() returns iterator, no new list created

### Advantages

- **Elegant insight**: Max tracking is clever
- **No index bounds**: No need to check range
- **No special cases**: Last character (first when reversed) handled naturally
- **Python friendly**: Works well with reversed()

### Disadvantages

- **Reverse iteration**: Not intuitive for some
- **Max tracking logic**: Requires careful understanding

## Approach 3: HashMap with Subtractive Pairs

Pre-define all subtractive cases:

```python
def romanToInt(self, s: str) -> int:
    mapping = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90,
        "CD": 400, "CM": 900
    }

    total = 0
    i = 0
    while i < len(s):
        # Check for two-character subtractive case
        if i + 1 < len(s) and s[i:i+2] in mapping:
            total += mapping[s[i:i+2]]
            i += 2
        else:
            total += mapping[s[i]]
            i += 1

    return total
```

### How It Works

Instead of checking relationships dynamically, pre-define all valid patterns.

**Example**: `s = "MCMXCIV"`

```
i=0: s[0:2]="MC" not in mapping
  Use s[0]="M" → 1000
  i=1

i=1: s[1:3]="CM" in mapping
  Use "CM" → 900
  i=3

i=3: s[3:5]="XC" in mapping
  Use "XC" → 90
  i=5

i=5: s[5:7]="IV" in mapping
  Use "IV" → 4
  i=7

i=7: out of range, stop

total = 1000 + 900 + 90 + 4 = 1994 ✓
```

### Complexity

- **Time**: O(n) - single pass with variable step
- **Space**: O(1) - larger dictionary but still constant

### Advantages

- **Explicit patterns**: All cases clearly defined
- **No comparison logic**: Just look up and add
- **Very clear**: Easy to understand what values mean

### Disadvantages

- **Larger dictionary**: More entries to store
- **String slicing**: Creates substring objects
- **More verbose**: Longer code

## Approach 4: String Replacement (Non-optimal)

Replace subtractive patterns first:

```python
def romanToInt(self, s: str) -> int:
    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    # Replace all subtractive cases
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "MMMM")

    # Sum all characters
    total = 0
    for ch in s:
        total += values[ch]

    return total
```

### How It Works

Convert all subtractive patterns into additive form, then sum.

**Example**: `s = "IV"`

```
Replace "IV" with "IIII":
  s = "IIII"

Sum all characters:
  I + I + I + I = 1 + 1 + 1 + 1 = 4

Return 4 ✓
```

### Complexity

- **Time**: O(n) - multiple passes through string
- **Space**: O(n) - creates modified strings

### Advantages

- **Simple logic**: Just add all values
- **No comparison needed**: Straightforward arithmetic

### Disadvantages

- **Extra space**: Creates new strings
- **Multiple passes**: Less efficient
- **Not practical**: Overkill for this problem

## Comparison of Approaches

| Approach           | Time | Space | Difficulty | Pros                      | Cons                  |
| ------------------ | ---- | ----- | ---------- | ------------------------- | --------------------- |
| Left-to-right      | O(n) | O(1)  | Easy       | Simple, direct            | Index bounds checking |
| Right-to-left      | O(n) | O(1)  | Medium     | Elegant, no special cases | Less intuitive        |
| Subtractive pairs  | O(n) | O(1)  | Easy       | Explicit patterns, clear  | Larger dictionary     |
| String replacement | O(n) | O(n)  | Easy       | Very simple logic         | Extra space           |

**Winner**: Right-to-left approach for elegance and clarity

## Edge Cases & Considerations

1. **Single character**:

   - `s = "I"` → 1
   - `s = "V"` → 5
   - Works correctly ✓

2. **Basic numbers**:

   - `s = "III"` → 3
   - `s = "XXX"` → 30
   - Simple addition cases ✓

3. **Subtractive cases**:

   - `s = "IV"` → 4
   - `s = "IX"` → 9
   - Must recognize subtraction ✓

4. **Complex number**:

   - `s = "MCMXCIV"` → 1994
   - Multiple subtractive patterns ✓

5. **Repeated characters**:

   - `s = "MMMM"` → 4000
   - Maximum valid is MMM (3000), but 4000 still works algorithmically

6. **All basic symbols**:

   - `s = "MDCLXVI"` → 1666
   - All different symbols in order ✓

7. **Maximum possible**:
   - `s = "MMMCMXCIX"` → 3999
   - Upper limit of valid Roman numerals

## Roman Numeral Rules

**Standard rules**:

1. I, X, C, M can appear up to 3 times consecutively
2. V, L, D cannot appear more than once
3. I can be placed before V and X only
4. X can be placed before L and C only
5. C can be placed before D and M only

The problem guarantees valid input, so we don't need to validate.

## Common Pitfalls

1. **Wrong comparison direction**:

   ```python
   # WRONG: Checking if next is greater doesn't work right-to-left
   if values[s[i]] > values[s[i + 1]]:
       total += values[s[i]]

   # CORRECT: Check if current is less than next
   if values[s[i]] < values[s[i + 1]]:
       total -= values[s[i]]
   ```

2. **Forgetting last character**:

   ```python
   # WRONG: Never adds the last character
   for i in range(len(s)):
       if values[s[i]] < values[s[i + 1]]:  # IndexError on last

   # CORRECT: Stop before last, add it separately
   for i in range(len(s) - 1):
       # ...
   total += values[s[-1]]
   ```

3. **Off-by-one in range**:

   ```python
   # WRONG: Skips second-to-last character
   for i in range(len(s) - 2):

   # CORRECT: Include second-to-last
   for i in range(len(s) - 1):
   ```

4. **Not handling all subtractive cases**:

   ```python
   # WRONG: Only checking IV, not IX, XL, XC, CD, CM
   if s[i] == "I" and s[i+1] == "V":
       total -= 1

   # CORRECT: Check all subtractive pairs or use value comparison
   if values[s[i]] < values[s[i + 1]]:
       total -= values[s[i]]
   ```

5. **Using incorrect dictionary values**:

   ```python
   # WRONG: Incorrect symbol mappings
   values = {"I": 1, "V": 4, "X": 10}  # V should be 5

   # CORRECT: Use correct values
   values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
   ```

## Optimization Notes

The right-to-left approach is **optimal for this problem**:

- **Time**: O(n) - must read every character
- **Space**: O(1) - fixed dictionary, no scaling
- **Elegant**: Natural handling of subtractive cases

**Interview tips**:

- Start with left-to-right (more intuitive)
- Explain the subtractive rule carefully
- Mention right-to-left as optimization
- Be prepared to code either approach

**Performance notes**:

- All O(n) approaches have similar real-world performance
- Dictionary lookups are very fast
- String operations are optimized
- No significant difference for valid input strings (max ~15 chars)

**When to use each**:

- Left-to-right: First instinct, easier to explain
- Right-to-left: Shows algorithmic insight
- Subtractive pairs: Most explicit, clearest intent
- String replacement: Educational only, don't use in production

## Roman Numeral Reference

| Number | Roman | Number | Roman |
| ------ | ----- | ------ | ----- |
| 1      | I     | 6      | VI    |
| 2      | II    | 7      | VII   |
| 3      | III   | 8      | VIII  |
| 4      | IV    | 9      | IX    |
| 5      | V     | 10     | X     |

| Number | Roman | Number | Roman |
| ------ | ----- | ------ | ----- |
| 40     | XL    | 400    | CD    |
| 50     | L     | 500    | D     |
| 90     | XC    | 900    | CM    |
| 100    | C     | 1000   | M     |

## Visual Example

```
MCMXCIV = 1994

Breakdown:
  M = 1000
  CM = 900 (C before M is subtractive)
  XC = 90 (X before C is subtractive)
  IV = 4 (I before V is subtractive)

Total: 1000 + 900 + 90 + 4 = 1994

Right-to-left processing:
  V (5): max=5, total=5
  I (1): 1<5, subtract, total=4
  C (100): max=100, total=104
  X (10): 10<100, subtract, total=94
  M (1000): max=1000, total=1094
  C (100): 100<1000, subtract, total=994
  M (1000): max=1000, total=1994
```

## Test Cases

```python
# Single symbols
romanToInt("I")                    # 1
romanToInt("V")                    # 5
romanToInt("X")                    # 10
romanToInt("M")                    # 1000

# Additive cases
romanToInt("III")                  # 3
romanToInt("XX")                   # 20
romanToInt("CCC")                  # 300

# Subtractive cases
romanToInt("IV")                   # 4
romanToInt("IX")                   # 9
romanToInt("XL")                   # 40
romanToInt("XC")                   # 90
romanToInt("CD")                   # 400
romanToInt("CM")                   # 900

# Complex numbers
romanToInt("LVIII")                # 58
romanToInt("MCMXCIV")              # 1994
romanToInt("XLII")                 # 42
romanToInt("XCIX")                 # 99
romanToInt("CDXLIV")               # 444
romanToInt("MMXXI")                # 2021
romanToInt("DCCCXC")               # 890

# Maximum value
romanToInt("MMMCMXCIX")            # 3999
```

## Thought Process

**Problem analysis**:

- Convert Roman numeral string to integer
- Must understand Roman numeral rules
- Seven basic symbols with fixed values
- Six special subtractive cases

**Key observations**:

1. Most of the time, add the symbol value
2. Subtractive only happens in 6 specific cases
3. Pattern: smaller value before larger value
4. Can recognize this by comparing adjacent characters

**Approach considerations**:

**Left-to-right with look-ahead**:

- Compare current character with next
- If smaller, it's subtractive (subtract it)
- Otherwise, add it
- Handle last character separately
- Most intuitive first approach

**Right-to-left with max tracking**:

- Go backward through the string
- Track maximum value seen so far
- If current < maximum, subtract (it's subtractive)
- Otherwise, add and update maximum
- Elegant because every character treated the same

**Why right-to-left works**:

```
When going right-to-left, smaller values before larger ones
naturally become subtractive because we've already seen
larger values.

Example: MCMXCIV
  Reading right-to-left: V I C X M C M
  When we read I, we've already seen V (larger)
  So I must be subtractive!
```

**Optimal solution**:

- Time: O(n) - must read every character
- Space: O(1) - dictionary is constant size
- Both approaches achieve optimality

**Interview strategy**:

1. Explain the subtractive rule clearly
2. Code left-to-right approach (more obvious)
3. Discuss complexity (O(n) time, O(1) space)
4. Mention right-to-left as alternative (show depth)
5. Walk through an example like MCMXCIV

This problem tests:

- String parsing and character iteration
- Understanding of domain knowledge (Roman numerals)
- Comparison logic and conditional handling
- Attention to algorithmic details
- Ability to optimize with clever insights

## Related Problems

- [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)
- [1680. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)
- [2006. Count Number of Pairs With Absolute Difference and Divisible by K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-and-divisible-by-k/)
