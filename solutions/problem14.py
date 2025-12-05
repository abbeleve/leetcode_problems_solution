class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in strs:
            if len(i) == 0:
                return ""

        for prefix_length in range(1, 200):
            try:
                prefix = strs[0][0:prefix_length]
            except:
                return strs[0][0:prefix_length - 1]
            for string in strs:
                try:
                    if string[0:prefix_length] != prefix:
                        return strs[0][0:prefix_length - 1]
                except:
                    return strs[0][0:prefix_length - 1]
                
        return strs[0][0:prefix_length]

s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))