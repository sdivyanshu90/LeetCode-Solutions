class Solution:
    def rotateString(self, A, B):
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False

def test_rotate_string():
    solution = Solution()
    
    # Test case 1
    A = "abcde"
    B = "cdeab"
    print(solution.rotateString(A, B)) # Expected: True
    
    # Test case 2
    A = "abcde"
    B = "abced"
    print(solution.rotateString(A, B)) # Expected: False
    
    # Test case 3
    A = ""
    B = ""
    print(solution.rotateString(A, B)) # Expected: True
    
    # Test case 4
    A = "a"
    B = "a"
    print(solution.rotateString(A, B)) # Expected: True

    # Test case 5
    A = "aa"
    B = "aa"
    print(solution.rotateString(A, B)) # Expected: True

    # Test case 6
    A = "abc"
    B = "cab"
    print(solution.rotateString(A, B)) # Expected: True

    # Test case 7
    A = "abcd"
    B = "dabc"
    print(solution.rotateString(A, B)) # Expected: True

    # Test case 8
    A = "abcd"
    B = "bcda"
    print(solution.rotateString(A, B)) # Expected: True

    # Test case 9
    A = "abcd"
    B = "acbd"
    print(solution.rotateString(A, B)) # Expected: False

    # Test case 10
    A = "rotation"
    B = "tationro"
    print(solution.rotateString(A, B)) # Expected: True

test_rotate_string()