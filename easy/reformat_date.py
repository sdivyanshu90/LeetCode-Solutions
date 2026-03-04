class Solution:
    def reformatDate(self, date: str) -> str:
        day = {
            "1st": "01", "2nd": "02", "3rd": "03", "4th": "04", "5th": "05", 
            "6th": "06", "7th": "07", "8th": "08", "9th": "09", "10th": "10", 
            "11th": "11", "12th": "12", "13th": "13", "14th": "14", "15th": "15", 
            "16th": "16", "17th": "17", "18th": "18", "19th": "19", "20th": "20", 
            "21st": "21", "22nd": "22", "23rd": "23", "24th": "24", "25th": "25", 
            "26th": "26", "27th": "27", "28th": "28", "29th": "29", "30th": "30", 
            "31st": "31"
        }

        month = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", 
            "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", 
            "Nov": "11", "Dec": "12"
        }

        split_date = date.split(" ")
        res = ""
        for i in split_date[::-1]:
            if i in day.keys():
                res += day[i] + "-"
            elif i in month.keys():
                res += month[i] + "-"
            else:
                res += i + "-"
        return res.rstrip("-")

def test_reformat_date():
    solution = Solution()

    # Test Case 1
    date1 = "20th Oct 2052"
    print(solution.reformatDate(date1))  # Expected output: "2052-10-20"

    # Test Case 2
    date2 = "6th Jun 1933"
    print(solution.reformatDate(date2))  # Expected output: "1933-06-06"

    # Test Case 3
    date3 = "26th May 1960"
    print(solution.reformatDate(date3))  # Expected output: "1960-05-26"

    # Test Case 4
    date4 = "1st Jan 2000"
    print(solution.reformatDate(date4))  # Expected output: "2000-01-01"

    # Test Case 5
    date5 = "31st Dec 1999"
    print(solution.reformatDate(date5))  # Expected output: "1999-12-31"

test_reformat_date()