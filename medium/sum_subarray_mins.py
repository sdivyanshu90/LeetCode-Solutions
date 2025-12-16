from typing import List

class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []
        mod = 10**9 + 7

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 

        stack = [] 
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod      
        return result

def test_sum_subarray_mins():
    solution = Solution()

    # Test Case 1
    print(solution.sumSubarrayMins([3, 1, 2, 4])) # Expected: 17

    # Test Case 2
    print(solution.sumSubarrayMins([11, 81, 94, 43, 3])) # Expected: 444

    # Test Case 3
    print(solution.sumSubarrayMins([1, 1, 1])) # Expected: 10

    # Test Case 4
    print(solution.sumSubarrayMins([5, 4, 3, 2, 1])) # Expected: 35

    # Test Case 5
    print(solution.sumSubarrayMins([2, 9, 7, 8, 3, 4, 6, 1])) # Expected: 129

test_sum_subarray_mins()