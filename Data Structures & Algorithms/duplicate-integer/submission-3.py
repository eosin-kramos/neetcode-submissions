class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        length = len(nums)
        i = 0 
        j = 1

        if length < 2:
            return False
        
        while i < length:
            while j < length:
                if nums[i] != nums[j]:
                    i += 1
                    j += 1
                else:
                    return True
            return False
        