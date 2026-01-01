from typing import List
from functools import cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def place(book_pos, cur_width, max_height):
            if book_pos == len(books):
                return 0
            width, height = books[book_pos]
            ans = height + place(book_pos + 1, width, height)
            if book_pos and cur_width + width <= shelfWidth:
                height_increase = max(0, height - max_height)
                ans = min(ans, height_increase + place(book_pos + 1, cur_width + width, max_height + height_increase))
            
            return ans
        
        return place(0, 0, 0)

def test_min_height_shelves():
    solution = Solution()

    # Test case 1
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    print(solution.minHeightShelves(books, shelfWidth))  # Expected output: 6

    # Test case 2
    books = [[7,3],[8,7],[2,7],[2,5]]
    shelfWidth = 10
    print(solution.minHeightShelves(books, shelfWidth))  # Expected output: 15

    # Test case 3
    books = [[1,3],[2,4],[3,2]]
    shelfWidth = 6
    print(solution.minHeightShelves(books, shelfWidth))  # Expected output: 4

    # Test case 4
    books = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    shelfWidth = 5
    print(solution.minHeightShelves(books, shelfWidth))  # Expected output: 13

    # Test case 5
    books = [[1,2],[2,3],[3,4],[4,5]]
    shelfWidth = 6
    print(solution.minHeightShelves(books, shelfWidth))  # Expected output: 9

test_min_height_shelves()