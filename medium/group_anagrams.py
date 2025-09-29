from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

def test_group_anagrams():
    s = Solution()
    
    # Test case 1: Regular case with multiple anagram groups
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    # Test case 2: Single string
    print(s.groupAnagrams(["abc"]))

    # Test case 3: No anagrams
    print(s.groupAnagrams(["abc", "def", "ghi"]))

    # Test case 4: All strings are anagrams of each other
    print(s.groupAnagrams(["abc", "bca", "cab", "cba", "bac", "acb"]))

    # Test case 5: Empty list
    print(s.groupAnagrams([]))

    # Test case 6: List with empty strings
    print(s.groupAnagrams(["", "", ""]))

    # Test case 7: Mixed lengths and characters
    print(s.groupAnagrams(["a", "b", "ab", "ba", "abc", "cba", "cab"]))

    # Test case 8: Case sensitivity
    print(s.groupAnagrams(["aA", "Aa", "aa", "AA"]))

    # Test case 9: Large input with repeated patterns
    print(s.groupAnagrams(["abcd"] * 10 + ["dcba"] * 10 + ["bcda"] * 10))

    # Test case 10: Strings with special characters
    print(s.groupAnagrams(["@bc!", "!cb@", "c!b@", "@!bc"]))

test_group_anagrams()