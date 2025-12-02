class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_digit_index = -1
        swap_idx_1 = -1
        swap_idx_2 = -1

        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i
            elif num_str[i] < num_str[max_digit_index]:
                swap_idx_1 = i
                swap_idx_2 = (
                    max_digit_index
                )

        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = (
                num_str[swap_idx_2],
                num_str[swap_idx_1],
            )

        return int(
            "".join(num_str)
        )

def test_maximum_swap():
    solution = Solution()

    # Test Case 1
    num1 = 2736
    print(solution.maximumSwap(num1))  # Expected: 7236

    # Test Case 2
    num2 = 9973
    print(solution.maximumSwap(num2))  # Expected: 9973

    # Test Case 3
    num3 = 1234
    print(solution.maximumSwap(num3))  # Expected: 4231

    # Test Case 4
    num4 = 98368
    print(solution.maximumSwap(num4))  # Expected: 98863

    # Test Case 5
    num5 = 1993
    print(solution.maximumSwap(num5))  # Expected: 9913

test_maximum_swap()