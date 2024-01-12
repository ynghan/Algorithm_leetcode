class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        d1 = defaultdict(int)
        for key in nums:
            d1[key] += 1
        #정렬 : O(nlogn)
        frequencies = dict(sorted(d1.items(), key=lambda x: x[1], reverse=True))
        
        result = list(frequencies.keys())[:k]

        return result

    