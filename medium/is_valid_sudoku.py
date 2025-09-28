from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True

def test_is_valid_sudoku():
    solution = Solution()

    # Test case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result1 = solution.isValidSudoku(board1)
    print(result1)  # Expected output: True

    # Test case 2: Invalid Sudoku (duplicate in row)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9","+","+","+"] ,
        [".","+","+","+","+","+","+","+","+"] 
    ]
    result2 = solution.isValidSudoku(board2)
    print(result2)  # Expected output: False

    # Test case 3: Invalid Sudoku (duplicate in column)
    board3 = [
        ["5","3","+","+","+","+","+","+","+"] ,
        ["6","+","+","+","+","+","+","+","+"] ,
        ["+","+","+","+","+","+","+","+","+"] ,
        ["8","+","+","+","+","+","+","+","+"] ,
        ["4","+","+","+","+","+","+","+","+"] ,
        ["7","+","+","+","+","+","+","+","+"] ,
        ["+","+6+","++","++","++","++","++"] ,
        ["+","++","++","++","++","++","++"] ,
        ["+","++","++","++","++","++","++"] 
    ]
    result3 = solution.isValidSudoku(board3)
    print(result3)  # Expected output: False

    # Test case 4: Invalid Sudoku (duplicate in box)
    board4 = [
        ["5","3","+","+","+","+","+","+","+"] ,
        ["6","+","+","+","+","+","+","+","+"] ,
        ["+","+","+","+","+","+","+","+","+"] ,
        ["8","+","+","+","+","+","+","+","+"] ,
        ["4","+","+","+","+","+","+","+","+"] ,
        ["7","+","+","+","+","+","+","+","+"] ,
        ["+","+6+","++","++","++","++","++"] ,
        ["+","++","++","++","++","++","++"] ,
        ["+","++","++","++","++","++","++"] 
    ]
    result4 = solution.isValidSudoku(board4)
    print(result4)  # Expected output: False 

    # Test case 5: Empty board
    board5 = [
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]
    result5 = solution.isValidSudoku(board5)
    print(result5)  # Expected output: True

test_is_valid_sudoku()