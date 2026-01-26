class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.word_hash_map = {}
        self.minimal_word_length = 10**4
        self.maximal_word_length = 0
        for word in wordDict:
            self.word_hash_map[word] = True
            self.minimal_word_length = min(self.minimal_word_length, len(word))
            self.maximal_word_length = max(self.maximal_word_length, len(word))
        self.segments = []
        self.s = s
    
    def backtracking(self, index, word_length):
        if self.s[index - word_length + 1:index + 1] in self.word_hash_map:
            self.segments.append(self.s[index - word_length + 1:index + 1])
            word_length = self.minimal_word_length
            index -= word_length

        for word_length_ in range(word_length, self.maximal_word_length):
            self.backtracking(index, word_length)