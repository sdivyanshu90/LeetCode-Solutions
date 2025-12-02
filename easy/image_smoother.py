from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        res = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                
                _sum = img[r][c]
                counter = 1
                if r - 1 >= 0:
                    counter += 1
                    _sum += img[r-1][c]
                    if c - 1 >= 0:
                        counter += 1
                        _sum += img[r-1][c-1]
                    if c + 1 < COLS:
                        counter += 1
                        _sum += img[r-1][c+1]
                if r + 1 < ROWS:
                    counter += 1
                    _sum += img[r+1][c]
                    if c-1 >= 0:
                        counter += 1
                        _sum += img[r+1][c-1]
                    if c+1 < COLS:
                        counter += 1
                        _sum += img[r+1][c+1]
                if c + 1 < COLS:
                    counter += 1
                    _sum += img[r][c+1]
                if c - 1 >= 0:
                    counter += 1
                    _sum += img[r][c-1]
                
                res[r][c] = _sum // counter 

        return res

def test_image_smoother():
    solution = Solution()

    # Test Case 1
    img1 = [[1,1,1],[1,0,1],[1,1,1]]
    print(solution.imageSmoother(img1)) # Expected: [[0,0,0],[0,0,0],[0,0,0]]

    # Test Case 2
    img2 = [[100,200,100],[200,50,200],[100,200,100]]
    print(solution.imageSmoother(img2)) # Expected: [[137,141,137],[141,138,141],[137,141,137]]

    # Test Case 3
    img3 = [[1]]
    print(solution.imageSmoother(img3)) # Expected: [[1]]

    # Test Case 4
    img4 = [[0,0,0],[0,0,0],[0,0,0]]
    print(solution.imageSmoother(img4)) # Expected: [[0,0,0],[0,0,0],[0,0,0]]

    # Test Case 5
    img5 = [[255,255],[255,255]]
    print(solution.imageSmoother(img5)) # Expected: [[255,255],[255,255]]

test_image_smoother()