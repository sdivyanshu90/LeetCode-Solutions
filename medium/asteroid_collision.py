from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack != [] and (i < 0 and stack[-1] > 0):
                if -i > stack[-1]:
                    stack.pop()
                    continue
                if -i == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack

def test_asteroid_collision():
    solution = Solution()

    # Test Case 1
    asteroids = [5, 10, -5]
    print(solution.asteroidCollision(asteroids))  # Expected: [5, 10]

    # Test Case 2
    asteroids = [8, -8]
    print(solution.asteroidCollision(asteroids))  # Expected: []

    # Test Case 3: No collisions
    asteroids = [1, 2, 3, 4, 5]
    print(solution.asteroidCollision(asteroids))  # Expected: [1, 2, 3, 4, 5]

    # Test Case 4: All asteroids collide and destroy each other
    asteroids = [10, -10, 5, -5]
    print(solution.asteroidCollision(asteroids))  # Expected: []

    # Test Case 5: Mixed sizes with collisions
    asteroids = [3, 2, -4, -1, 5, -6]
    print(solution.asteroidCollision(asteroids))  # Expected: [-4, 5]

    # Test Case 6: Large asteroid destroys smaller ones
    asteroids = [20, -5, -15, -25]
    print(solution.asteroidCollision(asteroids))  # Expected: [20]

    # Test Case 7: Edge case with single asteroid
    asteroids = [-1]
    print(solution.asteroidCollision(asteroids))  # Expected: [-1]

    # Test Case 8: Edge case with two asteroids of equal size
    asteroids = [7, -7]
    print(solution.asteroidCollision(asteroids))  # Expected: []

    # Test Case 9: Multiple collisions in sequence
    asteroids = [10, 2, -5, -15, 20, -10]
    print(solution.asteroidCollision(asteroids))  # Expected: [10, 20]

    # Test Case 10: All asteroids moving in the same direction
    asteroids = [1, 2, 3, 4, 5]
    print(solution.asteroidCollision(asteroids))  # Expected: [1, 2, 3, 4, 5]

test_asteroid_collision()