class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        lvl = 0
        res = 0
        for rung in rungs:
            res += max(0, (rung - lvl - 1) // dist)
            lvl = rung
        return res

def test_add_rungs():
    solution = Solution()

    # Test case 1
    rungs1 = [1, 3, 5, 10]
    dist1 = 2
    print(solution.addRungs(rungs1, dist1))  # Expected output: 2

    # Test case 2
    rungs2 = [3, 6, 8, 10]
    dist2 = 3
    print(solution.addRungs(rungs2, dist2))  # Expected output: 0

    # Test case 3
    rungs3 = [3, 4, 6, 7]
    dist3 = 2
    print(solution.addRungs(rungs3, dist3))  # Expected output: 1

    # Test case 4
    rungs4 = [5]
    dist4 = 10
    print(solution.addRungs(rungs4, dist4))  # Expected output: 0

    # Test case 5
    rungs5 = [1, 1000000000]
    dist5 = 1
    print(solution.addRungs(rungs5, dist5))  # Expected output: 999999998

test_add_rungs()