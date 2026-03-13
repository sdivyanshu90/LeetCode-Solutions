from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = i = 0
        n = len(colors)
        while i < n:
            j = i
            s = mx = 0
            while j < n and colors[j] == colors[i]:
                s += neededTime[j]
                if mx < neededTime[j]:
                    mx = neededTime[j]
                j += 1
            if j - i > 1:
                ans += s - mx
            i = j
        return ans

def test_min_cost():
    solution = Solution()

    # Test case 1
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    print(solution.minCost(colors, neededTime))  # Expected output: 3

    # Test case 2
    colors = "abc"
    neededTime = [1, 2, 3]
    print(solution.minCost(colors, neededTime))  # Expected output: 0

    # Test case 3
    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    print(solution.minCost(colors, neededTime))  # Expected output: 2

    # Test case 4
    colors = "aaabbbabbbb"
    neededTime = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
    print(solution.minCost(colors, neededTime))  # Expected output: 26

    # Test case 5
    colors = "a"
    neededTime = [1]
    print(solution.minCost(colors, neededTime))  # Expected output: 0

test_min_cost()