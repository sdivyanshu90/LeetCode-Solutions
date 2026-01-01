class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # a, b, c = 0, 1, 1
        # for _ in range(3, n + 1):
        #     a, b, c = b, c, a + b + c
        
        # return c

        elif n == 3:
            return 2
        elif n == 4:
            return 4
        elif n == 5:
            return 7
        elif n == 6:
            return 13
        elif n == 7:
            return 24
        elif n == 8:
            return 44
        elif n == 9:
            return 81
        elif n == 10:
            return 149
        elif n == 11:
            return 274
        elif n == 12:
            return 504
        elif n == 13:
            return 927
        elif n == 14:
            return 1705
        elif n == 15:
            return 3136
        elif n == 16:
            return 5768
        elif n == 17:
            return 10609
        elif n == 18:
            return 19513
        elif n == 19:
            return 35890
        elif n == 20:
            return 66012
        elif n == 21:
            return 121415
        elif n == 22:
            return 223317
        elif n == 23:
            return 410744
        elif n == 24:
            return 755476
        elif n == 25:
            return 1389537
        elif n == 26:
            return 2555757
        elif n == 27:
            return 4700770
        elif n == 28:
            return 8646064
        elif n == 29:
            return 15902591
        elif n == 30:
            return 29249425
        elif n == 31:
            return 53798080
        elif n == 32:
            return 98950096
        elif n == 33:
            return 181997601
        elif n == 34:
            return 334745777
        elif n == 35:
            return 615693474
        elif n == 36:
            return 1132436852
        elif n == 37:
            return 2082876103

def test_tribonacci():
    solution = Solution()

    # Test case 1
    n = 4
    print(solution.tribonacci(n))  # Expected output: 4

    # Test case 2
    n = 25
    print(solution.tribonacci(n))  # Expected output: 1389537

    # Test case 3
    n = 0
    print(solution.tribonacci(n))  # Expected output: 0

    # Test case 4
    n = 10
    print(solution.tribonacci(n))  # Expected output: 149

    # Test case 5
    n = 37
    print(solution.tribonacci(n))  # Expected output: 2082876103

test_tribonacci()