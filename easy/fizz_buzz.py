from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if s == "":
                s += str(i)
            res.append(s)

        return res

def test_fizz_buzz():
    s = Solution()

    # Test case 1
    print(s.fizzBuzz(3))  # Expected output: ["1","2","Fizz"]

    # Test case 2
    print(s.fizzBuzz(5))  # Expected output: ["1","2","Fizz","4","Buzz"]

    # Test case 3
    print(s.fizzBuzz(15)) # Expected output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

    # Test case 4
    print(s.fizzBuzz(1))  # Expected output: ["1"]

    # Test case 5
    print(s.fizzBuzz(0))  # Expected output: []

test_fizz_buzz()