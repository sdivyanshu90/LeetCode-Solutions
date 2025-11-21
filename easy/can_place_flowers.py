from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):            
            if (i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0 and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0: 
                return True
        return False

def test_can_place_flowers():
    s = Solution()

    # Test case 1
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(s.canPlaceFlowers(flowerbed, n))  # Expected output: True

    # Test case 2
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(s.canPlaceFlowers(flowerbed, n))  # Expected output: False

    # Test case 3
    flowerbed = [0, 0, 1, 0, 0]
    n = 1
    print(s.canPlaceFlowers(flowerbed, n))  # Expected output: True

    # Test case 4
    flowerbed = [0, 0, 0, 0, 0]
    n = 3
    print(s.canPlaceFlowers(flowerbed, n))  # Expected output: True

    # Test case 5
    flowerbed = [1, 1, 1, 1, 1]
    n = 1
    print(s.canPlaceFlowers(flowerbed, n))  # Expected output: False

test_can_place_flowers()