class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_time = times[targetFriend]
        times.sort()

        n = len(times)
        chair_time = [0] * n

        for time in times:
            for i in range(n):
                if chair_time[i] <= time[0]:
                    chair_time[i] = time[1]
                    if time == target_time:
                        return i
                    break
        return 0

def test_smallest_chair():
    solution = Solution()

    # Test Case 1
    times1 = [[1, 4], [2, 3], [4, 6]]
    targetFriend1 = 1
    print(solution.smallestChair(times1, targetFriend1))  # Expected output: 1

    # Test Case 2
    times2 = [[3, 10], [1, 5], [2, 6]]
    targetFriend2 = 0
    print(solution.smallestChair(times2, targetFriend2))  # Expected output: 0

    # Test Case 3
    times3 = [[0, 10], [1, 5], [2, 6]]
    targetFriend3 = 0
    print(solution.smallestChair(times3, targetFriend3))  # Expected output: 1

    # Test Case 4
    times4 = [[0, 10], [1, 5], [2, 6]]
    targetFriend4 = 1
    print(solution.smallestChair(times4, targetFriend4))  # Expected output: 0

    # Test Case 5
    times5 = [[0, 10], [1, 5], [2, 6]]
    targetFriend5 = 2
    print(solution.smallestChair(times5, targetFriend5))  # Expected output: 0

test_smallest_chair()