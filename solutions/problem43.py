class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        result = "0"
        for power, digit2 in enumerate(num2[::-1]):
            partial = ""
            carry = 0
            d2 = int(digit2)
            
            for digit1 in num1[::-1]:
                d1 = int(digit1)
                prod = d1 * d2 + carry
                carry = prod // 10
                partial = str(prod % 10) + partial
            
            if carry > 0:
                partial = str(carry) + partial
            
            partial += '0' * power
            result = self.sum_two_strings(result, partial)
        
        return result

    def sum_two_strings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        num1, num2 = num1[::-1], num2[::-1]
        carry = 0
        res = []
        
        for i in range(len(num2)):
            s = int(num1[i]) + int(num2[i]) + carry
            carry = s // 10
            res.append(str(s % 10))
        
        for i in range(len(num2), len(num1)):
            s = int(num1[i]) + carry
            carry = s // 10
            res.append(str(s % 10))
        
        if carry:
            res.append(str(carry))
        
        return ''.join(reversed(res))
    
# This one is much faster xD
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    
s = Solution()
print(s.multiply('98', '9'))