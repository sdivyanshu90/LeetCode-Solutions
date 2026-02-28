class Solution:
    def maxDiff(self, num: int) -> int:
        def change(x, y):
            return str(num).replace(str(x), str(y))

        min_num = max_num = num
        for x in range(10):
            for y in range(10):
                res = change(x, y)

                if res[0] != "0":
                    res_i = int(res)
                    min_num = min(min_num, res_i)
                    max_num = max(max_num, res_i)

        return max_num - min_num

def test_max_diff():
    solution = Solution()

    # Test case 1
    num1 = 555
    print(solution.maxDiff(num1))  # Expected output: 888

    # Test case 2
    num2 = 9
    print(solution.maxDiff(num2))  # Expected output: 8

    # Test case 3
    num3 = 123456
    print(solution.maxDiff(num3))  # Expected output: 820000

    # Test case 4
    num4 = 10000
    print(solution.maxDiff(num4))  # Expected output: 80000

    # Test case 5
    num5 = 9288
    print(solution.maxDiff(num5))  # Expected output: 8700

test_max_diff()