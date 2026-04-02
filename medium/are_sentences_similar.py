from collections import deque

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        deque1 = list(s1.split())
        deque2 = list(s2.split())
        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.pop(0)
            deque2.pop(0)

        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop(-1)
            deque2.pop(-1)
        return not deque1 or not deque2

def test_are_sentences_similar():
    solution = Solution()

    # Test Case 1
    s1_1 = "My name is Haley"
    s2_1 = "Me Haley"
    print(solution.areSentencesSimilar(s1_1, s2_1))  # Expected Output: False

    # Test Case 2
    s1_2 = "of"
    s2_2 = "A lot of words"
    print(solution.areSentencesSimilar(s1_2, s2_2))  # Expected Output: False

    # Test Case 3
    s1_3 = "Eating right now"
    s2_3 = "Eating"
    print(solution.areSentencesSimilar(s1_3, s2_3))  # Expected Output: True

    # Test Case 4
    s1_4 = "Luky"
    s2_4 = "Lucccky"
    print(solution.areSentencesSimilar(s1_4, s2_4))  # Expected Output: False

    # Test Case 5
    s1_5 = "A B C D E F G"
    s2_5 = "A B C D E F G"
    print(solution.areSentencesSimilar(s1_5, s2_5))  # Expected Output: True

test_are_sentences_similar()