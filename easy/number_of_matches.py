class Solution:
    def numberOfMatches(self, n: int) -> int:
        n_matches = 0
        while n > 1:
            if n % 2 == 0:
                n_matches += int(n / 2)
                n = int(n/2)
            else:
                n_matches += int((n - 1) / 2)
                n = int((n - 1) / 2 + 1)

        return n_matches

def test_number_of_matches():
    solution = Solution()

    # Test case 1
    n = 7
    print(solution.numberOfMatches(n))  # Expected output: 6

    # Test case 2
    n = 14
    print(solution.numberOfMatches(n))  # Expected output: 13

    # Test case 3
    n = 1
    print(solution.numberOfMatches(n))  # Expected output: 0

    # Test case 4
    n = 2
    print(solution.numberOfMatches(n))  # Expected output: 1

    # Test case 5
    n = 3
    print(solution.numberOfMatches(n))  # Expected output: 2

test_number_of_matches()