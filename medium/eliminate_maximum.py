class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = []
        for i in range(len(dist)):
            arrival.append(dist[i] / speed[i])
        
        arrival.sort()
        ans = 0

        for i in range(len(arrival)):
            if arrival[i] <= i:
                break
                
            ans += 1

        return ans

def test_eliminate_maximum():
    solution = Solution()

    # Test case 1
    dist1 = [1, 3, 4]
    speed1 = [1, 1, 1]
    print(solution.eliminateMaximum(dist1, speed1))  # Expected output: 3

    # Test case 2
    dist2 = [1, 1, 2]
    speed2 = [1, 1, 1]
    print(solution.eliminateMaximum(dist2, speed2))  # Expected output: 2

    # Test case 3
    dist3 = [3, 2, 4]
    speed3 = [5, 3, 2]
    print(solution.eliminateMaximum(dist3, speed3))  # Expected output: 1

    # Test case 4
    dist4 = [10, 8, 0, 5, 3]
    speed4 = [2, 4, 11, 1, 1]
    print(solution.eliminateMaximum(dist4, speed4))  # Expected output: 3

    # Test case 5
    dist5 = [1, 2, 3]
    speed5 = [1, 1, 1]
    print(solution.eliminateMaximum(dist5, speed5))  # Expected output: 3

test_eliminate_maximum()