class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        return heapq.nlargest(k, freq.keys(), key=freq.get)