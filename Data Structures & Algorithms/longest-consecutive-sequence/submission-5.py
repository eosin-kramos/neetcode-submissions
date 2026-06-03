#iterate through list, check if num is in set. 
#if num is in set, check if num - 1 and num + 1 is in map. If it is, add +1 to counter.
#have a max() 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        ans = 0
        for num in nums: 
            if num not in numSet:
                numSet.add(num)
                
            seq = 1
            before = num - 1
            after = num + 1

            while before in numSet:
                seq += 1
                before -= 1
            while after in numSet:
                seq += 1
                after +=1
            
            ans = max(ans, seq)
        
        return ans
                    

        