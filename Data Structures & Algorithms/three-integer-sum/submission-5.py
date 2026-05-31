class Solution:
    #[-4,-1,-1,0,1,2]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    arr = [nums[i], nums[l], nums[r]]
                    if tuple(arr) not in seen:
                        res.append(arr)
                        seen.add(tuple(arr))
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1

        return res
