class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        valid = ['-', '0','1','2','3','4','5','6','7','8','9']
        for index, i in enumerate(s):
            if i not in valid:
                s = s[:index]
                break
        for index, i in enumerate(s):
            if i != '0':
                s = s[index:]
                break
        if s[0] == '-':
            multiplier = -1
            s = s[1:]
        else:
            multiplier = 1
        left_border = -2**31
        right_border = 2**31 - 1
        s = int(s) * multiplier
        if left_border <= s <= right_border:
            return s
        return 0