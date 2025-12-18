from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]): 
                    return False
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    break
        return True

def test_is_alien_sorted():
    solution = Solution()

    # Test case 1
    words1 = ["hello","leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    print(solution.isAlienSorted(words1, order1))  # Expected output: True

    # Test case 2
    words2 = ["word","world","row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    print(solution.isAlienSorted(words2, order2))  # Expected output: False

    # Test case 3
    words3 = ["apple","app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"
    print(solution.isAlienSorted(words3, order3))  # Expected output: False

    # Test case 4
    words4 = ["kuvp","q"]
    order4 = "ngxlkthsjuoqcpavbfdermiywz"
    print(solution.isAlienSorted(words4, order4))  # Expected output: True

    # Test case 5
    words5 = ["z","x"]
    order5 = "zyxwvutsrqponmlkjihgfedcba"
    print(solution.isAlienSorted(words5, order5))  # Expected output: True

test_is_alien_sorted()