class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy

def test_reaching_points():
    solution = Solution()
    
    # Test case 1
    sx, sy, tx, ty = 1, 1, 3, 5
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: True
    
    # Test case 2
    sx, sy, tx, ty = 1, 1, 2, 2
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: False
    
    # Test case 3
    sx, sy, tx, ty = 1, 2, 5, 7
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: True
    
    # Test case 4
    sx, sy, tx, ty = 2, 2, 12, 8
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: True

    # Test case 5
    sx, sy, tx, ty = 3, 3, 12, 9
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: False

    # Test case 6
    sx, sy, tx, ty = 1, 4, 5, 9
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: True

    # Test case 7
    sx, sy, tx, ty = 5, 7, 5, 7
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: True

    # Test case 8
    sx, sy, tx, ty = 10, 15, 25, 40
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: False

    # Test case 9
    sx, sy, tx, ty = 1, 1, 1000000000, 1
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: True

    # Test case 10
    sx, sy, tx, ty = 1, 1, 1000000000, 2
    print(solution.reachingPoints(sx, sy, tx, ty)) # Expected: False

test_reaching_points()