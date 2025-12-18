from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        queue = deque()

        for i in range(N):
            queue.append(i)
        
        deck.sort()

        result = [0] * N
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
                
        return result

def test_deck_revealed_increasing():
    solution = Solution()

    # Test case 1
    deck1 = [17,13,11,2,3,5,7]
    print(solution.deckRevealedIncreasing(deck1))  # Expected output: [2, 13, 3, 11, 5, 17, 7]

    # Test case 2
    deck2 = [1,1000]
    print(solution.deckRevealedIncreasing(deck2))  # Expected output: [1, 1000]

    # Test case 3
    deck3 = [3,6,9,1,4,7]
    print(solution.deckRevealedIncreasing(deck3))  # Expected output: [1, 6, 3, 9, 4, 7]

    # Test case 4
    deck4 = [10,20,30,40,50]
    print(solution.deckRevealedIncreasing(deck4))  # Expected output: [10, 50, 20, 40, 30]

    # Test case 5
    deck5 = [5]
    print(solution.deckRevealedIncreasing(deck5))  # Expected output: [5]

test_deck_revealed_increasing()