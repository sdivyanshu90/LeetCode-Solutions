class MyHashMap:

    def __init__(self):
        self.data = {}

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.data:
            del self.data[key]

def test_my_hash_map():
    my_hash_map = MyHashMap()

    # Test Case 1: Put and Get
    my_hash_map.put(1, 1)
    my_hash_map.put(2, 2)
    print(my_hash_map.get(1))  # Expected: 1
    print(my_hash_map.get(3))  # Expected: -1

    # Test Case 2: Update Value
    my_hash_map.put(2, 1)
    print(my_hash_map.get(2))  # Expected: 1

    # Test Case 3: Remove and Get
    my_hash_map.remove(2)
    print(my_hash_map.get(2))  # Expected: -1

    # Test Case 4: Edge Cases
    my_hash_map.put(0, 0)
    print(my_hash_map.get(0))  # Expected: 0
    my_hash_map.remove(0)
    print(my_hash_map.get(0))  # Expected: -1

    # Test Case 5: Large Number of Operations
    for i in range(10000):
        my_hash_map.put(i, i * 2)
    all_correct = all(my_hash_map.get(i) == i * 2 for i in range(10000))
    print(all_correct)  # Expected: True

test_my_hash_map()