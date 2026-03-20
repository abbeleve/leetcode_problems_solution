class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        for letter in s:
            if letter not in hash_map:
                hash_map[letter] = 1
            else:
                hash_map[letter] += 1
        sorted_chars = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for letter, freq in sorted_chars:
            result += letter * freq
        return result
    
s = Solution()
print(s.frequencySort("loveleetcode"))