#Create an empty array with the size of nums
#Assuming that nums ir ordered, iterate through array
#Count how many times element appears
#when element is different, use count as iteration and element as value
#iterate through map in reverse and stop when we get k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = dict()
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        reversedFreqMap = sorted(freqMap.items(), key=lambda item: item[1], reverse=True)
        
        count = 0
        output = []
        for key, freq in reversedFreqMap:
            output.append(key)
            count += 1
            if count == k:
                break
        
        return output


            





        