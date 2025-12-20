from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0] * (n + 1)

        for a,b in trust:
            people[a] -= 1
            people[b] += 1
        
        for i in range(1, n + 1):
            if people[i] == n -1:
                return i
        
        return -1

def test_find_judge():
    solution = Solution()
    
    # Test case 1
    n = 2
    trust = [[1,2]]
    print(solution.findJudge(n, trust))  # Expected output: 2

    # Test case 2
    n = 3
    trust = [[1,3],[2,3]]
    print(solution.findJudge(n, trust))  # Expected output: 3

    # Test case 3
    n = 3
    trust = [[1,3],[2,3],[3,1]]
    print(solution.findJudge(n, trust))  # Expected output: -1

    # Test case 4
    n = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    print(solution.findJudge(n, trust))  # Expected output: 3

    # Test case 5
    n = 1
    trust = []
    print(solution.findJudge(n, trust))  # Expected output: 1

test_find_judge()