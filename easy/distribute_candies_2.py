from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        idx = 0
        i = 1

        while candies > 0:
            res[idx] += min(candies, i)
            idx = (idx + 1) % len(res)
            candies -= i
            i += 1
        return res

def test_distribite_candies():
    solution = Solution()

    # Test case 1
    candies = 7
    num_people = 4
    print(solution.distributeCandies(candies, num_people))  # Expected output: [1,2,3,1]

    # Test case 2
    candies = 10
    num_people = 3
    print(solution.distributeCandies(candies, num_people))  # Expected output: [5,2,3]

    # Test case 3
    candies = 1
    num_people = 1
    print(solution.distributeCandies(candies, num_people))  # Expected output: [1]

    # Test case 4
    candies = 15
    num_people = 5
    print(solution.distributeCandies(candies, num_people))  # Expected output: [1,2,3,4,5]

    # Test case 5
    candies = 20
    num_people = 4
    print(solution.distributeCandies(candies, num_people))  # Expected output: [6,7,3,4]

test_distribite_candies()