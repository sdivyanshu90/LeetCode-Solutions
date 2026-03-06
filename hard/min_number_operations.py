class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res, prev = 0, 0

        for num in target:
            if num > prev:
                res += (num - prev)
            prev = num
        return res

def test_min_number_operations():
    solution = Solution()

    # Test case 1
    target1 = [1, 2, 3, 2, 1]
    print(solution.minNumberOperations(target1))  # Expected output: 3

    # Test case 2
    target2 = [3, 1, 1, 2]
    print(solution.minNumberOperations(target2))  # Expected output: 4

    # Test case 3
    target3 = [1, 1, 1]
    print(solution.minNumberOperations(target3))  # Expected output: 1

    # Test case 4
    target4 = [1, 2, 3]
    print(solution.minNumberOperations(target4))  # Expected output: 3

    # Test case 5
    target5 = [3, 2, 1]
    print(solution.minNumberOperations(target5))  # Expected output: 3

test_min_number_operations()