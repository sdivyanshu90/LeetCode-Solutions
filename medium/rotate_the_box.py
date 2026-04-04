class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])
        res = [["."] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            i = COLS - 1
            for c in range(COLS - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    res[i][ROWS - r - 1] = "#"
                    i -= 1

                elif boxGrid[r][c] == "*":
                    res[c][ROWS - r - 1] = "*"
                    i = c - 1

        return res

def test_rotate_the_box():
    solution = Solution()

    # Test case 1
    boxGrid1 = [["#",".","#"]]
    print(solution.rotateTheBox(boxGrid1))  # Expected output: [["."],["#"],["#"]]

    # Test case 2
    boxGrid2 = [["#",".","*"],["#","#","*"]]
    print(solution.rotateTheBox(boxGrid2))  # Expected output: [["."],["#"],["#"],["*"],["*"]]

    # Test case 3
    boxGrid3 = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
    print(solution.rotateTheBox(boxGrid3))  # Expected output: [["."],["#"],["#"],["#"],["*"],["."]]

    # Test case 4
    boxGrid4 = [["*",".","*"],["#","#","*"]]
    print(solution.rotateTheBox(boxGrid4))  # Expected output: [["."],["#"],["*"],["*"]]

    # Test case 5
    boxGrid5 = [["#","#","#"],["#","#","#"]]
    print(solution.rotateTheBox(boxGrid5))  # Expected output: [["."],["."],["."],["#"],["#"],["#"]]

test_rotate_the_box()