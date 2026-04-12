class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        
        for word in words:
            prefix += word
            
            if prefix == s:
                return True
            
            if len(prefix) > len(s):
                return False
        
        return False

def test_is_prefix_string():
    solution = Solution()

    # Test Case 1
    s1 = "iloveleetcode"
    words1 = ["i", "love", "leetcode", "apples"]
    print(solution.isPrefixString(s1, words1))  # Expected output: True

    # Test Case 2
    s2 = "iloveleetcode"
    words2 = ["apples", "i", "love", "leetcode"]
    print(solution.isPrefixString(s2, words2))  # Expected output: False

    # Test Case 3
    s3 = "abc"
    words3 = ["a", "b", "c"]
    print(solution.isPrefixString(s3, words3))  # Expected output: True

    # Test Case 4
    s4 = "abc"
    words4 = ["ab", "c"]
    print(solution.isPrefixString(s4, words4))  # Expected output: True

    # Test Case 5
    s5 = "abc"
    words5 = ["a", "bc"]
    print(solution.isPrefixString(s5, words5))  # Expected output: True

test_is_prefix_string()