from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums_length = len(nums)
        pair_products_frequency = {}
        total_number_of_tuples = 0

        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                product_value = nums[first_index] * nums[second_index]
                if product_value in pair_products_frequency:
                    pair_products_frequency[product_value] += 1
                else:
                    pair_products_frequency[product_value] = 1

        for product_frequency in pair_products_frequency.values():
            pairs_of_equal_product = (
                (product_frequency - 1) * product_frequency // 2
            )

            total_number_of_tuples += 8 * pairs_of_equal_product

        return total_number_of_tuples

def test_tuple_same_product():
    solution = Solution()

    # Test case 1
    nums = [2, 3, 4, 6]
    print(solution.tupleSameProduct(nums))  # Expected output: 8

    # Test case 2
    nums = [1, 2, 4, 5, 10]
    print(solution.tupleSameProduct(nums))  # Expected output: 16

    # Test case 3
    nums = [2, 3, 4, 6, 8, 12]
    print(solution.tupleSameProduct(nums))  # Expected output: 40

    # Test case 4
    nums = [1, 1, 1, 1]
    print(solution.tupleSameProduct(nums))  # Expected output: 120

    # Test case 5
    nums = [2, 3, 5, 7]
    print(solution.tupleSameProduct(nums))  # Expected output: 0

test_tuple_same_product()