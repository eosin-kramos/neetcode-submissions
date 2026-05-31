#Take nums[0] as min
#iterate through nums and put it in a set()
#while iterating through num, check nums[1] - 1 is in set
#if nums[i] - 1 is in set, check if that num - 1 is in set, then add to count 
#should use max to keep check of the most consecutive sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        output = 0

        for num in nums:
            seen.add(num)
            count = 1

            left_num = num - 1
            right_num = num + 1

            while left_num in seen:
                count += 1
                left_num -= 1
            
            while right_num in seen:
                count += 1
                right_num += 1
            
            output = max(output, count)
        
        return output
                
                