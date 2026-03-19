import heapq

class MedianFinder:

    def __init__(self):
        self.data = []
        self.length = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.data, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 1:
            return heapq.nlargest(self.length // 2 + 1, self.data)[-1]
        largest = heapq.nlargest(self.length // 2 + 1, self.data)
        return (largest[-1] + largest[-2]) / 2