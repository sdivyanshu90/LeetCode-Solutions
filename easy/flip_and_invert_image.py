from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr = [row[::-1] for row in image]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

        return arr

def test_flip_and_invert_image():
    solution = Solution()

    # Test Case 1
    image1 = [[1,1,0],[1,0,1],[0,0,0]]
    print(solution.flipAndInvertImage(image1)) # Expected: [[1,0,0],[0,1,0],[1,1,1]]

    # Test Case 2
    image2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(solution.flipAndInvertImage(image2)) # Expected: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

    # Test Case 3
    image3 = [[0]]
    print(solution.flipAndInvertImage(image3)) # Expected: [[1]]

    # Test Case 4
    image4 = [[1]]
    print(solution.flipAndInvertImage(image4)) # Expected: [[0]]

    # Test Case 5
    image5 = [[1,0],[0,1]]
    print(solution.flipAndInvertImage(image5)) # Expected: [[0,1],[1,0]]

test_flip_and_invert_image()