class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first

        for i in range(len(encoded)):
            arr[i + 1] = encoded[i] ^ arr[i]

        return arr

def test_decode():
    s = Solution()

    # Test Case 1
    encoded1 = [1,2,3]
    first1 = 1
    print(s.decode(encoded1, first1)) # Expected Output: [1,0,2,1]

    # Test Case 2
    encoded2 = [6,2,7,3]
    first2 = 4
    print(s.decode(encoded2, first2)) # Expected Output: [4,2,0,7,4]

    # Test Case 3
    encoded3 = [5,9,10]
    first3 = 5
    print(s.decode(encoded3, first3)) # Expected Output: [5,0,9,3]

    # Test Case 4
    encoded4 = [0]
    first4 = 0
    print(s.decode(encoded4, first4)) # Expected Output: [0,0]

    # Test Case 5
    encoded5 = [255]
    first5 = 255
    print(s.decode(encoded5, first5)) # Expected Output: [255,0]

test_decode()