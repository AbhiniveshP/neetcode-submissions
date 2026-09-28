from heapq import heappush as insert
from heapq import heappop as remove

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.__heap = []
        self.__k = k
        for num in nums:
            insert(self.__heap, num)
            if (len(self.__heap) > k):
                remove(self.__heap)

    def add(self, val: int) -> int:
        insert(self.__heap, val)
        if (len(self.__heap) > self.__k):
            remove(self.__heap)
        return self.__heap[0]