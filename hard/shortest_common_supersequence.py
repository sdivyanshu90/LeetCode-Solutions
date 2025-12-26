class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        prev_row = [str2[0:col] for col in range(str2_length + 1)]

        for row in range(1, str1_length + 1):
            curr_row = [str1[0:row]] + [None for _ in range(str2_length)]

            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    pick_s1 = prev_row[col]
                    pick_s2 = curr_row[col - 1]

                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )

            prev_row = curr_row

        return prev_row[str2_length]

def test_shortest_common_supersequence():
    solution = Solution()

    # Test case 1
    str1_1 = "abac"
    str2_1 = "cab"
    print(solution.shortestCommonSupersequence(str1_1, str2_1))  # Expected output: "cabac"

    # Test case 2
    str1_2 = "geek"
    str2_2 = "eke"
    print(solution.shortestCommonSupersequence(str1_2, str2_2))  # Expected output: "geeke"

    # Test case 3
    str1_3 = "abc"
    str2_3 = "def"
    print(solution.shortestCommonSupersequence(str1_3, str2_3))  # Expected output: "abcdef"

    # Test case 4
    str1_4 = "aaaa"
    str2_4 = "aa"
    print(solution.shortestCommonSupersequence(str1_4, str2_4))  # Expected output: "aaaa"

    # Test case 5
    str1_5 = "ab"
    str2_5 = "ab"
    print(solution.shortestCommonSupersequence(str1_5, str2_5))  # Expected output: "ab"

test_shortest_common_supersequence()