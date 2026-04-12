class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left_pointer, right_pointer = 0, 0
        min_window = s + "!"
        fully_inside = False
        if len(t) > len(s):
            return ""
        hash_map = {}
        for string in t:
            hash_map[string] = hash_map.get(string, 0) + 1
        have, need = 0, len(hash_map)
        while right_pointer < len(s):
            if s[right_pointer] in hash_map:
                hash_map[s[right_pointer]] -= 1
                if hash_map[s[right_pointer]] == 0:
                    have += 1
            right_pointer += 1
            while have == need:
                if right_pointer - left_pointer < len(min_window):
                    min_window = s[left_pointer:right_pointer]
                if s[left_pointer] in hash_map:
                    hash_map[s[left_pointer]] += 1
                    if hash_map[s[left_pointer]] > 0:
                        have -= 1
                left_pointer += 1
        return min_window if min_window != s + "!" else ""

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))