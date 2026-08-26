# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterated_list = []
        while iterator.hasNext():
            elem = iterator.next()
            self.iterated_list.append(elem)
        self.index = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            return self.iterated_list[self.index]
        raise StopIteration()

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            res = self.iterated_list[self.index]
            self.index += 1
            return res
        raise StopIteration()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index != len(self.iterated_list)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].