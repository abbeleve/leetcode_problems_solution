"""Realisation of min-heap just for training and fun"""
class Heap:
    def __init__(self):
        """Realisation of min-heap"""
        self.heap = []

    def heappush(self, element: int) -> None:
        """Insert element in heap"""
        if len(self.heap) == 0:
            self.heap.append(element)
            return 
        self.heap.append(element)
        self.sift_up()

    def sift_up(self) -> None:
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def sift_down(self) -> None:
        index = 0
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def swap(self, index_1, index_2) -> None:
        save = self.heap[index_1]
        self.heap[index_1] = self.heap[index_2]
        self.heap[index_2] = save

    def peek(self) -> int:
        return self.heap[0]
    
    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        self.swap(0, -1)
        result = self.heap.pop()
        self.sift_down()
        return result