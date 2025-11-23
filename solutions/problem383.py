class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1
        
        for letter in ransomNote:
            letters[letter] = letters.get(letter, 0) - 1
            if letters.get(letter, 0) < 0:
                return False
        
        return True

s = Solution()
print(s.canConstruct('asdf', 'asdf'))