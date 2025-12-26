class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for char in tiles:
            char_count[ord(char) - ord("A")] += 1

        return self._find_sequences(char_count)

    def _find_sequences(self, char_count: list) -> int:
        total = 0

        for pos in range(26):
            if char_count[pos] == 0:
                continue
            total += 1
            char_count[pos] -= 1
            total += self._find_sequences(char_count)
            char_count[pos] += 1

        return total

def test_num_tile_possibilities():
    solution = Solution()

    # Test case 1
    tiles1 = "AAB"
    print(solution.numTilePossibilities(tiles1))  # Expected output: 8

    # Test case 2
    tiles2 = "AAABBC"
    print(solution.numTilePossibilities(tiles2))  # Expected output: 188

    # Test case 3
    tiles3 = "V"
    print(solution.numTilePossibilities(tiles3))  # Expected output: 1

    # Test case 4
    tiles4 = "ABCDEFG"
    print(solution.numTilePossibilities(tiles4))  # Expected output: 13699

    # Test case 5
    tiles5 = "CCCC"
    print(solution.numTilePossibilities(tiles5))  # Expected output: 4

test_num_tile_possibilities()