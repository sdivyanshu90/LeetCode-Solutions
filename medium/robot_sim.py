from typing import List

class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER = (
            60001
        )

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0

        for command in commands:
            if command == -1:
                current_direction = (current_direction + 1) % 4
                continue

            if command == -2:
                current_direction = (current_direction + 3) % 4
                continue

            dx, dy = directions[current_direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if self._hash_coordinates(next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y

            max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared

    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + self.HASH_MULTIPLIER * y

def test_robot_sim():
    solution = Solution()

    # Test case 1
    commands1 = [4, -1, 3]
    obstacles1 = []
    print(solution.robotSim(commands1, obstacles1))  # Expected output: 25

    # Test case 2
    commands2 = [4, -1, 4, -2, 4]
    obstacles2 = [[2, 4]]
    print(solution.robotSim(commands2, obstacles2))  # Expected output: 65

    # Test case 3
    commands3 = [6, -1, -1, 6]
    obstacles3 = []
    print(solution.robotSim(commands3, obstacles3))  # Expected output: 36

    # Test case 4
    commands4 = [7, -2, -2, 7, 5]
    obstacles4 = [[-3, 2], [2, -3], [0, 1], [4, 2], [3, 3], [5, 5], [1, -4]]
    print(solution.robotSim(commands4, obstacles4))  # Expected output: 25

    # Test case 5
    commands5 = [1, 2, 3, 4, 5]
    obstacles5 = [[1, 0], [2, 2], [3, 3]]
    print(solution.robotSim(commands5, obstacles5))  # Expected output: 26

test_robot_sim()