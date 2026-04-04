class Solution:
    def replaceDigits(self, s: str) -> str:
        temp = []
        for i in range(0, len(s), 2):
            temp.append(s[i:i+2])
        
        alpha = {letter: index for index, letter in enumerate(string.ascii_lowercase, start = 1)}
        rev_alpha = {index: letter for letter, index in (alpha.items())}

        res = ""
        for words in temp:
            if len(words) == 2:
                rep = alpha[words[0]] + int(words[1])
                res += words[0] + rev_alpha[rep]
            else:
                res += words

        return res

def test_replace_digits():
    solution = Solution()

    # Test case 1
    s1 = "a1c1e1"
    print(solution.replaceDigits(s1))  # Expected output: "abcdef"

    # Test case 2
    s2 = "a1b2c3d4e"
    print(solution.replaceDigits(s2))  # Expected output: "abbdcdefe"

    # Test case 3
    s3 = "a0b0c0"
    print(solution.replaceDigits(s3))  # Expected output: "abc"

    # Test case 4
    s4 = "z9"
    print(solution.replaceDigits(s4))  # Expected output: "zj"

    # Test case 5
    s5 = "a1z9"
    print(solution.replaceDigits(s5))  # Expected output: "abzj"

test_replace_digits()