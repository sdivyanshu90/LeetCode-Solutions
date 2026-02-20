class Solution:
    def sequentialDigits(self, low, high):
        c = "123456789"
        res = []

        for i in range(len(c)):
            for j in range(i + 1, len(c) + 1):
                curr = int(c[i:j])
                if low <= curr <= high:
                    res.append(curr)

        res.sort()
        return res

def test_sequential_digits():
    solution = Solution()

    # Test case 1
    low, high = 100, 300
    print(solution.sequentialDigits(low, high))  # Expected output: [123, 234]

    # Test case 2
    low, high = 1000, 13000
    print(solution.sequentialDigits(low, high))  # Expected output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

    # Test case 3
    low, high = 10, 1000000000
    print(solution.sequentialDigits(low, high))  # Expected output: [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]

    # Test case 4
    low, high = 58, 155
    print(solution.sequentialDigits(low, high))  # Expected output: [67, 78, 89, 123]

    # Test case 5
    low, high = 10, 99
    print(solution.sequentialDigits(low, high))  # Expected output: [12, 23, 34, 45, 56, 67, 78, 89]

test_sequential_digits()