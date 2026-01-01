from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            ret += num[val]
            num[val] += 1
        return ret

def test_num_equiv_domino_pairs():
    solution = Solution()

    # Test case 1
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    print(solution.numEquivDominoPairs(dominoes))  # Expected output: 1

    # Test case 2
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    print(solution.numEquivDominoPairs(dominoes))  # Expected output: 3

    # Test case 3
    dominoes = [[1,1],[1,1],[1,1]]
    print(solution.numEquivDominoPairs(dominoes))  # Expected output: 3

    # Test case 4
    dominoes = [[2,3],[3,2],[2,3],[3,2]]
    print(solution.numEquivDominoPairs(dominoes))  # Expected output: 6

    # Test case 5
    dominoes = [[0,0],[0,0],[0,0],[0,0]]
    print(solution.numEquivDominoPairs(dominoes))  # Expected output: 6

test_num_equiv_domino_pairs()