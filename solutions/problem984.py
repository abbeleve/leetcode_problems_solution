class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        swap = False
        if b > a:
            a, b = b, a
            swap = True
        res = ""
        while a > 0 or b > 0:
            diff = a - b
            if diff > 0:
                if a >= 2 and b >= 1:
                    res += "aab"
                    a -= 2
                    b -= 1
                else:
                    if a >= 1:
                        res += "a"
                        a -= 1
                    if b >= 1:
                        res += "b"
                        b -= 1
            elif diff < 0:
                if b >= 2 and a >= 1:
                    res += "bba"
                    b -= 2
                    a -= 1
                else:
                    if b >= 1:
                        res += "b"
                        b -= 1
                    if a >= 1:
                        res += "a"
                        a -= 1
            else:
                if a >= 1:
                    res += "a"
                    a -= 1
                if b >= 1:
                    res += "b"
                    b -= 1
        if swap:
            res = "".join(["a" if letter == "b" else "b" for letter in res])
        return res

s = Solution()
print(s.strWithout3a3b(100, 99))