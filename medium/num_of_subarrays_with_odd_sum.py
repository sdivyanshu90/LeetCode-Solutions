class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)

        for i in range(n):
            arr[i] %= 2

        dp_even, dp_odd = [0] * n, [0] * n

        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            dp_odd[n - 1] = 1

        for num in range(n - 2, -1, -1):
            if arr[num] == 1:
                dp_odd[num] = (1 + dp_even[num + 1]) % MOD
                dp_even[num] = dp_odd[num + 1]
            else:
                dp_even[num] = (1 + dp_even[num + 1]) % MOD
                dp_odd[num] = dp_odd[num + 1]

        count = 0
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD

        return int(count)

def test_num_of_subarrays():
    solution = Solution()

    # Test case 1
    arr1 = [1, 3, 5]
    print(solution.numOfSubarrays(arr1))  # Expected output: 4

    # Test case 2
    arr2 = [2, 4, 6]
    print(solution.numOfSubarrays(arr2))  # Expected output: 0

    # Test case 3
    arr3 = [1, 2, 3, 4, 5]
    print(solution.numOfSubarrays(arr3))  # Expected output: 9

    # Test case 4
    arr4 = [1, 1, 1]
    print(solution.numOfSubarrays(arr4))  # Expected output: 7

    # Test case 5
    arr5 = [2, 2, 2]
    print(solution.numOfSubarrays(arr5))  # Expected output: 0

test_num_of_subarrays()