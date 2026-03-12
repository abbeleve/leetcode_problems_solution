class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.s = s
        self.wordDict = wordDict
        self.memo = {}
        return self.backtrack("", 0, s, wordDict)
    
    def backtrack(self, word, word_length, word_to_build, word_dict):
        if word == word_to_build:
            return True
        
        if word_length in self.memo:
            return self.memo[word_length]

        for word_chunk in word_dict:
            if len(word_chunk) + word_length > len(word_to_build):
                continue
            if word_chunk == word_to_build[word_length:word_length+len(word_chunk)]:
                new_word_length = word_length + len(word_chunk)
                new_word = word + word_chunk
                if self.backtrack(new_word, new_word_length, word_to_build, word_dict):
                    self.memo[word_length] = True
                    return True
        self.memo[word_length] = False
        return False
    
s = Solution()
print(s.wordBreak(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))