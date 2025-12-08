import math
from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for k, freq in count.items():
            group_size = k + 1
            groups = math.ceil(freq / group_size)
            res += groups * group_size
        return res

def test_num_rabbits():
    solution = Solution()
    
    # Test case 1
    answers = [1, 1, 2]
    print(solution.numRabbits(answers)) # Expected: 5
    
    # Test case 2
    answers = [10, 10, 10]
    print(solution.numRabbits(answers)) # Expected: 11
    
    # Test case 3
    answers = []
    print(solution.numRabbits(answers)) # Expected: 0
    
    # Test case 4
    answers = [0, 0, 1, 1, 1]
    print(solution.numRabbits(answers)) # Expected: 6

    # Test case 5
    answers = [2, 2, 2, 2]
    print(solution.numRabbits(answers)) # Expected: 6

    # Test case 6
    answers = [3, 3, 3, 3, 3, 3, 3]
    print(solution.numRabbits(answers)) # Expected: 8

    # Test case 7
    answers = [4, 4, 4, 4, 4]
    print(solution.numRabbits(answers)) # Expected: 10

    # Test case 8
    answers = [1, 0, 1, 0]
    print(solution.numRabbits(answers)) # Expected: 6

    # Test case 9
    answers = [5]
    print(solution.numRabbits(answers)) # Expected: 6

    # Test case 10
    answers = [0]
    print(solution.numRabbits(answers)) # Expected: 1

test_num_rabbits()