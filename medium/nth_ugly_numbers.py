# Approach 1
# import set

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         ugly_numbers_set = {1}
#         min_heap = [1]
        
#         last_ugly = 1
#         seen = {1}

#         for _ in range(n):
#             last_ugly = heapq.heappop(min_heap)
            
#             for factor in [2, 3, 5]:
#                 new_ugly = last_ugly * factor
#                 if new_ugly not in seen:
#                     seen.add(new_ugly)
#                     heapq.heappush(min_heap, new_ugly)

#         return last_ugly

# Approach 2
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers_set = {1}
        current_ugly = 1
        for i in range(n):
            current_ugly = min(ugly_numbers_set)
            ugly_numbers_set.remove(current_ugly)
            ugly_numbers_set.add(current_ugly * 2)
            ugly_numbers_set.add(current_ugly * 3)
            ugly_numbers_set.add(current_ugly * 5)
        return current_ugly

def test_nth_ugly_number():
    s = Solution()

    # Test Case 1: The absolute base case
    n1 = 1
    print(f"\nInput: n = {n1}")
    print(s.nthUglyNumber(n1)) # Expected: 1

    # Test Case 2: A standard small case
    n2 = 10
    print(f"\nInput: n = {n2}")
    print(s.nthUglyNumber(n2)) # Expected: 12

    # Test Case 3: A number that is a power of a single prime factor (2^3)
    n3 = 7
    print(f"\nInput: n = {n3}")
    print(s.nthUglyNumber(n3)) # Expected: 8

    # Test Case 4: A number resulting from a mix of two prime factors (3*5)
    n4 = 11
    print(f"\nInput: n = {n4}")
    print(s.nthUglyNumber(n4)) # Expected: 15

    # Test Case 5: A number involving a repeated prime factor (2*2*5)
    n5 = 14
    print(f"\nInput: n = {n5}")
    print(s.nthUglyNumber(n5)) # Expected: 20

    # Test Case 6: A slightly larger number that is a power of 2 (2^6)
    n6 = 27
    print(f"\nInput: n = {n6}")
    print(s.nthUglyNumber(n6)) # Expected: 64

    # Test Case 7: A medium-range n
    n7 = 150
    print(f"\nInput: n = {n7}")
    print(s.nthUglyNumber(n7)) # Expected: 5832

    # Test Case 8: A number that can be formed in multiple ways
    n8 = 15
    print(f"\nInput: n = {n8}")
    print(s.nthUglyNumber(n8)) # Expected: 24
    
    # Test Case 9: A large n to test performance and integer size handling
    n9 = 1000
    print(f"\nInput: n = {n9}")
    print(s.nthUglyNumber(n9)) # Expected: 51200000

    # Test Case 10: The typical maximum constraint on coding platforms
    n10 = 1690
    print(f"\nInput: n = {n10}")
    print(s.nthUglyNumber(n10)) # Expected: 2123366400

test_nth_ugly_number()