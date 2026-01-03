from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        
        return min(
            char_count['b'],
            char_count['a'],
            char_count['l'] // 2,
            char_count['o'] // 2,
            char_count['n']
        )

def test_max_number_of_balloons():
    solution = Solution()

    # Test Case 1
    text = "nlaebolko"
    print(solution.maxNumberOfBalloons(text)) # Expected Output: 1

    # Test Case 2
    text = "loonbalxballpoon"
    print(solution.maxNumberOfBalloons(text)) # Expected Output: 2

    # Test Case 3
    text = "leetcode"
    print(solution.maxNumberOfBalloons(text)) # Expected Output: 0

    # Test Case 4
    text = "balon"
    print(solution.maxNumberOfBalloons(text)) # Expected Output: 0

    # Test Case 5
    text = "balloonballoonballoon"
    print(solution.maxNumberOfBalloons(text)) # Expected Output: 3

test_max_number_of_balloons()