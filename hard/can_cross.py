from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        visited_set = set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in [jump-1, jump, jump+1]:
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in visited_set:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            visited_set.add((stone, jump))
        return False

def test_can_cross():
    s = Solution()

    # Test case 1
    print(s.canCross([0,1,3,5,6,8,12,17]))  # Expected output: True

    # Test case 2
    print(s.canCross([0,1,2,3,4,8,9,11]))   # Expected output: False

    # Test case 3
    print(s.canCross([0,1]))                  # Expected output: True

    # Test case 4
    print(s.canCross([0,2]))                  # Expected output: False

    # Test case 5
    print(s.canCross([0,1,3,6,10,15,21,28])) # Expected output: True

    # Test case 6
    print(s.canCross([0,1,2,3,4,5,6,7,8,9,10])) # Expected output: True

    # Test case 7
    print(s.canCross([0,1,3,4,5,7,9,10,12])) # Expected output: True

    # Test case 8
    print(s.canCross([0]))                     # Expected output: False

    # Test case 9
    print(s.canCross([0,1,3,5,7,9,11,13]))    # Expected output: True

    # Test case 10
    print(s.canCross([0,1,2,4,7,11]))         # Expected output: True

test_can_cross()