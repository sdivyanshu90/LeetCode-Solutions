from typing import List

class Fancy:
    def __init__(self):
        self.items = []
        self.mult = 1
        self.add = 0
        self.mod_val = 10**9 + 7

    def append(self, val: int) -> None:
        inv_m = pow(self.mult, self.mod_val - 2, self.mod_val)
        
        real_val = val - self.add
        real_val = real_val % self.mod_val
        real_val = (real_val * inv_m) % self.mod_val
        
        self.items.append(real_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod_val

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.mod_val
        self.add = (self.add * m) % self.mod_val

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.items):
            return -1
        
        ans = self.items[idx]
        ans = (ans * self.mult) % self.mod_val
        ans = (ans + self.add) % self.mod_val
        
        return ans


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

def test_fancy():
    fancy = Fancy()

    # Test case 1
    fancy.append(2)  # fancy sequence: [2]
    fancy.addAll(3)  # fancy sequence: [5]
    fancy.append(7)  # fancy sequence: [5, 7]
    print(fancy.getIndex(0))  # Expected output: 5
    fancy.multAll(2)  # fancy sequence: [10, 14]
    print(fancy.getIndex(0))  # Expected output: 10
    print(fancy.getIndex(1))  # Expected output: 14
    fancy.addAll(3)  # fancy sequence: [13, 17]
    fancy.append(10)  # fancy sequence: [13, 17, 10]
    fancy.multAll(2)  # fancy sequence: [26, 34, 20]
    print(fancy.getIndex(0))  # Expected output: 26
    print(fancy.getIndex(1))  # Expected output: 34
    print(fancy.getIndex(2))  # Expected output: 20

    # Test case 2
    fancy = Fancy()
    fancy.append(0)  # fancy sequence: [0]
    fancy.addAll(1)  # fancy sequence: [1]
    fancy.multAll(2)  # fancy sequence: [2]
    print(fancy.getIndex(0))  # Expected output: 2
    fancy.addAll(3)  # fancy sequence: [5]
    fancy.append(4)  # fancy sequence: [5, 4]
    fancy.multAll(2)  # fancy sequence: [10, 8]
    print(fancy.getIndex(0))  # Expected output: 10

    # Test case 3
    fancy = Fancy()
    fancy.append(1)  # fancy sequence: [1]
    fancy.multAll(2)  # fancy sequence: [2]
    fancy.addAll(3)  # fancy sequence: [5]
    fancy.append(4)  # fancy sequence: [5, 4]
    fancy.multAll(2)  # fancy sequence: [10, 8]
    print(fancy.getIndex(0))  # Expected output: 10
    print(fancy.getIndex(1))  # Expected output: 8

    # Test case 4
    fancy = Fancy()
    fancy.append(2)  # fancy sequence: [2]
    fancy.addAll(3)  # fancy sequence: [5]
    fancy.append(7)  # fancy sequence: [5, 7]
    print(fancy.getIndex(0))  # Expected output: 5
    fancy.multAll(2)  # fancy sequence: [10, 14]
    print(fancy.getIndex(0))  # Expected output: 10
    print(fancy.getIndex(1))  # Expected output: 14
    fancy.addAll(3)  # fancy sequence: [13, 17]
    fancy.append(10)  # fancy sequence: [13, 17, 10]
    fancy.multAll(2)  # fancy sequence: [26, 34, 20]
    print(fancy.getIndex(0))  # Expected output: 26
    print(fancy.getIndex(1))  # Expected output: 34
    print(fancy.getIndex(2))  # Expected output: 20

    # Test case 5
    fancy = Fancy()
    fancy.append(0)  # fancy sequence: [0]
    fancy.addAll(1)  # fancy sequence: [1]
    fancy.multAll(2)  # fancy sequence: [2]
    print(fancy.getIndex(0))  # Expected output: 2
    fancy.addAll(3)  # fancy sequence: [5]
    fancy.append(4)  # fancy sequence: [5, 4]
    fancy.multAll(2)  # fancy sequence: [10, 8]
    print(fancy.getIndex(0))  # Expected output: 10
    print(fancy.getIndex(1))  # Expected output: 8

test_fancy()