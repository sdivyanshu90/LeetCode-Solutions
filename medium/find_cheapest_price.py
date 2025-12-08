from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = defaultdict(list)
        visited = [float('inf')] * n
        visited[src] = 0
        
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
            
        queue = deque([(src, 0)])
        K += 1
        
        while K > 0 and queue:
            size = len(queue)
            while size > 0:
                curr_node, curr_price = queue.popleft()
                for neighbor, price in adj[curr_node]:
                    new_price = curr_price + price
                    if new_price < visited[neighbor]:
                        visited[neighbor] = new_price
                        queue.append((neighbor, new_price))
                size -= 1
            K -= 1
        
        return visited[dst] if visited[dst] != float('inf') else -1

def test_find_cheapest_price():
    solution = Solution()
    
    # Test case 1
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    K = 1
    print(solution.findCheapestPrice(n, flights, src, dst, K)) # Expected: 200
    
    # Test case 2
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    K = 0
    print(solution.findCheapestPrice(n, flights, src, dst, K)) # Expected: 500
    
    # Test case 3
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    K = 1
    print(solution.findCheapestPrice(n, flights, src, dst, K)) # Expected: 700

    # Test case 4
    n = 5
    flights = [[0,1,10],[0,2,5],[1,2,2],[1,3,1],[2,1,3],[2,3,9],[2,4,2],[3,4,4],[4,3,6]]
    src = 0
    dst = 4
    K = 2
    print(solution.findCheapestPrice(n, flights, src, dst, K)) # Expected: 7

    # Test case 5
    n = 3
    flights = [[0,1,200],[1,2,200],[0,2,500]]
    src = 0
    dst = 2
    K = 1
    print(solution.findCheapestPrice(n, flights, src, dst, K)) # Expected: 400

test_find_cheapest_price()