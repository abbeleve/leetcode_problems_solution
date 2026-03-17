class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hash_map = {}
        bulls, cows = 0, 0
        index = 0
        while index < len(secret):
            if secret[index] == guess[index]:
                bulls += 1
                secret = secret[0:index] + secret[index + 1:]
                guess = guess[0:index] + guess[index + 1:]
            else:
                index += 1
        for index, letter in enumerate(secret):
            if letter not in hash_map:
                hash_map[letter] = [index]
            else:
                hash_map[letter].append(index)
        for index, letter in enumerate(guess):
            if letter in hash_map and len(hash_map[letter]) > 0:
                hash_map[letter].pop()
                cows += 1
        return f"{bulls}A{cows}B"

s = Solution()
print(s.getHint(secret = "1123", guess = "0111"))