class Solution:
    def longestWord(self, words: list[str]) -> str:
        dictionary = set(words)
        max_word = ""
        for word in words:
            possible = True
            for i in range(1, len(word)):
                if word[0:i] not in dictionary:
                    possible = False
            if possible:
                if len(word) > len(max_word):
                    max_word = word
                if len(word) == len(max_word):
                    if word < max_word:
                        max_word = word
        return max_word
        

s = Solution()
print(s.longestWord(words = ["a","banana","app","appl","ap","apply","apple"]))