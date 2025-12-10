from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        i = 0

        for j in range(len(s)):
            if j == len(s) - 1 or s[j] != s[j + 1]:
                if j - i + 1 >= 3:
                    res.append([i, j])

                i = j + 1
        return res

def test_largest_group_positions():
    solution = Solution()

    # Test Case 1
    s1 = "abbxxxxzzy"
    print(solution.largeGroupPositions(s1)) # Expected: [[3,6]]

    # Test Case 2
    s2 = "abc"
    print(solution.largeGroupPositions(s2)) # Expected: []

    # Test Case 3
    s3 = "abcdddeeeeaabbbcd"
    print(solution.largeGroupPositions(s3)) # Expected: [[3,5],[6,9],[12,14]]

    # Test Case 4
    s4 = "aaabbbcccddd"
    print(solution.largeGroupPositions(s4)) # Expected: [[0,2],[3,5],[6,8],[9,11]]

    # Test Case 5
    s5 = "aabbccddeeefffggghhh"
    print(solution.largeGroupPositions(s5)) # Expected: [[8, 10], [11, 13], [14, 16], [17, 19]]

test_largest_group_positions()