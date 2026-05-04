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
    
import math
class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        amount_of_rabbits = 0
        hash_map = {}
        for answer in answers:
            hash_map[answer] = hash_map.get(answer, 0) + 1
        keys = hash_map.keys()
        for key in keys:
            group_size = math.ceil(hash_map[key] / (key + 1))
            amount_of_rabbits += group_size * (key + 1)
        return amount_of_rabbits
    
s = Solution()
print(s.numRabbits([1,0,1,0,0]))