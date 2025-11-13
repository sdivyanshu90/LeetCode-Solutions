class Solution:
    def find_max(self, score):
        max_score = 0
        for s in score:
            if s > max_score :
                max_score = s
        return max_score

    def findRelativeRanks(self, score):
        N = len(score)

        M = self.find_max(score)
        score_to_index = [0] * (M + 1)
        for i in range(N):
            score_to_index[score[i]] = i + 1

        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        rank = [None] * N
        place = 1
        for i in range(M, -1, -1):
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place < 4:
                    rank[original_index] = MEDALS[place - 1]
                else:
                    rank[original_index] = str(place)
                place += 1
        return rank

def test_find_relative_ranks():
    solution = Solution()

    score1 = [5, 4, 3, 2, 1]
    print(solution.findRelativeRanks(score1)) # Expected: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    score2 = [10, 3, 8, 9, 4]
    print(solution.findRelativeRanks(score2)) # Expected: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

    score3 = [1, 2, 3, 4, 5]
    print(solution.findRelativeRanks(score3)) # Expected: ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]

    score4 = [100, 90, 90, 80]
    print(solution.findRelativeRanks(score4)) # Expected: ["Gold Medal", "Silver Medal", "Bronze Medal", "4"]

    score5 = [50]
    print(solution.findRelativeRanks(score5)) # Expected: ["Gold Medal"]

test_find_relative_ranks()