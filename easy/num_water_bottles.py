class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange == 1:
            return float('inf')
        
        return numBottles + (numBottles - 1) // (numExchange - 1)

def test_num_water_bottles():
    solution = Solution()

    # Test case 1
    numBottles1 = 9
    numExchange1 = 3
    print(solution.numWaterBottles(numBottles1, numExchange1))  # Expected output: 13

    # Test case 2
    numBottles2 = 15
    numExchange2 = 4
    print(solution.numWaterBottles(numBottles2, numExchange2))  # Expected output: 19

    # Test case 3
    numBottles3 = 5
    numExchange3 = 5
    print(solution.numWaterBottles(numBottles3, numExchange3))  # Expected output: 6

    # Test case 4
    numBottles4 = 2
    numExchange4 = 3
    print(solution.numWaterBottles(numBottles4, numExchange4))  # Expected output: 2

    # Test case 5
    numBottles5 = 10
    numExchange5 = 2
    print(solution.numWaterBottles(numBottles5, numExchange5))  # Expected output: 19

test_num_water_bottles()