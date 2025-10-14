# Approach 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

# Approach 2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         count1 = [0] * 256
#         count2 = [0] * 256

#         for i in s:
#             count1[ord(i)] += 1
#         for j in t:
#             count2[ord(j)] += 1

#         if len(s) != len(t):
#             return False
        
#         for i in range(256):
#             if count1[i] != count2[i]:
#                 return False
#         return True

# Approach 3
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         for i in "abcdefghijklmnopqrstuvwxyz":
#             if s.count(i) != t.count(i):
#                 return False

#         return set(s) == set(t)

# Approach 4
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         stack = list(s)

#         for i in t:
#             if i in stack:
#                 stack.remove(i)

#         return len(stack) == 0

# Approach 5
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         else:
#             return False

def test_is_anagram():
    s = Solution()

    # Test Case 1: Basic valid anagram
    str_s, str_t = "anagram", "nagaram"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: True

    # Test Case 2: Basic invalid anagram
    str_s, str_t = "rat", "car"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: False

    # Test Case 3: Different lengths
    str_s, str_t = "hello", "hell"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: False

    # Test Case 4: Case sensitivity
    str_s, str_t = "Listen", "silent"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: False (due to 'L' vs 'l')

    # Test Case 5: Empty strings (edge case)
    str_s, str_t = "", ""
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: True

    # Test Case 6: Strings with duplicate characters
    str_s, str_t = "aabbc", "babac"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: True

    # Test Case 7: Strings with numbers and symbols
    str_s, str_t = "123!", "!321"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: True

    # Test Case 8: Subtle false case (same characters, different counts)
    str_s, str_t = "aacc", "ccca"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: False

    # Test Case 9: Longer strings
    str_s, str_t = "astronomer", "moonstarer"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: True

    # Test Case 10: Unicode characters
    str_s, str_t = "안녕하세요", "안녕요하세"
    print(f"\nInput: s = '{str_s}', t = '{str_t}'")
    print(f"Output: {s.isAnagram(str_s, str_t)}") # Expected: True

test_is_anagram()