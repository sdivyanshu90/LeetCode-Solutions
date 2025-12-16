from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

def test_total_fruit():
    solution = Solution()

    # Test Case 1
    print(solution.totalFruit([1, 2, 1])) # Expected: 3

    # Test Case 2
    print(solution.totalFruit([0, 1, 2, 2])) # Expected: 3

    # Test Case 3
    print(solution.totalFruit([1, 2, 3, 2, 2])) # Expected: 4

    # Test Case 4
    print(solution.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])) # Expected: 5

    # Test Case 5
    print(solution.totalFruit([1])) # Expected: 1

test_total_fruit()