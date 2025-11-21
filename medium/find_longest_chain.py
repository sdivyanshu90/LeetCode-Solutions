from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        end = float('-inf')
        
        longest_chain = 0
        for pair in pairs:
            if pair[0] > end:
                longest_chain += 1
                end = pair[1]
        
        return longest_chain

def test_find_longest_chain():
    s = Solution()

    # Test case 1
    pairs = [[1,2],[2,3],[3,4]]
    print(s.findLongestChain(pairs))  # Expected output: 2

    # Test case 2
    pairs = [[5,24],[15,25],[27,40],[50,60]]
    print(s.findLongestChain(pairs))  # Expected output: 3

    # Test case 3
    pairs = [[1,2],[7,8],[4,5]]
    print(s.findLongestChain(pairs))  # Expected output: 3

    # Test case 4
    pairs = [[-10,-8],[-5,-3],[0,2],[3,5],[6,8]]
    print(s.findLongestChain(pairs))  # Expected output: 5

    # Test case 5
    pairs = [[1,10],[2,3],[4,5],[6,7],[8,9]]
    print(s.findLongestChain(pairs))  # Expected output: 4

test_find_longest_chain()