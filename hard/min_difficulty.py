class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        acc, maxs = jobDifficulty[:], jobDifficulty[:]
        if d > n:
            return -1
        for i in range(n-2, -1, -1):
            acc[i] += acc[i+1]
            if maxs[i] < maxs[i+1]:
                maxs[i] = maxs[i+1]

        @functools.lru_cache(None)
        def dp(ind: int, k: int) -> int:
            if ind + k == n:
                return acc[ind]
            if k == 1:
                return maxs[ind]

            curMax, minDiff = jobDifficulty[ind], inf
            for i in range(ind+1, n-k+2):
                curDiff = curMax + dp(i, k-1)
                if minDiff > curDiff:
                    minDiff = curDiff
                if curMax < jobDifficulty[i]:
                    curMax = jobDifficulty[i]
            return minDiff

        return dp(0, d)

def test_minDifficulty():
    solution = Solution()

    # Test case 1
    jobDifficulty = [6,5,4,3,2,1]
    d = 2
    expected = 7
    print(solution.minDifficulty(jobDifficulty, d))  # Expected Output: 7

    # Test case 2
    jobDifficulty = [9,9,9]
    d = 4
    expected = -1
    print(solution.minDifficulty(jobDifficulty, d))  # Expected Output: -1

    # Test case 3
    jobDifficulty = [1,1,1]
    d = 3
    expected = 3
    print(solution.minDifficulty(jobDifficulty, d))  # Expected Output: 3

    # Test case 4
    jobDifficulty = [7,1,7,1,7,1]
    d = 3
    expected = 15
    print(solution.minDifficulty(jobDifficulty, d))  # Expected Output: 15

    # Test case 5
    jobDifficulty = [11,111,22,222,33,333,44,444]
    d = 6
    expected = 843
    print(solution.minDifficulty(jobDifficulty, d))  # Expected Output: 843

test_minDifficulty()