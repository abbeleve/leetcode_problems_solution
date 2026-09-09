class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        self.res = 0
        self.memo = {}
        self.recurse()

    def recurse(self,):
        