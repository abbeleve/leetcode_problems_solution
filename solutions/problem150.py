class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        token_index = 0
        operators = ('+', '-', '*', '/')
        while token_index < len(tokens):
            token = tokens[token_index]
            if token in operators:
                number1, number2 = int(tokens[token_index - 2]), int(tokens[token_index - 1])
                if token == "+":
                    number = number1 + number2
                elif token == "-":
                    number = number1 - number2
                elif token == "*":
                    number = number1 * number2
                else:
                    number = number1 / number2
                tokens.pop(token_index - 1)
                token_index -= 1
                tokens.pop(token_index)
                token_index -= 1
                tokens[token_index] = number
            else:                
                token_index += 1
        return int(tokens[0])
    
s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))