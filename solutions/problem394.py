class Solution:
    def decodeString(self, s: str) -> str:
        self.s = s
        self.result = ""
        repeat = s[0]

    def recurse(self, substring):
        

s = Solution()
print(s.decodeString(s = "3[a]2[bc]"))