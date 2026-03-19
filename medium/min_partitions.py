class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(digit) for digit in n)

def test_min_partitions():
    solution = Solution()

    # Test case 1
    n = "32"
    print(solution.minPartitions(n))  # Expected output: 3

    # Test case 2
    n = "82734"
    print(solution.minPartitions(n))  # Expected output: 8

    # Test case 3
    n = "27346209830709182346"
    print(solution.minPartitions(n))  # Expected output: 9

    # Test case 4
    n = "0"
    print(solution.minPartitions(n))  # Expected output: 0

    # Test case 5
    n = "99999999999999999999"
    print(solution.minPartitions(n))  # Expected output: 9

test_min_partitions()