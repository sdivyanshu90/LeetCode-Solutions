from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        clockwise_distance = 0
        anticlockwise_distance = 0
        total_distance = sum(distance)
        
        for i in range(start, destination):
            clockwise_distance += distance[i]
        
        anticlockwise_distance = total_distance - clockwise_distance
        
        return min(clockwise_distance, anticlockwise_distance)

def test_distance_between_bus_stops():
    solution = Solution()

    # Test Case 1
    distance = [1,2,3,4]
    start = 0
    destination = 1
    print(solution.distanceBetweenBusStops(distance, start, destination)) # Expected Output: 1

    # Test Case 2
    distance = [1,2,3,4]
    start = 0
    destination = 2
    print(solution.distanceBetweenBusStops(distance, start, destination)) # Expected Output: 3

    # Test Case 3
    distance = [1,2,3,4]
    start = 0
    destination = 3
    print(solution.distanceBetweenBusStops(distance, start, destination)) # Expected Output: 4

    # Test Case 4
    distance = [7,10,1,12,11,14,5,0]
    start = 7
    destination = 2
    print(solution.distanceBetweenBusStops(distance, start, destination)) # Expected Output: 17

    # Test Case 5
    distance = [3,6,7,2,9,10]
    start = 3
    destination = 5
    print(solution.distanceBetweenBusStops(distance, start, destination)) # Expected Output: 12

test_distance_between_bus_stops()