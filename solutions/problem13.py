class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_mapper = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        index = 0
        cum_sum = 0
        while index < len(s):
            if index + 1 < len(s):
                slice = s[index:index+2]
                if roman_to_int_mapper[slice[0]] < roman_to_int_mapper[slice[1]]:
                    cum_sum += roman_to_int_mapper["".join(slice)]
                    index += 1
                else:
                    cum_sum += roman_to_int_mapper[s[index]]
            else:
                cum_sum += roman_to_int_mapper[s[index]]
            index += 1
        return cum_sum

s = Solution()
print(s.romanToInt("MCMXCIV"))