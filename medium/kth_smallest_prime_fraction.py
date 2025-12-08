import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        pq = []
        def compare(a, b):
            return a[0] - b[0]

        for i in range(len(arr)):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))

        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (
                    (arr[numerator_index] / arr[denominator_index]), 
                    numerator_index, 
                    denominator_index
                ))
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]

def test_kth_smallest_prime_fraction():
    solution = Solution()
    
    # Test case 1
    arr = [1,2,3,5]
    k = 3
    print(solution.kthSmallestPrimeFraction(arr, k)) # Expected: [2,5]
    
    # Test case 2
    arr = [1,7]
    k = 1
    print(solution.kthSmallestPrimeFraction(arr, k)) # Expected: [1,7]
    
    # Test case 3
    arr = [1,13,17,59]
    k = 6
    print(solution.kthSmallestPrimeFraction(arr, k)) # Expected: [13,17]

    # Test case 4
    arr = [1,19,29,59,61,67,71,73,79,83]
    k = 18
    print(solution.kthSmallestPrimeFraction(arr, k)) # Expected: [29,79]

    # Test case 5
    arr = [1,3,7,11,13]
    k = 8
    print(solution.kthSmallestPrimeFraction(arr, k)) # Expected: [7,13]

test_kth_smallest_prime_fraction()