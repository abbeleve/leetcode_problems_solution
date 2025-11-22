class Solution:
    def isValid(self, s: str) -> bool:
        #match = {'{':'}','(':')','[':']'}
        match = ['{}', '[]', '()']
        while True:
            new_s = s
            for i in match:
                s = s.replace(i, '')
            if new_s == s:
                break
                
        if s == '':
            return True
        return False

s = Solution()
print(s.isValid('([])'))