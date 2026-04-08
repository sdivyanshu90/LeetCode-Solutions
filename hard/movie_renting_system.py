from collections import defaultdict
import bisect
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price_map = {}
        self.available = defaultdict(list)
        self.rented = []
        
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            self._insert(self.available[movie], (price, shop))

    def _insert(self, arr, val):
        bisect.insort(arr, val)

    def _remove(self, arr, val):
        idx = bisect.bisect_left(arr, val)
        if idx < len(arr) and arr[idx] == val:
            arr.pop(idx)

    def search(self, movie: int) -> List[int]:
        return [s for _, s in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self._remove(self.available[movie], (price, shop))
        self._insert(self.rented, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self._remove(self.rented, (price, shop, movie))
        self._insert(self.available[movie], (price, shop))

    def report(self) -> List[List[int]]:
        return [[s, m] for (p, s, m) in self.rented[:5]]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

def test_movie_renting_system():
    n = 3
    entries = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
    obj = MovieRentingSystem(n, entries)

    # Test case 1
    print(obj.search(1))  # Expected output: [1, 0, 2]

    # Test case 2
    obj.rent(0, 1)
    print(obj.report())  # Expected output: [[0, 1]]

    # Test case 3
    obj.rent(1, 1)
    print(obj.report())  # Expected output: [[1, 1], [0, 1]]

    # Test case 4
    obj.drop(0, 1)
    print(obj.search(1))  # Expected output: [0, 2]

    # Test case 5
    print(obj.report())  # Expected output: [[1, 1]]

test_movie_renting_system()