class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.capacity:
            evicted_key = self.queue.pop(0)
            del self.cache[evicted_key]

        self.cache[key] = value
        self.queue.append(key)        


def test_lru_cache():
    lru = LRUCache(2)
    lru.put(1, 1)          # cache is {1=1}
    lru.put(2, 2)          # cache is {1=1, 2=2}
    print(lru.get(1))      # return 1

    lru.put(3, 3)          # evicts key 2, cache is {1=1, 3=3}
    print(lru.get(2))      # returns -1 (not found)

    lru.put(4, 4)          # evicts key 1, cache is {4=4, 3=3}
    print(lru.get(1))      # return -1 (not found)

    print(lru.get(3))      # return 3
    
    print(lru.get(4))      # return 4

test_lru_cache()