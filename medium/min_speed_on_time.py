from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calculate_total_time(speed):
            total_time = 0
            for d in dist[:-1]:
                total_time += (d - 1) // speed + 1
            total_time += dist[-1] / speed
            return total_time
        lower_bound = 1
        upper_bound = int(1e7) + 1

        while lower_bound < upper_bound:
            mid = (lower_bound + upper_bound) // 2
            total_time = calculate_total_time(mid)

            if total_time <= hour:
                upper_bound = mid
            else:
                lower_bound = mid + 1

        return lower_bound if lower_bound < int(1e7) + 1 else -1

def test_min_speed_on_time():
    solution = Solution()

    # Test case 1
    dist1 = [1, 3, 2]
    hour1 = 6
    print(solution.minSpeedOnTime(dist1, hour1))  # Expected output: 1

    # Test case 2
    dist2 = [1, 3, 2]
    hour2 = 2.7
    print(solution.minSpeedOnTime(dist2, hour2))  # Expected output: 3

    # Test case 3
    dist3 = [1, 3, 2]
    hour3 = 1.9
    print(solution.minSpeedOnTime(dist3, hour3))  # Expected output: -1

    # Test case 4
    dist4 = [1, 3, 2]
    hour4 = 4.5
    print(solution.minSpeedOnTime(dist4, hour4))  # Expected output: 2

    # Test case 5
    dist5 = [1, 3, 2]
    hour5 = 5.5
    print(solution.minSpeedOnTime(dist5, hour5))  # Expected output: 2

test_min_speed_on_time()