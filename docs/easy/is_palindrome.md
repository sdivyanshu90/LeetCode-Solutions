# Valid Palindrome

## Problem Summary

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

A palindrome reads the same forward and backward after processing.

**Example**: `"A man, a plan, a canal: Panama"` → `True` (becomes `"amanaplanacanalpanama"`)

## Approach: Filter and Reverse (Implemented)

### Strategy

The solution uses string filtering and reverse comparison:

1. Filter the string to keep only alphanumeric characters using `filter(str.isalnum, s)`
2. Convert to lowercase with `.lower()`
3. Compare the processed string with its reverse using slicing `[::-1]`
4. Return `True` if they match, `False` otherwise

```python
def isPalindrome(self, s: str) -> bool:
    new_s = "".join(filter(str.isalnum, s)).lower()
    if new_s == new_s[::-1]:
        return True
    return False
```

### How It Works

**Example 1**: `s = "A man, a plan, a canal: Panama"`

```
Original: "A man, a plan, a canal: Panama"

Step 1 - Filter non-alphanumeric:
  filter(str.isalnum, s) → "AmanaplanacanalPanama"

Step 2 - Convert to lowercase:
  .lower() → "amanaplanacanalpanama"

Step 3 - Reverse and compare:
  new_s = "amanaplanacanalpanama"
  new_s[::-1] = "amanaplanacanalpanama"

  "amanaplanacanalpanama" == "amanaplanacanalpanama" ✓
  Return True
```

**Example 2**: `s = "race a car"`

```
Original: "race a car"

Filter: "raceacar"
Lowercase: "raceacar"
Reverse: "racaecar"

"raceacar" != "racaecar" ✗
Return False
```

**Example 3**: `s = " "`

```
Original: " "

Filter: "" (empty after removing spaces)
Lowercase: ""
Reverse: ""

"" == "" ✓
Return True (empty string is palindrome)
```

### Why Filter and Reverse Works

- **Filtering non-alphanumeric**: `filter(str.isalnum, s)` removes all spaces, punctuation, and special characters
- **Case normalization**: `.lower()` ensures case-insensitive comparison
- **Reverse comparison**: String slicing `[::-1]` creates a reversed copy for direct equality check
- **Clean approach**: Each transformation step is explicit and easy to understand

### Complexity Analysis

- **Time Complexity**: O(n) where n = len(s)
  - Filtering: O(n) to scan through all characters
  - Lowercase conversion: O(n)
  - Reverse and comparison: O(n)
  - Total: O(n) + O(n) + O(n) = O(n)
- **Space Complexity**: O(n)
  - Filtered string requires O(n) space
  - Reversed string requires O(n) space
  - Total: O(n)

### Advantages

- **Highly readable**: Clean and Pythonic code
- **Easy to understand**: Each step is explicit
- **Handles all cases**: Works with any input string
- **Concise**: Few lines of code

### Disadvantages

- **Uses O(n) space**: Creates two new strings (filtered and reversed)
- **Not optimal for space**: Could be done with O(1) space using two pointers
- **Multiple passes**: Scans string multiple times

## Alternative Approach 1: Two Pointers with Preprocessing

Use regex for filtering, then two-pointer comparison:

```python
import re

def isPalindrome(self, s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### How It Works

- Use regex to remove all non-alphanumeric characters
- Convert to lowercase
- Two pointers converge from both ends checking equality

### Complexity

- **Time**: O(n) - preprocessing + two-pointer scan
- **Space**: O(n) - for cleaned string

### Advantages

- **Clear logic**: Preprocessing then comparison
- **Early exit**: Returns False as soon as mismatch found

### Disadvantages

- **Still O(n) space**: Creates preprocessed string

## Alternative Approach 2: True O(1) Space (Two Pointers on Original String)

Skip non-alphanumeric characters on-the-fly:

```python
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare lowercase characters
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### How It Works

- Two pointers start at both ends
- Skip invalid characters dynamically without creating new string
- Compare lowercase characters directly
- No extra space for string storage

### Complexity

- **Time**: O(n) - single pass through string
- **Space**: O(1) - only two pointer variables

### Advantages

- **Space optimal**: True O(1) space
- **No preprocessing**: Works on original string
- **Early exit**: Returns as soon as mismatch found

### Disadvantages

- **More complex**: More code with nested while loops
- **Less readable**: Logic is more intricate
