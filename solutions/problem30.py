class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        hash_map = {word:0 for word in words}
        multiplication_map = {word:words.count(word) for word in words}
        step = len(words[0])
        words_length = len(words)
        amount_of_substrings = 0
        result_list = []
        for left_index in range(0, len(s) - step * (words_length - 1), step):
            skip_index = False
            right_index = left_index + step * words_length
            sliding_window = s[left_index:right_index]
            for word_index in range(0, len(sliding_window), step):
                word = sliding_window[word_index:word_index+step]
                if word not in hash_map:
                    skip_index = True
                    break
                if hash_map[word] == amount_of_substrings*multiplication_map[word] + 1*multiplication_map[word]:
                    skip_index = True
                    break
                hash_map[word] += 1
            if skip_index:
                for word in words:
                    hash_map[word] = amount_of_substrings*multiplication_map[word]
                continue
            amount_of_substrings += 1
            result_list.append(left_index)
        return result_list

s = Solution()
print(s.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]))