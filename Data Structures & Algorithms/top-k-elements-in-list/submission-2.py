class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []

        for num in nums:
            d[num] = d.get(num, 0) + 1
                
        freq = [[] for i in range(len(nums) + 1)]

        for key, value in d.items():
            freq[value].append(key)

        for num in range(len(freq) - 1, 0, -1):
            for i in freq[num]:
                res.append(i)
            if len(res) == k:
                return res


