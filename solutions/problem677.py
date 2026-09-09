class MapSum:

    def __init__(self):
        self.hash_map = {}
        self.prefix_map = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.hash_map:
            for prefix_len in range(1, len(key) + 1):
                prefix = key[0:prefix_len]
                if prefix in self.prefix_map:
                    self.prefix_map[prefix].append(key)
                else:
                    self.prefix_map[prefix] = [key]
        self.hash_map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        if prefix in self.prefix_map:
            for keys in self.prefix_map[prefix]:
                res += self.hash_map[keys]
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)