class Solution:
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

s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))