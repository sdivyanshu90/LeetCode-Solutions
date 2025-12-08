class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        result = [0.0] * 101
        result[0] = poured
        
        for i in range(query_row):
            next_row = [0.0] * 101
            for j in range(i + 1):
                overflow = (result[j] - 1) / 2.0
                if overflow > 0:
                    next_row[j] += overflow
                    next_row[j + 1] += overflow
            result = next_row        
        return min(1.0, result[query_glass])

def test_champagne_tower():
    solution = Solution()
    
    # Test case 1
    poured = 1
    query_row = 1
    query_glass = 1
    print(solution.champagneTower(poured, query_row, query_glass)) # Expected: 0.0
    
    # Test case 2
    poured = 2
    query_row = 1
    query_glass = 1
    print(solution.champagneTower(poured, query_row, query_glass)) # Expected: 0.5
    
    # Test case 3
    poured = 100000009
    query_row = 33
    query_glass = 17
    print(solution.champagneTower(poured, query_row, query_glass)) # Expected: 1.0

    # Test case 4
    poured = 25
    query_row = 6
    query_glass = 1
    print(solution.champagneTower(poured, query_row, query_glass)) # Expected: 0.1875

    # Test case 5
    poured = 4
    query_row = 2
    query_glass = 0
    print(solution.champagneTower(poured, query_row, query_glass)) # Expected: 0.25

test_champagne_tower()