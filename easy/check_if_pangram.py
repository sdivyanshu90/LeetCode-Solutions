class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for char in sentence:
            if 'a' <= char <= 'z':
                seen.add(char)
            if len(seen) == 26:
                return True
        return False

def test_check_if_pangram():
    solution = Solution()

    # Test Case 1
    sentence1 = "thequickbrownfoxjumpsoverthelazydog"
    print(solution.checkIfPangram(sentence1))  # Expected Output: True

    # Test Case 2
    sentence2 = "leetcode"
    print(solution.checkIfPangram(sentence2))  # Expected Output: False

    # Test Case 3
    sentence3 = "abcefghjklmnopqrstuwxyz"
    print(solution.checkIfPangram(sentence3))  # Expected Output: False

    # Test Case 4
    sentence4 = "thequickbrownfoxjumpsoverthelazydo"
    print(solution.checkIfPangram(sentence4))  # Expected Output: False

    # Test Case 5
    sentence5 = "packmyboxwithfivedozenliquorjugs"
    print(solution.checkIfPangram(sentence5))  # Expected Output: True

test_check_if_pangram()