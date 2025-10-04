class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

def test_exist():
    solution = Solution()

    # Test case 1
    board1 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word1 = "ABCCED"
    print(solution.exist(board1, word1))  # Expected output: True

    # Test case 2
    board2 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word2 = "SEE"
    print(solution.exist(board2, word2))  # Expected output: True

    # Test case 3
    board3 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word3 = "ABCB"
    print(solution.exist(board3, word3))  # Expected output: False

    # Test case 4
    board4 = [['A']]
    word4 = "A"
    print(solution.exist(board4, word4))  # Expected output: True

    # Test case 5
    board5 = [['A']]
    word5 = "B"
    print(solution.exist(board5, word5))  # Expected output: False

    # Test case 6
    board6 = [
        ['C','A','A'],
        ['A','A','A'],
        ['B','C','D']
    ]
    word6 = "AAB"
    print(solution.exist(board6, word6))  # Expected output: True

    # Test case 7
    board7 = [
        ['A','B'],
        ['C','D']
    ]
    word7 = "ACDB"
    print(solution.exist(board7, word7))  # Expected output: True

    # Test case 8
    board8 = [
        ['A','B','C'],
        ['D','E','F'],
        ['G','H','I']
    ]
    word8 = "ABCDEFGHI"
    print(solution.exist(board8, word8))  # Expected output: False

    # Test case 9
    board9 = [
        ['A','B','C'],
        ['D','E','F'],
        ['G','H','I']
    ]
    word9 = "AFC"
    print(solution.exist(board9, word9))  # Expected output: False

    # Test case 10
    board10 = [
        ['A','B','C','E'],
        ['S','F','E','S'],
        ['A','D','E','E']
    ]
    word10 = "ABCESEEEFS"
    print(solution.exist(board10, word10))  # Expected output: True

test_exist()