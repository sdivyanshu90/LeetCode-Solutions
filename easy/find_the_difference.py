class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i): 
                return i

def test_find_the_difference():
    solution = Solution()
    
    # Test case 1
    print(solution.findTheDifference("abcd", "abcde")) # Expected output: "e"
    
    # Test case 2
    print(solution.findTheDifference("", "y")) # Expected output: "y"

    # Test case 3: Edge case - single character
    print(solution.findTheDifference("a", "aa")) # Expected output: "a"

    # Test case 4: Repeated characters
    print(solution.findTheDifference("aabbcc", "abcbcad")) # Expected output: "d"
    
    # Test case 5: All characters the same except one
    print(solution.findTheDifference("zzzz", "zzzzz")) # Expected output: "z"

    # Test case 6: Long strings with one different character
    s = "abcdefghij" * 1000
    t = s + "k"
    print(solution.findTheDifference(s, t)) # Expected output: "k"

    # Test case 7: Different character at the beginning
    print(solution.findTheDifference("bcdef", "abcdef")) # Expected output: "a"

    # Test case 8: Different character at the end
    print(solution.findTheDifference("mnopq", "mnopqr")) # Expected output: "r"

    # Test case 9: Mixed characters
    print(solution.findTheDifference("xyzxyz", "xyzxyza")) # Expected output: "a"

    # Test case 10: Unicode characters
    print(solution.findTheDifference("Hol", "Holl")) # Expected output: "l"

test_find_the_difference()