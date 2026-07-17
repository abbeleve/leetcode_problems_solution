import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        heap = []
        hash_map = {}
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1
        for word, count in hash_map.items():
            heapq.heappush(heap, (-count, word))
        res = []
        for i in range(k):
            count, word = heapq.heappop(heap)
            res.append(word)
        return res