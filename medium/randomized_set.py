import random

class RandomizedSet:

    def __init__(self):
        self.valToIndex = dict()
        self.valList = list()

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False

        self.valToIndex[val] = len(self.valList)
        self.valList.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False

        lastVal = self.valList[-1]
        valIndex = self.valToIndex[val]
        if lastVal != val:
            self.valToIndex[lastVal] = valIndex
            self.valList[valIndex] = lastVal

        self.valList.pop()
        self.valToIndex.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice( self.valList )
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def test_randomized_set():
    randomizedSet = RandomizedSet()
    
    # Test case 1: Insert elements
    print(randomizedSet.insert(1)) # Expected output: True
    print(randomizedSet.insert(2)) # Expected output: True
    print(randomizedSet.insert(1)) # Expected output: False

    # Test case 2: Remove elements
    print(randomizedSet.remove(2)) # Expected output: True
    print(randomizedSet.remove(3)) # Expected output: False

    # Test case 3: Get random element
    print(randomizedSet.getRandom()) # Expected output: 1 (only element left)

    # Test case 4: Insert more elements
    print(randomizedSet.insert(3)) # Expected output: True
    print(randomizedSet.insert(4)) # Expected output: True

    # Test case 5: Get random element multiple times
    random_elements = [randomizedSet.getRandom() for _ in range(10)]
    print(random_elements) # Expected output: [4, 3, 1, 4, 3, 4, 4, 1, 4, 4]

    # Test case 6: Remove all elements
    print(randomizedSet.remove(1)) # Expected output: True
    print(randomizedSet.remove(3)) # Expected output: True
    print(randomizedSet.remove(4)) # Expected output: True
    print(randomizedSet.remove(4)) # Expected output: False

    # Test case 7: Get random from empty set (should handle gracefully)
    try:
        print(randomizedSet.getRandom()) # Expected output: Error or specific handling
    except IndexError:
        print("No elements to return.")

    # Test case 8: Insert after clearing
    print(randomizedSet.insert(5)) # Expected output: True
    print(randomizedSet.getRandom()) # Expected output: 5

    # Test case 9: Insert negative and zero values
    print(randomizedSet.insert(0)) # Expected output: True
    print(randomizedSet.insert(-1)) # Expected output: True
    print(randomizedSet.getRandom()) # Expected output: 0

    # Test case 10: Remove negative and zero values
    print(randomizedSet.remove(0)) # Expected output: True
    print(randomizedSet.remove(-1)) # Expected output: True
    print(randomizedSet.getRandom()) # Expected output: 5

test_randomized_set()