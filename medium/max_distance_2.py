from typing import List

class Solution:
    def can_place_balls(self, x, position, m):
        prev_ball_pos = position[0]
        balls_placed = 1

        for i in range(1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_ball_pos >= x:
                balls_placed += 1
                prev_ball_pos = curr_pos
            if balls_placed == m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        answer = 0
        n = len(position)
        position.sort()

        low = 1
        high = int(position[-1] / (m - 1.0)) + 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.can_place_balls(mid, position, m):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer


def test_max_distance():
    solution = Solution()

    # Test case 1
    position1 = [1, 2, 3, 4, 7]
    m1 = 3
    print(solution.maxDistance(position1, m1))  # Expected output: 3

    # Test case 2
    position2 = [5, 4, 3, 2, 1, 1000000000]
    m2 = 2
    print(solution.maxDistance(position2, m2))  # Expected output: 999999999

    # Test case 3
    position3 = [1, 3, 5]
    m3 = 2
    print(solution.maxDistance(position3, m3))  # Expected output: 4

    # Test case 4
    position4 = [1, 2, 3]
    m4 = 2
    print(solution.maxDistance(position4, m4))  # Expected output: 2

    # Test case 5
    position5 = [1, 10]
    m5 = 2
    print(solution.maxDistance(position5, m5))  # Expected output: 9

test_max_distance()