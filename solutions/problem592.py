class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("-", "+-")
        splitted_expression = expression.split("+")
        splitted_expression = [i for i in splitted_expression if len(i) > 0]
        while len(splitted_expression) > 1:
            first_numerator, first_denominator = self.get_numerator_and_denominator(splitted_expression[0])
            second_numerator, second_denominator = self.get_numerator_and_denominator(splitted_expression[1])
            lcs = self.LCS(first_denominator, second_denominator)
            mult_first_numerator, mult_second_numerator = lcs // int(first_denominator), lcs // int(second_denominator)
            first_numerator, second_numerator = int(first_numerator) * mult_first_numerator, int(second_numerator) * mult_second_numerator
            res_numerator = first_numerator + second_numerator
            if res_numerator == 0:
                res_denominator = 1
            else:
                res_denominator = lcs
            splitted_expression.pop(1)
            splitted_expression[0] = f"{int(res_numerator)}/{int(res_denominator)}"
        res = splitted_expression[0]
        num, den = self.get_numerator_and_denominator(res)
        gcd = self.GCD(abs(int(num)), den)
        num = int(num) // gcd
        den = int(den) // gcd
        return f"{int(num)}/{int(den)}"
            
    def get_numerator_and_denominator(self, exp):
        numerator = exp.split('/')[0]
        denominator = exp.split('/')[1]
        return numerator, denominator

    def GCD(self, a, b):
        a, b = int(a), int(b)
        while a > 0 and b > 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        return max(a, b)

    def LCS(self, a, b):
        a, b = int(a), int(b)
        return a * b / self.GCD(a, b)

s = Solution()
print(s.fractionAddition("1/3-1/2"))