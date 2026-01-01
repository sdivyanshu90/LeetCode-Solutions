class Solution:
    def dayOfYear(self, date: str) -> int:
        month_dates = [31,28,31,30,31,30,31,31,30,31,30,31]
        month_dates_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

        split_date = [int(i) for i in date.split("-")]
        tes = split_date[1] % 12
        if split_date[0] % 400 == 0 or (split_date[0] % 4 == 0 and split_date[0] % 100 != 0):
            return (sum(month_dates_leap[:tes - 1]) + split_date[2])
        else:
            return (sum(month_dates[:tes - 1]) + split_date[2])

def test_day_of_year():
    solution = Solution()

    # Test case 1
    date = "2019-01-09"
    print(solution.dayOfYear(date))  # Expected output: 9

    # Test case 2
    date = "2019-02-10"
    print(solution.dayOfYear(date))  # Expected output: 41

    # Test case 3
    date = "2003-03-01"
    print(solution.dayOfYear(date))  # Expected output: 60

    # Test case 4
    date = "2004-03-01"
    print(solution.dayOfYear(date))  # Expected output: 61

    # Test case 5
    date = "2020-12-31"
    print(solution.dayOfYear(date))  # Expected output: 366

test_day_of_year()