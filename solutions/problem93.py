class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        self.result = []
        self.s = s
        if len(s) < 4 or len(s) > 12:
            return self.result
        self.backtrack("", 0)
        return self.result
    
    def backtrack(self, ip_string, pos):
        if pos == len(self.s) and len(ip_string.split('.')) == 4:
            self.result.append(ip_string)
        if pos == len(self.s) and len(ip_string.split('.')) < 4:
            return False
        if len(ip_string.split('.')) == 4:
            return False

        for i in range(1, 4):
            if i + pos > len(self.s):
                return
            if i > 1 and self.s[pos] == '0':
                continue
            if int(self.s[pos:pos + i]) > 255:
                continue
            if len(ip_string) == 0:
                ip_string = self.s[pos:pos + i]
            else:
                ip_string += '.' + self.s[pos:pos + i]
            self.backtrack(ip_string, pos + i)
            if len(ip_string) == i:
                ip_string = ""
            else:
                ip_string = ip_string[0:len(ip_string) - i - 1]

s = Solution()
print(s.restoreIpAddresses("101023"))