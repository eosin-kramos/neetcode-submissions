#Questions: Is this already ordered? 
# iterate through array, and add it to map. Add to value by 1
# we create a bucket, with length being len(nums), 
# iterate through map, we use value as the index, and in that index, we add key
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        for key, value in frequency.items():
            bucket[value].append(key)
        
        count = 0
        result = []

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                count += 1
            if count == k:
                break

        
        return result


