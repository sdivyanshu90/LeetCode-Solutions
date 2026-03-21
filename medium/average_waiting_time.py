class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        net_wait_time = 0

        for customer in customers:
            next_idle_time = max(customer[0], next_idle_time) + customer[1]
            net_wait_time += next_idle_time - customer[0]
        average_wait_time = net_wait_time / len(customers)
        return average_wait_time

def test_average_waiting_time():
    s = Solution()

    # Test Case 1
    customers1 = [[1,2],[2,5],[4,3]]
    print(s.averageWaitingTime(customers1)) # Expected Output: 5.00000

    # Test Case 2
    customers2 = [[5,2],[5,4],[10,3],[20,1]]
    print(s.averageWaitingTime(customers2)) # Expected Output: 3.25000

    # Test Case 3
    customers3 = [[1,1],[2,1],[3,1]]
    print(s.averageWaitingTime(customers3)) # Expected Output: 1.00000

    # Test Case 4
    customers4 = [[0,3],[1,9],[2,6]]
    print(s.averageWaitingTime(customers4)) # Expected Output: 9.00000

    # Test Case 5
    customers5 = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    print(s.averageWaitingTime(customers5)) # Expected Output: 11.20000

test_average_waiting_time()