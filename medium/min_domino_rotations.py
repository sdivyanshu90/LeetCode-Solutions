from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(tops, bottoms):
            curr = 0
            for i in range(n):
                if tops[i] != d:
                    if bottoms[i] != d:
                        return n
                    curr += 1
            return curr
        n = len(tops)
        ans = n
        for d in (tops[0], bottoms[0]):
            ans = min(ans, check(tops, bottoms), check(bottoms, tops))
        return ans if ans < n else -1

def test_min_domino_rotations():
    solution = Solution()

    # Test case 1
    tops1 = [2,1,2,4,2,2]
    bottoms1 = [5,2,6,2,3,2]
    print(solution.minDominoRotations(tops1, bottoms1))  # Expected output: 2

    # Test case 2
    tops2 = [3,5,1,2,3]
    bottoms2 = [3,6,3,3,4]
    print(solution.minDominoRotations(tops2, bottoms2))  # Expected output: -1

    # Test case 3
    tops3 = [1,2,1,1,1,2,2,2]
    bottoms3 = [2,1,2,2,2,2,2,2]
    print(solution.minDominoRotations(tops3, bottoms3))  # Expected output: 1

    # Test case 4
    tops4 = [1,1,1,1]
    bottoms4 = [1,1,1,1]
    print(solution.minDominoRotations(tops4, bottoms4))  # Expected output: 0

    # Test case 5
    tops5 = [2,2,2,2]
    bottoms5 = [1,1,1,1]
    print(solution.minDominoRotations(tops5, bottoms5))  # Expected output: 0

test_min_domino_rotations()