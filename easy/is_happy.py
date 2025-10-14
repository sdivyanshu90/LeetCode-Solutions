class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            total_sum = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total_sum += digit ** 2
            return total_sum
        
        while n != 1 and n != 4:
            n = get_next(n)
        
        return n == 1

def test_is_happy():
    s = Solution()

    # Test Case 1: A well-known happy number
    n = 19
    print(f"\nInput: {n}, Output: {s.isHappy(n)}") # Expected: True
    # Path: 19 -> 82 -> 68 -> 100 -> 1

    # Test Case 2: A known unhappy number
    n = 2
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: False
    # Path: 2 -> 4 (which is the cycle anchor for unhappy numbers)

    # Test Case 3: The base case for happy numbers
    n = 1
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: True

    # Test Case 4: The cycle anchor for unhappy numbers
    n = 4
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: False

    # Test Case 5: Another simple happy number
    n = 7
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: True
    # Path: 7 -> 49 -> 97 -> 130 -> 10 -> 1

    # Test Case 6: A happy number that immediately simplifies
    n = 100
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: True
    # Path: 100 -> 1

    # Test Case 7: A single-digit unhappy number
    n = 5
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: False
    # Path: 5 -> 25 -> 29 -> 85 -> 89 -> ... -> 4
    
    # Test Case 8: A large happy number
    n = 91
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: True
    # Path: 91 -> 82 -> 68 -> 100 -> 1

    # Test Case 9: A large unhappy number
    n = 116
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: False
    # Path: 116 -> 38 -> 73 -> 58 -> ... -> 4

    # Test Case 10: A number that requires several steps
    n = 139
    print(f"Input: {n}, Output: {s.isHappy(n)}") # Expected: True
    # Path: 139 -> 91 -> 82 -> 68 -> 100 -> 1

test_is_happy()