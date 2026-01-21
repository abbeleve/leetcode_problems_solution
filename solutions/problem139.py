class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_hash_map = {}
        minimal_word_length = 10**4
        maximal_word_length = 0
        for word in wordDict:
            word_hash_map[word] = True
            minimal_word_length = min(minimal_word_length, len(word))
            maximal_word_length = max(maximal_word_length, len(word))
        left_index = len(s) - 1
        right_index = len(s)
        while left_index >= 0:
            lookup_word = word[left_index:right_index]
            if lookup_word in word_hash_map:
                right_index = left_index
