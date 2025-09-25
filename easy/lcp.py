from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

def test_longest_common_prefix():
    solution = Solution()

    # Test case 1
    strs = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "fl"

    # Test case 2
    strs = ["dog","racecar","car"]
    print(solution.longestCommonPrefix(strs))  # Expected output: ""

    # Test case 3
    strs = ["interspecies","interstellar","interstate"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "inters"

    # Test case 4
    strs = ["throne","dungeon"]
    print(solution.longestCommonPrefix(strs))  # Expected output: ""

    # Test case 5
    strs = ["throne","throne"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "throne"

    # Test case 6
    strs = ["a"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "a"

    # Test case 7
    strs = ["", "b"]
    print(solution.longestCommonPrefix(strs))  # Expected output: ""

    # Test case 8
    strs = ["c", "c"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "c"

    # Test case 9
    strs = ["ab", "a"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "a"

    # Test case 10
    strs = ["a", "a", "a"]
    print(solution.longestCommonPrefix(strs))  # Expected output: "a"

test_longest_common_prefix()