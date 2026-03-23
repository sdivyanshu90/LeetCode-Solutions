class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digit_sum(num: int) -> int:
            return sum(map(int, str(num)))
        
        freq = {}
        for i in range(lowLimit, highLimit + 1):
            dig = digit_sum(i)
            if dig in freq:
                freq[dig] += 1
            else:
                freq[dig] = 1

        return max(freq.values())

def test_count_balls():
    solution = Solution()

    # Test case 1
    lowLimit = 1
    highLimit = 10
    print(solution.countBalls(lowLimit, highLimit))  # Expected output: 2

    # Test case 2
    lowLimit = 5
    highLimit = 15
    print(solution.countBalls(lowLimit, highLimit))  # Expected output: 2

    # Test case 3
    lowLimit = 19
    highLimit = 28
    print(solution.countBalls(lowLimit, highLimit))  # Expected output: 2

    # Test case 4
    lowLimit = 1
    highLimit = 1000
    print(solution.countBalls(lowLimit, highLimit))  # Expected output: 3

    # Test case 5
    lowLimit = 123
    highLimit = 321
    print(solution.countBalls(lowLimit, highLimit))  # Expected output: 3

test_count_balls()