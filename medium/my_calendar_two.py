from sortedcontainers import SortedDict


class MyCalendarTwo:

    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped_booking = 0

        for count in self.booking_count.values():
            overlapped_booking += count
            if overlapped_booking > self.max_overlapped_booking:
                self.booking_count[start] -= 1
                self.booking_count[end] += 1

                if self.booking_count[start] == 0:
                    del self.booking_count[start]

                return False

        return True 


def test_my_calendar_two():
    my_calendar_two = MyCalendarTwo()

    # Test Case 1: Basic Booking
    print(my_calendar_two.book(10, 20))  # Expected: True
    print(my_calendar_two.book(15, 25))  # Expected: True
    print(my_calendar_two.book(20, 30))  # Expected: True

    # Test Case 2: Triple Booking
    print(my_calendar_two.book(17, 22))  # Expected: False
    print(my_calendar_two.book(5, 15))   # Expected: True
    print(my_calendar_two.book(25, 35))  # Expected: True

    # Test Case 3: Edge Overlap
    print(my_calendar_two.book(5, 10))   # Expected: True
    print(my_calendar_two.book(30, 40))  # Expected: True
    print(my_calendar_two.book(15, 20))  # Expected: True

    # Test Case 4: Large Intervals
    print(my_calendar_two.book(1000000, 2000000))  # Expected: True
    print(my_calendar_two.book(1500000, 2500000))  # Expected: True
    print(my_calendar_two.book(1800000, 2200000))  # Expected: False

    # Test Case 5: Back-to-Back Bookings
    print(my_calendar_two.book(50, 60))   # Expected: True
    print(my_calendar_two.book(60, 70))   # Expected: True
    print(my_calendar_two.book(70, 80))   # Expected: True

test_my_calendar_two()