from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True)

        res = 0
        for numBox, numUnits in boxTypes:
            if truckSize == 0:
                break

            box = min(numBox, truckSize)
            res += (box * numUnits)
            truckSize -= box
        return res

def test_maximum_units():
    s = Solution()

    # Test Case 1
    boxTypes1 = [[1,3],[2,2],[3,1]]
    truckSize1 = 4
    print(s.maximumUnits(boxTypes1, truckSize1)) # Expected Output: 8

    # Test Case 2
    boxTypes2 = [[5,10],[2,5],[4,7],[3,9]]
    truckSize2 = 10
    print(s.maximumUnits(boxTypes2, truckSize2)) # Expected Output: 91

    # Test Case 3
    boxTypes3 = [[1,3],[2,2],[3,1]]
    truckSize3 = 2
    print(s.maximumUnits(boxTypes3, truckSize3)) # Expected Output: 5

    # Test Case 4
    boxTypes4 = [[5,10],[2,5],[4,7],[3,9]]
    truckSize4 = 15
    print(s.maximumUnits(boxTypes4, truckSize4)) # Expected Output: 115

    # Test Case 5
    boxTypes5 = [[1,3],[2,2],[3,1]]
    truckSize5 = 10
    print(s.maximumUnits(boxTypes5, truckSize5)) # Expected Output: 10

test_maximum_units()