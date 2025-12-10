from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        visited_routes = set()
        visited_stops = set()

        queue = deque([(source, 0)])

        while queue:
            current_stop, num_buses = queue.popleft()

            if current_stop == target:
                return num_buses

            for route_index in stop_to_routes[current_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    for next_stop in routes[route_index]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, num_buses + 1))

        return -1

def test_num_buses_to_destination():
    solution = Solution()

    # Test Case 1
    routes1 = [[1,2,7],[3,6,7]]
    source1 = 1
    target1 = 6
    print(solution.numBusesToDestination(routes1, source1, target1)) # Expected: 2

    # Test Case 2
    routes2 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source2 = 15
    target2 = 12
    print(solution.numBusesToDestination(routes2, source2, target2)) # Expected: -1

    # Test Case 3
    routes3 = [[1,2,3],[3,4,5],[5,6,7],[7,8,9]]
    source3 = 1
    target3 = 9
    print(solution.numBusesToDestination(routes3, source3, target3)) # Expected: 4

    # Test Case 4
    routes4 = [[1,5,7],[3,5,9],[2,6,8]]
    source4 = 1
    target4 = 6
    print(solution.numBusesToDestination(routes4, source4, target4)) # Expected: -1

    # Test Case 5
    routes5 = [[1,2,3],[4,5,6],[7,8,9],[2,4,6],[3,5,7]]
    source5 = 1
    target5 = 9
    print(solution.numBusesToDestination(routes5, source5, target5)) # Expected: 3

test_num_buses_to_destination()