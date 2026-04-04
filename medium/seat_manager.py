class SeatManager:

    def __init__(self, n: int):
        self.q = []
        self.index = 0
        self.n = n

    def reserve(self) -> int:
        if self.q:
            return heapq.heappop(self.q)
        else:
            self.index += 1
            return self.index

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.q, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

def test_seat_manager():
    # Test case 1
    seat_manager1 = SeatManager(5)
    print(seat_manager1.reserve())  # Expected output: 1
    print(seat_manager1.reserve())  # Expected output: 2
    seat_manager1.unreserve(1)
    print(seat_manager1.reserve())  # Expected output: 1
    print(seat_manager1.reserve())  # Expected output: 3

    # Test case 2
    seat_manager2 = SeatManager(3)
    print(seat_manager2.reserve())  # Expected output: 1
    print(seat_manager2.reserve())  # Expected output: 2
    print(seat_manager2.reserve())  # Expected output: 3
    seat_manager2.unreserve(2)
    print(seat_manager2.reserve())  # Expected output: 2

    # Test case 3
    seat_manager3 = SeatManager(4)
    print(seat_manager3.reserve())  # Expected output: 1
    print(seat_manager3.reserve())  # Expected output: 2
    seat_manager3.unreserve(1)
    seat_manager3.unreserve(2)
    print(seat_manager3.reserve())  # Expected output: 1
    print(seat_manager3.reserve())  # Expected output: 2
    print(seat_manager3.reserve())  # Expected output: 3
    print(seat_manager3.reserve())  # Expected output: 4

    # Test case 4
    seat_manager4 = SeatManager(2)
    print(seat_manager4.reserve())  # Expected output: 1
    print(seat_manager4.reserve())  # Expected output: 2
    seat_manager4.unreserve(1)
    print(seat_manager4.reserve())  # Expected output: 1
    print(seat_manager4.reserve())  # Expected output: 2

    # Test case 5
    seat_manager5 = SeatManager(6)
    print(seat_manager5.reserve())  # Expected output: 1
    print(seat_manager5.reserve())  # Expected output: 2
    print(seat_manager5.reserve())  # Expected output: 3
    seat_manager5.unreserve(2)
    print(seat_manager5.reserve())  # Expected output: 2
    print(seat_manager5.reserve())  # Expected output: 4
    print(seat_manager5.reserve())  # Expected output: 5
    print(seat_manager5.reserve())  # Expected output: 6

test_seat_manager()