class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for dict_word in dictionary:
            found_flag, index_dict_word, index_s = False, 0, 0
            while index_dict_word < len(dict_word) and index_s < len(s):
                if dict_word[index_dict_word] == s[index_s]:
                    index_dict_word += 1
                    index_s += 1
                    if index_dict_word == len(dict_word):
                        found_flag = True
                        break
                else:
                    index_s += 1
            if found_flag:
                return dict_word
                    
        return ""
    
s = Solution()
print(s.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))