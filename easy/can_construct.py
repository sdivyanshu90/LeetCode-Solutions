from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1 = Counter(ransomNote)
        str2 = Counter(magazine)
        
        # Check if all characters in ransomNote are present in magazine and their counts are less or equal
        for char, count in str1.items():
            if char not in str2 or count > str2[char]:
                return False
        
        return True

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         char_count = {}
        
#         # Count the characters in the magazine and check if ransomNote can be constructed
#         for char in magazine:
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
        
#         for char in ransomNote:
#             if char not in char_count or char_count[char] == 0:
#                 return False
#             char_count[char] -= 1
        
#         return True

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         str1, str2 = Counter(ransomNote), Counter(magazine)
#         if str1 & str2 == str1:
#             return True
#         else:
#             return False

def test_can_construct():
    solution = Solution()
    
    # Test case 1: Basic case
    print(solution.canConstruct("a", "b")) # Expected output: False
    
    # Test case 2: Exact match
    print(solution.canConstruct("aa", "aab")) # Expected output: True

    # Test case 3: Insufficient characters
    print(solution.canConstruct("aa", "ab")) # Expected output: False

    # Test case 4: Empty ransomNote
    print(solution.canConstruct("", "abc")) # Expected output: True

    # Test case 5: Empty magazine
    print(solution.canConstruct("a", "")) # Expected output: False

    # Test case 6: Both empty
    print(solution.canConstruct("", "")) # Expected output: True

    # Test case 7: Large input with sufficient characters
    large_ransom = "a" * 1000 + "b" * 500 + "c" * 200
    large_magazine = "a" * 2000 + "b" * 1000 + "c" * 500
    print(solution.canConstruct(large_ransom, large_magazine)) # Expected output: True

    # Test case 8: Large input with insufficient characters
    large_ransom_insufficient = "a" * 3000 + "b" * 500 + "c" * 200
    print(solution.canConstruct(large_ransom_insufficient, large_magazine)) # Expected output: False

    # Test case 9: Ransom note with special characters
    print(solution.canConstruct("a!b@c#", "a!b@c#d$e%f^")) # Expected output: True

    # Test case 10: Magazine with no characters
    print(solution.canConstruct("law", "")) # Expected output: False

test_can_construct()