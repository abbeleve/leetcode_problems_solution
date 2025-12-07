class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupped_anagrames = dict()
        indexer = 0
        for i in range(len(strs) - 1):
            is_anagram = self.isAnagram(strs[i], strs[i + 1])
            if is_anagram:
                if groupped_anagrames.get(indexer) is None:
                    indexer += 1

    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        for elem in s:
            if s_map.get(elem) is None:
                s_map[elem] = 1
                continue
            s_map[elem] += 1
        
        for elem in t:
            if t_map.get(elem) is None:
                t_map[elem] = 1
                continue
            t_map[elem] += 1
        
        t_map_keys = list(t_map)
        s_map_keys = list(s_map)
        
        for key in s_map_keys:
            if s_map.get(key) != t_map.get(key):
                return False
            
        for key in t_map_keys:
            if s_map.get(key) != t_map.get(key):
                return False
            
        return True
