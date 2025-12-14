from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = lo = 0
        hi = len(people) - 1

        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            ans += 1
        return ans

def test_num_rescue_boats():
    solution = Solution()

    # Test case 1
    people1 = [1, 2]
    limit1 = 3
    print(solution.numRescueBoats(people1, limit1))  # Expected output: 1

    # Test case 2
    people2 = [3, 2, 2, 1]
    limit2 = 3
    print(solution.numRescueBoats(people2, limit2))  # Expected output: 3

    # Test case 3
    people3 = [3, 5, 3, 4]
    limit3 = 5
    print(solution.numRescueBoats(people3, limit3))  # Expected output: 4

    # Test case 4
    people4 = [2, 4]
    limit4 = 5
    print(solution.numRescueBoats(people4, limit4))  # Expected output: 2

    # Test case 5
    people5 = [1, 1, 1, 1, 1, 1]
    limit5 = 3
    print(solution.numRescueBoats(people5, limit5))  # Expected output: 3

test_num_rescue_boats()