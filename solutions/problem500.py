class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            word = word.strip()
            for row in rows:
                that_row = True
                for letter in word:
                    letter = letter.lower()
                    if letter not in row:
                        that_row = False
                        break
                if that_row:
                    result.append(word)
                    break
        return result

s = Solution()
print(s.findWords(["Hello","Alaska","Dad","Peace"]))