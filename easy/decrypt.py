from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0 for _ in range(len(code))]
        if k == 0:
            return result

        start, end, window_sum = 1, k, 0

        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        for i in range(start, end + 1):
            window_sum += code[i]

        for i in range(len(code)):
            result[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
        return result

def test_decrypt():
    solution = Solution()

    # Test case 1
    code1 = [5, 7, 1, 4]
    k1 = 3
    print(solution.decrypt(code1, k1))  # Expected output: [12, 10, 16, 13]

    # Test case 2
    code2 = [1, 2, 3, 4]
    k2 = 0
    print(solution.decrypt(code2, k2))  # Expected output: [0, 0, 0, 0]

    # Test case 3
    code3 = [2, 4, 9, 3]
    k3 = -2
    print(solution.decrypt(code3, k3))  # Expected output: [12, 5, 6, 13]

    # Test case 4
    code4 = [1, 2, 3, 4, 5]
    k4 = 2
    print(solution.decrypt(code4, k4))  # Expected output: [5, 7, 9, 6, 3]

    # Test case 5
    code5 = [10, 20, 30, 40, 50]
    k5 = -3
    print(solution.decrypt(code5, k5))  # Expected output: [120, 100, 80, 60, 90]

test_decrypt()