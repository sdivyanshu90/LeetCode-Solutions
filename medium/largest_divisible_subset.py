from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        groupSize = [1] * n
        prevElement = [-1] * n
        maxIndex = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if groupSize[i] < 1 + groupSize[j]:
                        groupSize[i] = 1 + groupSize[j]
                        prevElement[i] = j
            if groupSize[i] > groupSize[maxIndex]:
                maxIndex = i

        result = []
        while maxIndex != -1:
            result.insert(0, nums[maxIndex])
            maxIndex = prevElement[maxIndex]

        return result


def test_largest_divisible_subset():
    solution = Solution()
    
    # Test case 1
    print(solution.largestDivisibleSubset([1,2,3])) # Expected output: [1,2]
    
    # Test case 2
    print(solution.largestDivisibleSubset([1,2,4,8])) # Expected output: [1,2,4,8]

    # Test case 3: Edge case - single element
    print(solution.largestDivisibleSubset([5])) # Expected output: [5]

    # Test case 4: No divisible pairs
    print(solution.largestDivisibleSubset([3,5,7,11])) # Expected output: [3]
    
    # Test case 5: Mixed elements
    print(solution.largestDivisibleSubset([4,8,10,240])) # Expected output: [4,8,240]

    # Test case 6: Larger input
    print(solution.largestDivisibleSubset([2,3,4,9,8,27,81])) # Expected output: [3,9,27,81]

    # Test case 7: All elements are the same
    print(solution.largestDivisibleSubset([6,6,6,6])) # Expected output: [6,6,6,6]

    # Test case 8: Large numbers
    print(solution.largestDivisibleSubset([100,200,300,400,500,600])) # Expected output: [100,200,400]

    # Test case 9: Prime numbers
    print(solution.largestDivisibleSubset([2,3,5,7,11,13])) # Expected output: [2]

    # Test case 10: Mixed elements
    print(solution.largestDivisibleSubset([3,9,27])) # Expected output: [3, 9, 27]

test_largest_divisible_subset()