from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, comb):
            if len(comb) == k:
                result.append(list(comb))
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        result = []
        backtrack(1, [])
        return result

def test_combine():
    solution = Solution()

    # Test case 1
    n1, k1 = 4, 2
    print(solution.combine(n1, k1))  # Expected output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    # Test case 2
    n2, k2 = 1, 1
    print(solution.combine(n2, k2))  # Expected output: [[1]]

    # Test case 3
    n3, k3 = 5, 3
    print(solution.combine(n3, k3))  # Expected output: [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]

    # Test case 4
    n4, k4 = 3, 1
    print(solution.combine(n4, k4))  # Expected output: [[1],[2],[3]]

    # Test case 5
    n5, k5 = 6, 4
    print(solution.combine(n5, k5))  # Expected output: Combinations of 6 choose 4

    # Test case 6
    n6, k6 = 2, 2
    print(solution.combine(n6, k6))  # Expected output: [[1,2]]

    # Test case 7
    n7, k7 = 3, 2
    print(solution.combine(n7, k7))  # Expected output: [[1,2],[1,3],[2,3]]

    # Test case 8
    n8, k8 = 4, 3
    print(solution.combine(n8, k8))  # Expected output: [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]

    # Test case 9
    n9, k9 = 5, 1
    print(solution.combine(n9, k9))  # Expected output: [[1],[2],[3],[4],[5]]

    # Test case 10
    n10, k10 = 7, 5
    print(solution.combine(n10, k10))  # Expected output: Combinations of 7 choose 5

test_combine()