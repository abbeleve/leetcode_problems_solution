class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        for letter in s:
            hash_map[letter] = hash_map.get(letter, 0) + 1
        keys = hash_map.keys()
        res = 0
        solo_letter = 0
        for letter in keys:
            if hash_map[letter] % 2 == 1:
                solo_letter = 1
            res += (hash_map[letter] // 2) * 2
        return res + solo_letter