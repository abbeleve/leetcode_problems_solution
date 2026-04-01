class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        hash_map = {}
        word = ""
        max_word = 0
        for day, response in enumerate(responses):
            response = list(set(response))
            for resp in response:
                hash_map[resp] = hash_map.get(resp, 0) + 1
                if hash_map[resp] > max_word:
                    max_word = hash_map[resp]
                    word = resp
                elif hash_map[resp] == max_word:
                    if resp < word:
                        word = resp
        return word
    
s = Solution()
print(s.findCommonResponse(responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]))