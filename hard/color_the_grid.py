class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        valid = dict()

        for mask in range(3**m):
            color = list()
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)

        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] -= mod
            f = g

        return sum(f) % mod

def test_color_the_grid():
    solution = Solution()

    # Test case 1
    m1, n1 = 1, 1
    print(solution.colorTheGrid(m1, n1))  # Expected output: 3

    # Test case 2
    m2, n2 = 1, 2
    print(solution.colorTheGrid(m2, n2))  # Expected output: 6

    # Test case 3
    m3, n3 = 5, 5
    print(solution.colorTheGrid(m3, n3))  # Expected output: 580986

    # Test case 4
    m4, n4 = 3, 3
    print(solution.colorTheGrid(m4, n4))  # Expected output: 246

    # Test case 5
    m5, n5 = 2, 3
    print(solution.colorTheGrid(m5, n5))  # Expected output: 54

test_color_the_grid()