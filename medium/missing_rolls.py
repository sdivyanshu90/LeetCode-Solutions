class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        remaining_sum = mean * (n + len(rolls)) - sum_rolls

        if remaining_sum > 6 * n or remaining_sum < n:
            return []

        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        n_elements = [distribute_mean] * n
        
        for i in range(mod):
            n_elements[i] += 1
        return n_elements

def test_missing_rolls():
    solution = Solution()

    # Test case 1
    rolls1 = [3, 2, 4, 3]
    mean1 = 4
    n1 = 2
    print(solution.missingRolls(rolls1, mean1, n1))  # Expected output: [6, 6]

    # Test case 2
    rolls2 = [1, 5, 6]
    mean2 = 3
    n2 = 4
    print(solution.missingRolls(rolls2, mean2, n2))  # Expected output: [2, 3, 2, 2]

    # Test case 3
    rolls3 = [1, 2, 3, 4]
    mean3 = 6
    n3 = 4
    print(solution.missingRolls(rolls3, mean3, n3))  # Expected output: []

    # Test case 4
    rolls4 = [1]
    mean4 = 3
    n4 = 1
    print(solution.missingRolls(rolls4, mean4, n4))  # Expected output: [5]

    # Test case 5
    rolls5 = [5]
    mean5 = 5
    n5 = 1
    print(solution.missingRolls(rolls5, mean5, n5))  # Expected output: [5]

test_missing_rolls()