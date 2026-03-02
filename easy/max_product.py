class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max, second_max = 0, 0
        
        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        return (first_max - 1) * (second_max - 1)

def test_max_product():
    solution = Solution()

    # Test case 1
    nums = [3, 4, 5, 2]
    print(solution.maxProduct(nums))  # Expected output: 12

    # Test case 2
    nums = [1, 5, 4, 5]
    print(solution.maxProduct(nums))  # Expected output: 16

    # Test case 3
    nums = [3, 7]
    print(solution.maxProduct(nums))  # Expected output: 12

    # Test case 4
    nums = [10, 2, 5, 2]
    print(solution.maxProduct(nums))  # Expected output: 36

    # Test case 5
    nums = [1, 1]
    print(solution.maxProduct(nums))  # Expected output: 0

test_max_product()