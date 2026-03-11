class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0]*n
        for i in range(n):
            arr[i] = (2 * i) + 1
        target = sum(arr) // n
        step = 0
        for i in range(n - 1, n // 2 - 1, -1):
            if target < arr[i]:
                step += arr[i] - target
            else:
                break

        return step

def test_min_operations():
    solution = Solution()

    # Test case 1
    n1 = 3
    print(solution.minOperations(n1))  # Expected output: 2

    # Test case 2
    n2 = 6
    print(solution.minOperations(n2))  # Expected output: 9

    # Test case 3
    n3 = 1
    print(solution.minOperations(n3))  # Expected output: 0

    # Test case 4
    n4 = 10
    print(solution.minOperations(n4))  # Expected output: 25

    # Test case 5
    n5 = 5555
    print(solution.minOperations(n5))  # Expected output: 7714506

test_min_operations()