class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash_map = {}
        for index, letter in enumerate(s):
            if letter not in hash_map:
                hash_map[letter] = [index]
            else:
                hash_map[letter].append(index)
        keys = sorted(list(hash_map.keys()))
        last_index = hash_map[keys[0]][0]
        res = keys[0]
        for i in range(1, len(keys)):
            last_letter = res[-1]
            key = keys[i]
            new_last_index = None
            for letter_position in reversed(hash_map[key]):
                if letter_position > last_index:
                    new_last_index = letter_position
                else:
                    if new_last_index is None:
                        new_last_index = letter_position
                    break
            if new_last_index > last_index:
                last_index = new_last_index
                
            
    
s = Solution()
print(s.removeDuplicateLetters("bcabc"))