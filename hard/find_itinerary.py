from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]

def test_find_itinerary():
    s = Solution()

    # Test Case 1: Example with multiple valid itineraries
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']

    # Test Case 2: Tickets with same departure and arrival
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'NRT', 'JFK', 'KUL']

    # Test Case 3: Single ticket
    tickets = [["JFK","ATL"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'ATL']

    # Test Case 4: Multiple tickets with same routes
    tickets = [["JFK","ATL"],["JFK","ATL"],["ATL","JFK"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'ATL', 'JFK', 'ATL']

    # Test Case 5: Complex itinerary with multiple stops
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'ATL', 'SFO', 'JFK', 'SFO', 'ATL']

    # Test Case 6: Itinerary with lexicographical order requirement
    tickets = [["JFK","AAA"],["JFK","BBB"],["AAA","JFK"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'AAA', 'JFK', 'BBB']

    # Test Case 7: Itinerary with cycles
    tickets = [["JFK","A"],["A","B"],["B","A"],["A","JFK"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'A', 'B', 'A', 'JFK']

    # Test Case 8: Itinerary with multiple identical tickets
    tickets = [["JFK","A"],["JFK","A"],["A","JFK"]]
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'A', 'JFK', 'A']

    # Test Case 9: Large number of tickets
    tickets = [["JFK","A"]]*100 + [["A","JFK"]]*10
    print(s.findItinerary(tickets))  # Expected: ['JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'JFK', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']

    # Test Case 10: Edge case with no tickets
    tickets = []
    print(s.findItinerary(tickets))  # Expected: ['JFK']

test_find_itinerary()