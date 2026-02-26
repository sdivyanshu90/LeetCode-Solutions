class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]
        for i in range(n):
            increasing_teams[i][1] = 1
            decreasing_teams[i][1] = 1
        for count in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] += increasing_teams[i][
                            count - 1
                        ]
                    if rating[j] < rating[i]:
                        decreasing_teams[j][count] += decreasing_teams[i][
                            count - 1
                        ]

        for i in range(n):
            teams += increasing_teams[i][3] + decreasing_teams[i][3]

        return teams

def test_num_teams():
    solution = Solution()

    # Test case 1
    rating1 = [2, 5, 3, 4, 1]
    print(solution.numTeams(rating1))  # Expected output: 3

    # Test case 2
    rating2 = [2, 1, 3]
    print(solution.numTeams(rating2))  # Expected output: 0

    # Test case 3
    rating3 = [1, 2, 3, 4]
    print(solution.numTeams(rating3))  # Expected output: 4

    # Test case 4
    rating4 = [4, 3, 2, 1]
    print(solution.numTeams(rating4))  # Expected output: 4

    # Test case 5
    rating5 = [1, 3, 2, 4]
    print(solution.numTeams(rating5))  # Expected output: 2

test_num_teams()