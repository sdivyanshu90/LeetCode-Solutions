class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for ip in address:
            if ip == ".":
                res += "[.]"
            else:
                res += ip
        return res

def test_defang_ip_addr():
    solution = Solution()

    # Test case 1
    address = "1.1.1.1"
    print(solution.defangIPaddr(address))  # Expected output: "1[.]1[.]1[.]1"

    # Test case 2
    address = "255.100.50.0"
    print(solution.defangIPaddr(address))  # Expected output: "255[.]100[.]50[.]0"

    # Test case 3
    address = "192.168.0.1"
    print(solution.defangIPaddr(address))  # Expected output: "192[.]168[.]0[.]1"

    # Test case 4
    address = "10.0.0.1"
    print(solution.defangIPaddr(address))  # Expected output: "10[.]0[.]0[.]1"

    # Test case 5
    address = "172.16.254.1"
    print(solution.defangIPaddr(address))  # Expected output: "172[.]16[.]254[.]1"

test_defang_ip_addr()