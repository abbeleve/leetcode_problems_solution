class Solution:
    def maxProduct(self, words: list[str]) -> int:
        bin_words = []
        for word in words:
            bin_words.append(self.to_binary(word))

        max_length = 0 
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bin_words[i] & bin_words[j] == 0:
                    max_length = max(max_length, len(words[i]) * len(words[j]))
        return max_length

    def to_binary(self, word: str) -> int:
        binary_word = 0
        for letter in word:
            bit_position = ord(letter) - ord('a')
            binary_word |= (1 << bit_position)
        return binary_word

s = Solution()
print(s.maxProduct(words = ["abcw","baz","foo","bar","xtfn","abcdef"]))