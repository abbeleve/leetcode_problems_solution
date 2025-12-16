class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        line_size = 0
        start_index = 0
        word_index = 0
        while word_index < len(words):
            if line_size + len(words[word_index]) <= maxWidth:
                line_size += len(words[word_index])
                word_index += 1
            else:
                gap_size = maxWidth - line_size
                word_amount = word_index - start_index
                for gap_counter in range(word_amount - 1):
                    