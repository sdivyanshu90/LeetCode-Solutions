class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        count = bin(k - 1).count('1')
        return 0 if count % 2 == 0 else 1

def test_kth_grammar():
    solution = Solution()
    
    # Test case 1
    n = 1
    k = 1
    print(solution.kthGrammar(n, k)) # Expected: 0
    
    # Test case 2
    n = 2
    k = 1
    print(solution.kthGrammar(n, k)) # Expected: 0
    
    # Test case 3
    n = 2
    k = 2
    print(solution.kthGrammar(n, k)) # Expected: 1
    
    # Test case 4
    n = 3
    k = 3
    print(solution.kthGrammar(n, k)) # Expected: 1
    
    # Test case 5
    n = 4
    k = 5
    print(solution.kthGrammar(n, k)) # Expected: 1

    # Test case 6
    n = 5
    k = 10
    print(solution.kthGrammar(n, k)) # Expected: 0

    # Test case 7
    n = 10
    k = 512
    print(solution.kthGrammar(n, k)) # Expected: 1

    # Test case 8
    n = 15
    k = 16384
    print(solution.kthGrammar(n, k)) # Expected: 0

    # Test case 9
    n = 20
    k = 1048576
    print(solution.kthGrammar(n, k)) # Expected: 0

    # Test case 10
    n = 30
    k = 1073741824
    print(solution.kthGrammar(n, k)) # Expected: 0

test_kth_grammar()