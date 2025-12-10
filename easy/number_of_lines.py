from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        tot = 0

        for char in s:
            count = widths[ord(char) - ord('a')]
            if count + tot > 100:
                line += 1
                tot = count
            else:
                tot += count
        return [line, tot]

def test_number_of_lines():
    solution = Solution()

    # Test Case 1
    widths1 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s1 = "abcdefghijklmnopqrstuvwxyz"
    print(solution.numberOfLines(widths1, s1)) # Expected: [3, 60]


    # Test Case 2
    widths2 = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s2 = "bbbcccdddaaa"
    print(solution.numberOfLines(widths2, s2)) # Expected: [2, 4]

    # Test Case 3
    widths3 = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    s3 = "abcdefghijklmnopqrstuvwxyz"
    print(solution.numberOfLines(widths3, s3)) # Expected: [2, 60]

    # Test Case 4
    widths4 = [8,7,6,5,4,3,2,1,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    s4 = "thequickbrownfoxjumpsoverthelazydog"
    print(solution.numberOfLines(widths4, s4)) # Expected: [5, 16]

    # Test Case 5
    widths5 = [1]*26
    s5 = "aaaaaaaaaa"
    print(solution.numberOfLines(widths5, s5)) # Expected: [1, 10]

test_number_of_lines()