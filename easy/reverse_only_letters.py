class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)

def test_reverse_only_letters():
    solution = Solution()

    # Test Case 1
    print(solution.reverseOnlyLetters("ab-cd")) # Expected: "dc-ba"

    # Test Case 2
    print(solution.reverseOnlyLetters("a-bC-dEf-ghIj")) # Expected: "j-Ih-gfE-dCba"

    # Test Case 3
    print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!")) # Expected: "Qedo1ct-eeLg=ntse-T!"

    # Test Case 4
    print(solution.reverseOnlyLetters("7_28]")) # Expected: "7_28]"

    # Test Case 5
    print(solution.reverseOnlyLetters("a-bC-dEf-ghIj!")) # Expected: "j-Ih-gfE-dCba!"

test_reverse_only_letters()