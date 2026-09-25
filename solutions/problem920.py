import math

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        if goal <= n:
            return int(math.factorial(n) / math.factorial(n - goal))
        return int(math.factorial(n) * (goal - k))