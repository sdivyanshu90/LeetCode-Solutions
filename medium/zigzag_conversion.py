# Approach 1: Brute Force Grid Simulation
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s
        
#         grid = [[""] * len(s) for _ in range(numRows)]
#         row, col = 0, 0
#         down = True

#         for ch in s:
#             grid[row][col] = ch
#             if down:
#                 if row == numRows - 1:
#                     down = False
#                     row -= 1
#                     col += 1
#                 else:
#                     row += 1
#             else:
#                 if row == 0:
#                     down = True
#                     row += 1
#                 else:
#                     row -= 1
#                     col += 1

#         result = []
#         for r in range(numRows):
#             for c in range(len(s)):
#                 if grid[r][c] != "":
#                     result.append(grid[r][c])
#         return "".join(result)

# Approach 2: Row Builders (Efficient Simulation)
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s
        
#         rows = ["" for _ in range(numRows)]
#         curr, step = 0, 1
        
#         for ch in s:
#             rows[curr] += ch
#             if curr == 0:
#                 step = 1
#             elif curr == numRows - 1:
#                 step = -1
#             curr += step
        
#         return "".join(rows)

# Approach 3: Direct Index Calculation
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycle = 2 * numRows - 2
        result = []

        for r in range(numRows):
            for i in range(r, len(s), cycle):
                result.append(s[i])
                if 0 < r < numRows - 1 and i + cycle - 2*r < len(s):
                    result.append(s[i + cycle - 2*r])
        
        return "".join(result)

def test_zigzag_conversion():
    solution = Solution()

    # Test Case 1: Normal case
    s = "PAYPALISHIRING"
    numRows = 3
    print(solution.convert(s, numRows))  # Expected: "PAHNAPLSIIGYIR"

    # Test Case 2: Single row
    s = "ABCD"
    numRows = 1
    print(solution.convert(s, numRows))  # Expected: "ABCD"

    # Test Case 3: More rows than characters
    s = "ABC"
    numRows = 5
    print(solution.convert(s, numRows))  # Expected: "ABC"

    # Test Case 4: Even number of rows
    s = "ABCDEFGHIJKLMN"
    numRows = 4
    print(solution.convert(s, numRows))  # Expected: "AGMBFHLNCEIKDJ"

    # Test Case 5: Empty string
    s = ""
    numRows = 3
    print(solution.convert(s, numRows))  # Expected: "" 

    # Test Case 6: Two rows
    s = "EVERYONEISREJECTINGME"
    numRows = 2
    print(solution.convert(s, numRows))  # Expected: "EEYNIRJCIGEVROESEETNM"

    # Test Case 7: Long string with many rows
    s = "THISISALONGSTRINGFORTESTINGZIGZAGCONVERSION"
    numRows = 10
    print(solution.convert(s, numRows))  # Expected: "TOVHFRNEIGTORSNECSIISGISRTAOATIZNLSNGOGGINZ"

    # Test Case 8: String with special characters
    s = "LeetCode"
    numRows = 3
    print(solution.convert(s, numRows))  # Expected: ""LCetoeed""
    
    # Test Case 9: Single character string
    s = "A"
    numRows = 1
    print(solution.convert(s, numRows))  # Expected: "A"

    # Test Case 10: Palindrome string
    s = "abba"
    numRows = 2
    print(solution.convert(s, numRows))  # Expected: "abba"