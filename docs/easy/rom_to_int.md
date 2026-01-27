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

**LeetCode Problem**: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

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
