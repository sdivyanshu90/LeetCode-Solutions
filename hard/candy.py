from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        
        return sum(candies)

def test_candy():
    solution = Solution()
    # Test Case 1
    print(solution.candy([1, 0, 2])) # Expected output: 5

    # Test Case 2
    print(solution.candy([1, 2, 2])) # Expected output: 4

    # Test Case 3
    print(solution.candy([1, 3, 4, 5, 2])) # Expected output: 11

    # Test Case 4
    print(solution.candy([1, 2, 3, 4, 5])) # Expected output: 15

    # Test Case 5
    print(solution.candy([5, 4, 3, 2, 1])) # Expected output: 15

    # Test Case 6
    print(solution.candy([1, 2, 3, 2, 1])) # Expected output: 9

    # Test Case 7
    print(solution.candy([1])) # Expected output: 1

    # Test Case 8
    print(solution.candy([1, 2])) # Expected output: 3

    # Test Case 9
    print(solution.candy([2, 1])) # Expected output: 3

    # Test Case 10
    print(solution.candy([1, 0, 2, 1])) # Expected output: 6

test_candy()