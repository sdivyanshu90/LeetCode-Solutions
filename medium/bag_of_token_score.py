from typing import List
from collections import deque

class Solution(object):
     def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        deque_tokens = deque(tokens)

        while deque_tokens:
            if power >= deque_tokens[0]:
                power -= deque_tokens.popleft()
                score += 1
            elif len(deque_tokens) > 2 and score > 0:
                power += deque_tokens.pop()
                score -= 1
            else:
                return score

        return score

def test_bag_of_tokens_score():
    solution = Solution()

    # Test case 1
    tokens1 = [100]
    power1 = 50
    print(solution.bagOfTokensScore(tokens1, power1))  # Expected output: 0

    # Test case 2
    tokens2 = [100,200]
    power2 = 150
    print(solution.bagOfTokensScore(tokens2, power2))  # Expected output: 1

    # Test case 3
    tokens3 = [100,200,300,400]
    power3 = 200
    print(solution.bagOfTokensScore(tokens3, power3))  # Expected output: 2

    # Test case 4
    tokens4 = [71,55,82]
    power4 = 54
    print(solution.bagOfTokensScore(tokens4, power4))  # Expected output: 0

    # Test case 5
    tokens5 = [26,87,34,11,23,8]
    power5 = 27
    print(solution.bagOfTokensScore(tokens5, power5))  # Expected output: 3

test_bag_of_tokens_score()