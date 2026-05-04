class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answers.sort()
        amount_of_rabbits = 0
        prev = answers[0]
        possible_rabbits = prev
        amount_of_rabbits += possible_rabbits + 1
        for index in range(1, len(answers)):
            if answers[index] == prev:
                if possible_rabbits > 0:
                    possible_rabbits -= 1
                else:
                    possible_rabbits = answers[index]
                    amount_of_rabbits += possible_rabbits + 1
                    continue
            else:
                prev = answers[index]
                possible_rabbits = answers[index]
                amount_of_rabbits += prev + 1
                continue
        return amount_of_rabbits
    
s = Solution()
print(s.numRabbits([1,0,1,0,0]))