from heapq import heappush as insert
from heapq import heappop as remove

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if (stones is None or len(stones) == 0):
            return 0
        if (len(stones) == 1):
            return stones[0]
        
        heap = []
        for w in stones:
            insert(heap, -w)
        
        while (len(heap) > 1):
            w1 = remove(heap)
            w2 = remove(heap)
            net = abs(w1 - w2)
            if (net > 0):
                insert(heap, -net)
        
        return 0 if len(heap) == 0 else -heap[0]