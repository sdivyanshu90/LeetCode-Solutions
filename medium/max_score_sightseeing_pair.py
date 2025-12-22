class Solution:
    def maxScoreSightseeingPair(self, values):
        n = len(values)
        max_left_score = [0] * n
        max_left_score[0] = values[0]

        max_score = 0

        for i in range(1, n):
            current_right_score = values[i] - i
            max_score = max(
                max_score, max_left_score[i - 1] + current_right_score
            )

            current_left_score = values[i] + i
            max_left_score[i] = max(max_left_score[i - 1], current_left_score)

        return max_score

def test_max_score_sightseeing_pair():
    solution = Solution()

    # Test case 1
    values1 = [8,1,5,2,6]
    print(solution.maxScoreSightseeingPair(values1))  # Expected output: 11

    # Test case 2
    values2 = [1,2]
    print(solution.maxScoreSightseeingPair(values2))  # Expected output: 2

    # Test case 3
    values3 = [10,7,5,8,7,6,4,3,2,1]
    print(solution.maxScoreSightseeingPair(values3))  # Expected output: 16

    # Test case 4
    values4 = [4,4,4,4]
    print(solution.maxScoreSightseeingPair(values4))  # Expected output: 7

    # Test case 5
    values5 = [1,3,5,7,9]
    print(solution.maxScoreSightseeingPair(values5))  # Expected output: 15

test_max_score_sightseeing_pair()