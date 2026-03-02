class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def condition(days) -> bool:

            flowers = 0
            bouquets = 0

            for bloom in bloomDay:

                if bloom <= days:
                    flowers += 1
                else:
                    bouquets += flowers // k
                    flowers = 0
                    
            bouquets += flowers // k
            return bouquets >= m

        if len(bloomDay) < m * k:
            return -1

        left = 1
        right = max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

def test_min_days():
    solution = Solution()

    # Test case 1
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    print(solution.minDays(bloomDay, m, k))  # Expected output: 3

    # Test case 2
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 2
    print(solution.minDays(bloomDay, m, k))  # Expected output: -1

    # Test case 3
    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3
    print(solution.minDays(bloomDay, m, k))  # Expected output: 12

    # Test case 4
    bloomDay = [1000000000,1000000000]
    m = 1
    k = 1
    print(solution.minDays(bloomDay, m, k))  # Expected output: 1000000000

    # Test case 5
    bloomDay = [1,10,2,9,3,8,4,7,5,6]
    m = 4
    k = 2
    print(solution.minDays(bloomDay, m, k))  # Expected output: -1

test_min_days()