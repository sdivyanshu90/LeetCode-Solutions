class MyHashSet:

    def __init__(self):
        self.bucket_size = 1000
        self.hash_set = [[] for _ in range(self.bucket_size)]

    def _hash_function(self, key):
        return key % self.bucket_size

    def add(self, key: int) -> None:
        hash_key = self._hash_function(key)
        if key not in self.hash_set[hash_key]:
            self.hash_set[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self._hash_function(key)
        if key in self.hash_set[hash_key]:
            self.hash_set[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self._hash_function(key)
        return key in self.hash_set[hash_key]

def test_my_hash_set():
    my_hash_set = MyHashSet()

    # Test Case 1: Add and Contains
    my_hash_set.add(1)
    my_hash_set.add(2)
    print(my_hash_set.contains(1))  # Expected: True
    print(my_hash_set.contains(3))  # Expected: False

    # Test Case 2: Add, Remove, and Contains
    my_hash_set.add(2)
    print(my_hash_set.contains(2))  # Expected: True
    my_hash_set.remove(2)
    print(my_hash_set.contains(2))  # Expected: False

    # Test Case 3: Edge Cases
    my_hash_set.add(1000000)
    print(my_hash_set.contains(1000000))  # Expected: True
    my_hash_set.remove(1000000)
    print(my_hash_set.contains(1000000))  # Expected: False

    # Test Case 4: Large Number of Operations
    for i in range(10000):
        my_hash_set.add(i)
    all_present = all(my_hash_set.contains(i) for i in range(10000))
    print(all_present)  # Expected: True

    # Test Case 5: Removing Non-Existent Key
    my_hash_set.remove(20000)  # Should not raise an error
    print(my_hash_set.contains(20000))  # Expected: False

test_my_hash_set()