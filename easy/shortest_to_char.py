from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        temp = []
        for i in range(len(s)):
            if s[i] == c:
                temp.append(i)
        
        res = []
        for i in range(len(s)):
            if s[i] != c:
                res.append(min([abs(i - j) for j in temp]))
            else:
                res.append(0)
        return res

def test_shortest_to_char():
    solution = Solution()

    # Test Case 1
    s1 = "loveleetcode"
    c1 = "e"
    print(solution.shortestToChar(s1, c1)) # Expected: [3,2,1,0,1,0,0,1,2,2,1,0]

    # Test Case 2
    s2 = "aaab"
    c2 = "b"
    print(solution.shortestToChar(s2, c2)) # Expected: [3,2,1,0]

    # Test Case 3
    s3 = "abcde"
    c3 = "a"
    print(solution.shortestToChar(s3, c3)) # Expected: [0,1,2,3,4]

    # Test Case 4
    s4 = "zzzzzz"
    c4 = "z"
    print(solution.shortestToChar(s4, c4)) # Expected: [0,0,0,0,0,0]

    # Test Case 5
    s5 = "aabbccdd"
    c5 = "c"
    print(solution.shortestToChar(s5, c5)) # Expected: [4,3,2,1,0,0,1,2]

test_shortest_to_char()