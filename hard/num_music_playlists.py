class Solution:
    MOD = 1_000_000_007

    def power(self, base: int, exponent: int) -> int:
        result = 1
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % self.MOD
            exponent >>= 1
            base = (base * base) % self.MOD
        return result

    def precalculate_factorials(self, n: int):
        self.factorial = [1] * (n + 1)
        self.inv_factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            self.factorial[i] = (self.factorial[i - 1] * i) % self.MOD
            self.inv_factorial[i] = self.power(self.factorial[i], self.MOD - 2)

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        self.precalculate_factorials(n)
        sign = 1
        answer = 0
        for i in range(n, k - 1, -1):
            temp = self.power(i - k, goal - k)
            temp = (temp * self.inv_factorial[n - i]) % self.MOD
            temp = (temp * self.inv_factorial[i - k]) % self.MOD
            answer = (answer + sign * temp + self.MOD) % self.MOD
            sign *= -1
        return (self.factorial[n] * answer) % self.MOD

def test_num_music_playlists():
    solution = Solution()

    # Test Case 1
    print(solution.numMusicPlaylists(3, 3, 1)) # Expected: 6

    # Test Case 2
    print(solution.numMusicPlaylists(2, 3, 0)) # Expected: 6

    # Test Case 3
    print(solution.numMusicPlaylists(2, 3, 1)) # Expected: 2

    # Test Case 4
    print(solution.numMusicPlaylists(4, 4, 2)) # Expected: 24

    # Test Case 5
    print(solution.numMusicPlaylists(5, 10, 3)) # Expected: 7560

test_num_music_playlists()