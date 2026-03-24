class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_hash_map = {}
        substring = s[0:minSize]
        hash_map = {}
        for letter in substring:
            hash_map[letter] = hash_map.get(letter, 0) + 1
        if len(list(hash_map.keys())) <= maxLetters:
            substring_hash_map[substring] = substring_hash_map.get(substring, 0) + 1
        for right_index in range(minSize, len(s)):
            deleting_letter = substring[0]
            if hash_map[deleting_letter] == 1:
                hash_map.pop(deleting_letter)
            else:
                hash_map[deleting_letter] -= 1
            new_letter = s[right_index]
            hash_map[new_letter] = hash_map.get(new_letter, 0) + 1
            substring = substring[1:] + new_letter
            if len(list(hash_map.keys())) <= maxLetters:
                substring_hash_map[substring] = substring_hash_map.get(substring, 0) + 1
        list_of_keys = list(substring_hash_map.keys())
        max_occurences = 0
        for substring in list_of_keys:
            if substring_hash_map[substring] > max_occurences:
                max_occurences = substring_hash_map[substring]
        return max_occurences

s = Solution()
print(s.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))