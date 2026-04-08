class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        kmp_lps = self._compute_longest_prefix_suffix(part)
        char_stack = []
        pattern_indexes = [0] * (len(s) + 1)

        str_index = 0
        pattern_index = 0
        while str_index < len(s):
            current_char = s[str_index]
            char_stack.append(current_char)

            if current_char == part[pattern_index]:
                pattern_indexes[len(char_stack)] = pattern_index + 1
                pattern_index += 1

                if pattern_index == len(part):
                    for _ in range(len(part)):
                        char_stack.pop()

                    pattern_index = (
                        0
                        if not char_stack
                        else pattern_indexes[len(char_stack)]
                    )
            else:
                if pattern_index != 0:
                    str_index -= 1
                    pattern_index = kmp_lps[pattern_index - 1]
                    char_stack.pop()
                else:
                    pattern_indexes[len(char_stack)] = 0

            str_index += 1

        return "".join(char_stack)

    def _compute_longest_prefix_suffix(self, pattern: str) -> list:
        lps = [0] * len(pattern)

        current = 1
        prefix_length = 0
        while current < len(pattern):
            if pattern[current] == pattern[prefix_length]:
                prefix_length += 1
                lps[current] = prefix_length
                current += 1

            elif prefix_length != 0:
                prefix_length = lps[prefix_length - 1]

            else:
                lps[current] = 0
                current += 1

        return lps

def test_remove_occurrences():
    solution = Solution()

    # Test case 1
    s = "daabcbaabcbc"
    part = "abc"
    print(solution.removeOccurrences(s, part))  # Expected output: "dab"

    # Test case 2
    s = "axxxxyyyyb"
    part = "xy"
    print(solution.removeOccurrences(s, part))  # Expected output: "ab"

    # Test case 3
    s = "aababaab"
    part = "aab"
    print(solution.removeOccurrences(s, part))  # Expected output: "ab"

    # Test case 4
    s = "abcde"
    part = "f"
    print(solution.removeOccurrences(s, part))  # Expected output: "abcde"

    # Test case 5
    s = "aaaaa"
    part = "aa"
    print(solution.removeOccurrences(s, part))  # Expected output: "a"

test_remove_occurrences()