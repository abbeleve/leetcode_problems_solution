class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        self.res = []
        self.recurse(label, label.bit_length())
        self.res.reverse()
        return self.res

    def recurse(self, number: int, depth: int):
        if depth == 1:
            self.res.append(1)
            return
        if depth % 2 == 0:
            maximum = 2 ** depth - 1
            index = maximum - number
        else:
            minimum = 2 ** (depth - 1)
            index = number - minimum
        index_above = index // 2
        self.res.append(number)
        number_above = 2 ** (depth - 2) + index_above if depth % 2 == 0 else 2 ** (depth - 1) - 1 - index_above
        self.recurse(number_above, depth - 1)