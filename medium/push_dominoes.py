class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N

        f = 0
        for i in range(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f

        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)

def test_pushDominoes():
    solution = Solution()
    
    # Test Case 1
    print(solution.pushDominoes("RR.L")) # Expected: "RR.L"

    # Test Case 2
    print(solution.pushDominoes(".L.R...LR..L..")) # Expected: "LL.RR.LLRRLL.."

    # Test Case 3
    print(solution.pushDominoes("...")) # Expected: "..."

    # Test Case 4
    print(solution.pushDominoes("R...L")) # Expected: "RR.LL"

    # Test Case 5
    print(solution.pushDominoes("L....R")) # Expected: "L....R"

test_pushDominoes()