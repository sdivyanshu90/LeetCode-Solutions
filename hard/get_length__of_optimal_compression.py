class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n=len(s)
        cache={}
        def rec(start,k):
            if (start,k) in cache:
                return cache[(start,k)]
            if start==n or k>=n-start:
                return 0
            count=defaultdict(int)
            mostFreq=0
            ans=float('inf')
            for j in range(start,n):
                c=s[j]
                count[c]+=1
                mostFreq=max(mostFreq,count[c])
                compressedLen=1+(len(str(mostFreq)) if mostFreq>1 else 0)
                remaining=j-start+1-mostFreq
                if k>=remaining:
                    ans=min(ans,compressedLen+rec(j+1,k-remaining))
            cache[(start,k)]=ans
            return ans
        return rec(0,k)

def test_get_length_of_optimal_compression():
    solution = Solution()

    # Test case 1
    s1 = "aaabcccd"
    k1 = 2
    print(solution.getLengthOfOptimalCompression(s1, k1))  # Expected output: 4

    # Test case 2
    s2 = "aabbaa"
    k2 = 2
    print(solution.getLengthOfOptimalCompression(s2, k2))  # Expected output: 2

    # Test case 3
    s3 = "aaaaaaaaaaa"
    k3 = 0
    print(solution.getLengthOfOptimalCompression(s3, k3))  # Expected output: 4

    # Test case 4
    s4 = "abcde"
    k4 = 1
    print(solution.getLengthOfOptimalCompression(s4, k4))  # Expected output: 4

    # Test case 5
    s5 = "aabbcc"
    k5 = 3
    print(solution.getLengthOfOptimalCompression(s5, k5))  # Expected output: 3

test_get_length_of_optimal_compression()