from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        temp = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                temp.add(i)

        b = list(temp)
        a = [i for i in range(left, right + 1)]
        
        for i in range(len(b) - len(a) + 1):
            for j in range(len(a)):
                if b[i + j] != a[j]:
                    break
            else:
                return True
        return False

def test_is_covered():
    solution = Solution()

    # Test case 1
    ranges = [[1, 2], [3, 4], [5, 6]]
    left = 2
    right = 5
    print(solution.isCovered(ranges, left, right))  # Expected output: True

    # Test case 2
    ranges = [[1, 10], [11, 20]]
    left = 1
    right = 20
    print(solution.isCovered(ranges, left, right))  # Expected output: True

    # Test case 3
    ranges = [[1, 5], [10, 15]]
    left = 1
    right = 10
    print(solution.isCovered(ranges, left, right))  # Expected output: False

    # Test case 4
    ranges = [[1, 3], [5, 7], [9, 11]]
    left = 2
    right = 10
    print(solution.isCovered(ranges, left, right))  # Expected output: False

    # Test case 5
    ranges = [[1, 5], [6, 10]]
    left = 1
    right = 10
    print(solution.isCovered(ranges, left, right))  # Expected output: True

test_is_covered()