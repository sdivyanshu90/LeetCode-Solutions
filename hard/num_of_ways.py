class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        type_a = 6
        type_b = 6

        for i in range(2, n + 1):
            new_a = (2 * type_a + 2 * type_b) % MOD
            new_b = (2 * type_a + 3 * type_b) % MOD

            type_a = new_a
            type_b = new_b

        return (type_a + type_b) % MOD

def test_num_of_ways():
    solution = Solution()

    # Test case 1
    n1 = 1
    print(solution.numOfWays(n1))  # Expected output: 6

    # Test case 2
    n2 = 2
    print(solution.numOfWays(n2))  # Expected output: 36

    # Test case 3
    n3 = 3
    print(solution.numOfWays(n3))  # Expected output: 150

    # Test case 4
    n4 = 4
    print(solution.numOfWays(n4))  # Expected output: 780

    # Test case 5
    n5 = 5
    print(solution.numOfWays(n5))  # Expected output: 3906

test_num_of_ways()