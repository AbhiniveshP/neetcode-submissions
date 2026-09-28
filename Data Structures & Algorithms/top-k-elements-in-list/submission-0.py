from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap, topk_list = [], []
        frequency_map = defaultdict(int)

        for num in nums:
            frequency_map[num] += 1
        
        for num, count in frequency_map.items():
            heappush(heap, (count, num))
            if (len(heap) > k):
                heappop(heap)
        
        while (heap):
            topk_list.append(heappop(heap)[1])
        
        return topk_list