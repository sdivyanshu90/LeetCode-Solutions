class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = [row[:] for row in rectangle]
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.rect[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

def test_subrectangle_queries():
    # Test case 1
    rectangle = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    obj = SubrectangleQueries(rectangle)
    obj.updateSubrectangle(0, 0, 3, 2, 5)
    print(obj.getValue(0, 2))  # Expected output: 5
    print(obj.getValue(3, 1))  # Expected output: 5

    # Test case 2
    rectangle = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    obj = SubrectangleQueries(rectangle)
    print(obj.getValue(0, 0))  # Expected output: 1
    obj.updateSubrectangle(0, 0, 1, 1, 100)
    print(obj.getValue(0, 0))  # Expected output: 100
    print(obj.getValue(1, 1))  # Expected output: 100
    print(obj.getValue(2, 2))  # Expected output: 3

    # Test case 3
    rectangle = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    obj = SubrectangleQueries(rectangle)
    print(obj.getValue(0, 2))  # Expected output: 1
    obj.updateSubrectangle(0, 0, 3, 2, 5)
    print(obj.getValue(0, 2))  # Expected output: 5
    print(obj.getValue(3, 1))  # Expected output: 5
    obj.updateSubrectangle(3, 0, 3, 2, 10)
    print(obj.getValue(3, 1))  # Expected output: 10

    # Test case 4
    rectangle = [[1]]
    obj = SubrectangleQueries(rectangle)
    print(obj.getValue(0, 0))  # Expected output: 1
    obj.updateSubrectangle(0, 0, 0, 0, 2)
    print(obj.getValue(0, 0))  # Expected output: 2

    # Test case 5
    rectangle = [[1, 2], [3, 4]]
    obj = SubrectangleQueries(rectangle)
    print(obj.getValue(0, 0))  # Expected output: 1
    print(obj.getValue(0, 1))  # Expected output: 2
    print(obj.getValue(1, 0))  # Expected output: 3
    print(obj.getValue(1, 1))  # Expected output: 4
    obj.updateSubrectangle(0, 0, 1, 1, 5)
    print(obj.getValue(0, 0))  # Expected output: 5
    print(obj.getValue(0, 1))  # Expected output: 5
    print(obj.getValue(1, 0))  # Expected output: 5
    print(obj.getValue(1, 1))  # Expected output: 5

test_subrectangle_queries()