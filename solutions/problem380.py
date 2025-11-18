import random

class RandomizedSet:

    def __init__(self):
        
        self.hash_map = dict()
        self.list_of_keys = []

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.hash_map[val] = (True, len(self.list_of_keys))
            self.list_of_keys.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            index = self.hash_map.pop(val)[1]
            last_key = self.list_of_keys.pop()
            if last_key != val:
                self.list_of_keys[index] = last_key
                self.hash_map[self.list_of_keys[index]] = (True, index)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.list_of_keys[random.randint(0, len(self.list_of_keys) - 1)]
        
s = RandomizedSet()
print(s.insert(0))
print(s.insert(1))
print(s.remove(0))
print(s.insert(2))
print(s.remove(1))
print(s.getRandom())