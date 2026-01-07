# Can Construct

## Problem Summary

- Given two strings ransomNote and magazine, determine if ransomNote can be constructed from the letters in magazine.
- Each letter in magazine can be used at most once.

Approach (counting frequency)

- Use a fixed-size frequency array (26 for lowercase English letters) or a hashmap.
- Count occurrences of each character in magazine.
- Iterate ransomNote and for each character decrement the corresponding count.
  - If at any point the count becomes negative, return False (not enough letters).
- If all characters processed successfully, return True.

Why this works

- The problem asks only whether magazine supplies enough occurrences of each character required by ransomNote.
- Counting is optimal because it tallies supply once and performs constant-time checks for demand.

Time and space complexity

- Time: O(m + n), where m = len(magazine) and n = len(ransomNote). We scan each string once.
- Space: O(1) using a 26-length array (or O(k) if using a hashmap with k distinct characters).

Implementation notes and micro-optimizations

- Use list of length 26 and ord(char) - ord('a') to index counts for best constant factor.
- Early exit as soon as a required character is missing.
- If inputs may include non-lowercase or Unicode, use a defaultdict/counter instead of fixed 26-array.

Edge cases

- ransomNote is empty -> return True.
- magazine is empty but ransomNote is not -> return False.
- ransomNote longer than magazine -> return False quickly (optional check).

Example testcases

- ransomNote = "aa", magazine = "ab" -> False
- ransomNote = "aa", magazine = "aab" -> True
- ransomNote = "", magazine = "" -> True
- ransomNote = "abc", magazine = "ab" -> False

Thought process

- The goal is to check availability counts, not order — counting frequencies matches problem requirements exactly and yields linear time with constant extra space.

## Approach: Hash Map (Implemented)

### Strategy

The solution uses hash map to solve the problem efficiently.

### How It Works

Problem summary

- Given two strings ransomNote and magazine, determine if ransomNote can be constructed from the letters in magazine.
- Each letter in magazine can be used at most once.

Approach (counting frequency)

- Use a fixed-size frequency array (26 for lowercase English letters) or a hashmap.
- Count occurrences of each character in magazine.
- Iterate ransomNote and for each character decrement the corresponding count.
  - If at any point the count becomes negative, return False (not enough letters).
- If all characters processed successfully, return True.

Why this works

- The problem asks only whether magazine supplies enough occurrences of each character required by ransomNote.
- Counting is optimal because it tallies supply once and performs constant-time checks for demand.

Time and space complexity

- Time: O(m + n), where m = len(magazine) and n = len(ransomNote). We scan each string once.
- Space: O(1) using a 26-length array (or O(k) if using a hashmap with k distinct characters).

Implementation notes and micro-optimizations

- Use list of length 26 and ord(char) - ord('a') to index counts for best constant factor.
- Early exit as soon as a required character is missing.
- If inputs may include non-lowercase or Unicode, use a defaultdict/counter instead of fixed 26-array.

Edge cases

- ransomNote is empty -> return True.
- magazine is empty but ransomNote is not -> return False.
- ransomNote longer than magazine -> return False quickly (optional check).

Example testcases

- ransomNote = "aa", magazine = "ab" -> False
- ransomNote = "aa", magazine = "aab" -> True
- ransomNote = "", magazine = "" -> True
- ransomNote = "abc", magazine = "ab" -> False

Thought process

- The goal is to check availability counts, not order — counting frequencies matches problem requirements exactly and yields linear time with constant extra space.

### Why Hash Map Works

- The problem asks only whether magazine supplies enough occurrences of each character required by ransomNote.
- Counting is optimal because it tallies supply once and performs constant-time checks for demand.

Time and space complexity

- Time: O(m + n), where m = len(magazine) and n = len(ransomNote). We scan each string once.
- Space: O(1) using a 26-length array (or O(k) if using a hashmap with k distinct characters).

Implementation notes and micro-optimizations

- Use list of length 26 and ord(char) - ord('a') to index counts for best constant factor.
- Early exit as soon as a required character is missing.
- If inputs may include non-lowercase or Unicode, use a defaultdict/counter instead of fixed 26-array.

Edge cases

- ransomNote is empty -> return True.
- magazine is empty but ransomNote is not -> return False.
- ransomNote longer than magazine -> return False quickly (optional check).

Example testcases

- ransomNote = "aa", magazine = "ab" -> False
- ransomNote = "aa", magazine = "aab" -> True
- ransomNote = "", magazine = "" -> True
- ransomNote = "abc", magazine = "ab" -> False

Thought process

- The goal is to check availability counts, not order — counting frequencies matches problem requirements exactly and yields linear time with constant extra space.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(m + n), where m = len(magazine) and n = len(ransomNote). We scan each string once. - Space: O(1) using a 26-length array (or O(k) if using a hashmap with k distinct characters). Implementation notes and micro-optimizations - Use list of length 26 and ord(char) - ord('a') to index counts for best constant factor. - Early exit as soon as a required character is missing. - If inputs may include non-lowercase or Unicode, use a defaultdict/counter instead of fixed 26-array. Edge cases - ransomNote is empty -> return True. - magazine is empty but ransomNote is not -> return False. - ransomNote longer than magazine -> return False quickly (optional check). Example testcases - ransomNote = "aa", magazine = "ab" -> False - ransomNote = "aa", magazine = "aab" -> True - ransomNote = "", magazine = "" -> True - ransomNote = "abc", magazine = "ab" -> False Thought process - The goal is to check availability counts, not order — counting frequencies matches problem requirements exactly and yields linear time with constant extra space.

### Advantages

- Efficient hash map solution
- Clear and maintainable code

### Disadvantages

- May require additional space
