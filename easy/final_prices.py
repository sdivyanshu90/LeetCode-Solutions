class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices[:]
        
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break

        return result

def test_final_prices():
    solution = Solution()

    # Test case 1
    prices = [8, 4, 6, 2, 3]
    print(solution.finalPrices(prices))  # Expected output: [4, 2, 4, 2, 3]

    # Test case 2
    prices = [1, 2, 3, 4, 5]
    print(solution.finalPrices(prices))  # Expected output: [1, 2, 3, 4, 5]

    # Test case 3
    prices = [10, 1, 1, 6]
    print(solution.finalPrices(prices))  # Expected output: [9, 0, 0, 6]

    # Test case 4
    prices = [5]
    print(solution.finalPrices(prices))  # Expected output: [5]

    # Test case 5
    prices = [7, 7, 7]
    print(solution.finalPrices(prices))  # Expected output: [0, 0, 7]

test_final_prices()