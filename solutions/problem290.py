class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_of_words = s.split()
        map_word_to_letter = dict()
        map_letter_to_word = dict()
        if len(list_of_words) != len(pattern):
            return False
        
        for index, word in enumerate(list_of_words):
            letter = pattern[index]
            if map_word_to_letter.get(word) is None and map_letter_to_word.get(letter) is None:
                map_word_to_letter[word] = letter
                map_letter_to_word[letter] = word
                continue

            if map_word_to_letter.get(word) == letter:
                continue
            if map_letter_to_word.get(letter) == word:
                continue
            return False
        return True
    
s = Solution()
print(s.wordPattern('abba', "dog cat cat dog"))