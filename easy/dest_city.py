from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        right = set()
        left = set()
        for i in paths:
            right.add(i[0])
            left.add(i[1])
        return list(left - right)[0]

def test_dest_city():
    solution = Solution()

    # Test case 1
    paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(solution.destCity(paths1))  # Expected output: "Sao Paulo"

    # Test case 2
    paths2 = [["B","C"],["D","B"],["C","A"]]
    print(solution.destCity(paths2))  # Expected output: "A"

    # Test case 3
    paths3 = [["A","Z"]]
    print(solution.destCity(paths3))  # Expected output: "Z"

    # Test case 4
    paths4 = [["X","Y"],["Y","Z"],["Z","W"]]
    print(solution.destCity(paths4))  # Expected output: "W"

    # Test case 5
    paths5 = [["P","Q"],["Q","R"],["R","S"],["S","T"]]
    print(solution.destCity(paths5))  # Expected output: "T"

test_dest_city()