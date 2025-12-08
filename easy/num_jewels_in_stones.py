class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in jewels)

def test_num_jewels_in_stones():
    solution = Solution()
    
    # Test case 1
    jewels = "aA"
    stones = "aAAbbbb"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 3
    
    # Test case 2
    jewels = "z"
    stones = "ZZ"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 0
    
    # Test case 3
    jewels = "abc"
    stones = "aabbcc"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 6
    
    # Test case 4
    jewels = ""
    stones = "aabbcc"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 0
    
    # Test case 5
    jewels = "xyz"
    stones = ""
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 0

    # Test case 6
    jewels = "A"
    stones = "aAaA"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 2

    # Test case 7
    jewels = "z"
    stones = "zzZZzZ"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 6

    # Test case 8
    jewels = "bdc"
    stones = "abcdeabcd"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 6

    # Test case 9
    jewels = "mnop"
    stones = "mnopqrstuv"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 4

    # Test case 10
    jewels = "Oo"
    stones = "oOooOOoO"
    print(solution.numJewelsInStones(jewels, stones)) # Expected: 8

test_num_jewels_in_stones()