class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        result = ''
        for index, number in enumerate(str(num)):
            power = len(str(num)) - index - 1
            if number == '5' or number == '1':
                result += hash_map[(10**power) * int(number)]
            elif number == '4' or number == '9':
                result += hash_map[(10**power)] + hash_map[(10**power) * (int(number) + 1)]
            else:
                if int(number) > 5:
                    result += hash_map[(10**power) * 5] + hash_map[(10**power)] * (int(number) - 5)
                else:
                    result += hash_map[(10**power)] * int(number)
        return result
    
s = Solution()
print(s.intToRoman(3749))