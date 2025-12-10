class Solution:
    def soupServings(self, n: int) -> float:
        memo = {}
        
        def serve(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.0
            elif b <= 0:
                return 0.0
            elif (a, b) not in memo:
                memo[a, b] = 0.25 * (serve(a - 100, b) + serve(a - 75, b - 25) + serve(a - 50, b - 50) + serve(a - 25, b - 75))
            return memo[a, b]
        
        if n >= 4500:
            return 1.0

        return serve(n, n)

def test_soup_servings():
    solution = Solution()

    # Test Case 1
    n1 = 50
    print(solution.soupServings(n1)) # Expected: 0.62500

    # Test Case 2
    n2 = 100
    print(solution.soupServings(n2)) # Expected: 0.71875

    # Test Case 3
    n3 = 200
    print(solution.soupServings(n3)) # Expected: 0.796875

    # Test Case 4
    n4 = 0
    print(solution.soupServings(n4)) # Expected: 0.5

    # Test Case 5
    n5 = 5000
    print(solution.soupServings(n5)) # Expected: 1.0

test_soup_servings()