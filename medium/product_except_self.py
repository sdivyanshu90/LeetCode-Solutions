from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [0] * n
        
        product[0] = 1
        for i in range(1, n):
            product[i] = nums[i - 1] * product[i - 1]
        
        suffixProduct = 1
        for i in range(n - 1, -1, -1):
            product[i] = product[i] * suffixProduct
            suffixProduct = suffixProduct * nums[i]

        return product

def test_product_except_self():
    s = Solution()

    # Test Case 1: Standard list of positive integers
    nums = [1, 2, 3, 4]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [24, 12, 8, 6]

    # Test Case 2: List containing one zero
    nums = [1, 2, 0, 4]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [0, 0, 8, 0]

    # Test Case 3: List containing multiple zeros
    nums = [1, 0, 3, 0]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [0, 0, 0, 0]

    # Test Case 4: List with negative numbers (even count)
    nums = [-1, 2, -3, 4]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [-24, 12, -8, 6]

    # Test Case 5: List with negative numbers (odd count)
    nums = [-1, -2, -3]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [6, 3, 2]

    # Test Case 6: List containing ones
    nums = [1, 1, 2, 5]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [10, 10, 5, 2]

    # Test Case 7: Smallest valid list (two elements)
    nums = [9, 8]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [8, 9]

    # Test Case 8: A longer list
    nums = [2, 3, 4, 5, 6]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [360, 240, 180, 144, 120]

    # Test Case 9: Mix of positive, negative, and zero
    nums = [-1, 1, 0, -3, 3]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [0, 0, 9, 0, 0]

    # Test Case 10: All elements are the same
    nums = [5, 5, 5, 5]
    print(f"\nInput: {nums}")
    print(f"Output: {s.productExceptSelf(nums)}") # Expected: [125, 125, 125, 125]

test_product_except_self()