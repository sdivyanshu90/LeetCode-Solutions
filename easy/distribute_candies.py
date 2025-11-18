from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)

def test_distribute_candies():
    s = Solution()

    # Test case 1
    candyType1 = [1,1,2,2,3,3]
    print(s.distributeCandies(candyType1)) # Expected output: 3

    # Test case 2
    candyType2 = [1,1,2,3]
    print(s.distributeCandies(candyType2)) # Expected output: 2

    # Test case 3
    candyType3 = [6,6,6,6]
    print(s.distributeCandies(candyType3)) # Expected output: 1

    # Test case 4
    candyType4 = [1,2,3,4,5,6]
    print(s.distributeCandies(candyType4)) # Expected output: 3

    # Test case 5
    candyType5 = [1]
    print(s.distributeCandies(candyType5)) # Expected output: 0
    
test_distribute_candies()