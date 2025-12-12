class Solution:
    def transpose(self, matrix):
        res = []
        
        for col in range(len(matrix[0])):
            temp = []
            for row in range(len(matrix)):
                temp.append(matrix[row][col])
            res.append(temp)
        return res

def test_transpose():
    solution = Solution()
    
    # Test Case 1
    print(solution.transpose([[1,2,3],[4,5,6],[7,8,9]])) # Expected: [[1,4,7],[2,5,8],[3,6,9]]

    # Test Case 2
    print(solution.transpose([[1,2,3],[4,5,6]])) # Expected: [[1,4],[2,5],[3,6]]

    # Test Case 3
    print(solution.transpose([[1]])) # Expected: [[1]]

    # Test Case 4
    print(solution.transpose([[1,2],[3,4],[5,6]])) # Expected: [[1,3,5],[2,4,6]]

    # Test Case 5
    print(solution.transpose([[1,0,0],[0,1,0],[0,0,1]])) # Expected: [[1,0,0],[0,1,0],[0,0,1]]

test_transpose()