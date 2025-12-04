from sortedcontainers import SortedList
import bisect

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True

def test_my_calendar():
    my_calendar = MyCalendar()

    # Test Case 1: Basic Booking
    print(my_calendar.book(10, 20))  # Expected: True
    print(my_calendar.book(15, 25))  # Expected: False
    print(my_calendar.book(20, 30))  # Expected: True

    # Test Case 2: Edge Overlap
    print(my_calendar.book(5, 10))   # Expected: True
    print(my_calendar.book(30, 40))  # Expected: True
    print(my_calendar.book(25, 35))  # Expected: False

    # Test Case 3: No Overlap
    print(my_calendar.book(0, 5))    # Expected: True
    print(my_calendar.book(40, 50))  # Expected: True

    # Test Case 4: Large Intervals
    print(my_calendar.book(1000000, 2000000))  # Expected: True
    print(my_calendar.book(1500000, 2500000))  # Expected: False

    # Test Case 5: Back-to-Back Bookings
    print(my_calendar.book(50, 60))   # Expected: True
    print(my_calendar.book(60, 70))   # Expected: True
    print(my_calendar.book(70, 80))   # Expected: True

test_my_calendar()