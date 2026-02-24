class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            self.prefix_product = [1]
            self.size = 0
        else:
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (
            self.prefix_product[self.size] // self.prefix_product[self.size - k]
        )

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

def test_ProductOfNumbers():
    obj = ProductOfNumbers()

    # Test case 1
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2)) # Expected output: 20
    print(obj.getProduct(3)) # Expected output: 40
    print(obj.getProduct(4)) # Expected output: 0

    # Test case 2
    obj2 = ProductOfNumbers()
    obj2.add(1)
    obj2.add(2)
    obj2.add(3)
    print(obj2.getProduct(2)) # Expected output: 6
    print(obj2.getProduct(3)) # Expected output: 6
    print(obj2.getProduct(4)) # Expected output: 0

    # Test case 3
    obj3 = ProductOfNumbers()
    obj3.add(0)
    print(obj3.getProduct(1)) # Expected output: 0
    print(obj3.getProduct(2)) # Expected output: 0

    # Test case 4
    obj4 = ProductOfNumbers()
    obj4.add(1)
    print(obj4.getProduct(1)) # Expected output: 1
    print(obj4.getProduct(2)) # Expected output: 0

    # Test case 5
    obj5 = ProductOfNumbers()
    obj5.add(2)
    obj5.add(3)
    obj5.add(4)
    print(obj5.getProduct(2)) # Expected output: 12
    print(obj5.getProduct(3)) # Expected output: 24
    print(obj5.getProduct(4)) # Expected output: 0

test_ProductOfNumbers()