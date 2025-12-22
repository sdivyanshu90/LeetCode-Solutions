# Valid Palindrome — Explanation, Approach, Complexity

**Problem Summary**

- Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
- A palindrome reads the same forward and backward after processing.
- Example: "A man, a plan, a canal: Panama" → True (becomes "amanaplanacanalpanama")

**Approach 1 (Active): Filter + reverse comparison**

- Filter the string to keep only alphanumeric characters using `filter(str.isalnum, s)`.
- Convert to lowercase with `.lower()`.
- Compare the processed string with its reverse using slicing `[::-1]`.
- Return `True` if they match, `False` otherwise.

Implementation:

```python
def isPalindrome(self, s: str) -> bool:
    new_s = "".join(filter(str.isalnum, s)).lower()
    if new_s == new_s[::-1]:
        return True
    return False
```

**Why It Works**

- `filter(str.isalnum, s)` removes all non-alphanumeric characters (spaces, punctuation).
- `.lower()` ensures case-insensitive comparison.
- String slicing `[::-1]` creates a reversed copy.
- Direct equality check verifies palindrome property.

**Complexity (Approach 1)**

- Time: O(n) where n = len(s)
  - Filter: O(n)
  - Lowercase conversion: O(n)
  - Reverse and comparison: O(n)
- Space: O(n) for the filtered string and its reverse

**Alternative Approach 2: Two pointers (in-place, commented in file)**

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

- Time: O(n)
- Space: O(n) for the cleaned string (though comparison is in-place)
- Uses regex to remove non-alphanumeric characters
- Two pointers converge from both ends

**True O(1) Space Approach (without preprocessing string)**

```python
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

- Time: O(n), Space: O(1)
- Skips non-alphanumeric characters on-the-fly without creating new string

**Thought Process / Design Choices**

- Approach 1 is most readable: filter → lowercase → compare with reverse.
- Approach 2 preprocesses the string then uses two pointers.
- True O(1) space approach skips invalid characters during comparison (more complex but optimal space).
- For most practical cases, Approach 1 or 2 are preferred for clarity.

**Edge Cases**

- Empty string → return True (vacuously a palindrome)
- Single character → return True
- Only non-alphanumeric characters (e.g., ".,!") → becomes empty string, return True
- All lowercase/uppercase → handled by `.lower()`
- Mixed alphanumeric (e.g., "0P") → return False

**Example Testcases (from repository)**

- "A man, a plan, a canal: Panama" → True
- "race a car" → False (becomes "raceacar")
- " " → True (empty after filtering)
- "A Toyota's a Toyota" → True (becomes "atoyotasatoyota")
- "No 'x' in Nixon" → True (becomes "noxinnixon")

**Common Pitfalls**

- Not handling case insensitivity → must convert to lowercase.
- Comparing original string with non-alphanumeric characters → must filter first.
- Not handling empty strings or strings with only special characters.
- Creating multiple intermediate strings → can be optimized with two pointers on original string.

**Optimization Notes**

- Approach 1: Clean and Pythonic, easy to understand.
- Approach 2: Similar to Approach 1 but uses regex for filtering.
- For competitive programming or interviews asking for O(1) space, use the true two-pointer approach.
- For production code prioritizing readability, Approach 1 is recommended.

**Key Insight**

- The problem requires two transformations: filtering (remove non-alphanumeric) and normalization (case-insensitive).
- After these transformations, standard palindrome check applies.
