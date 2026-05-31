class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            if i != 0 and num == nums[i - 1]:
                continue
            while left < right:
                toAdd = nums[left] + nums[right]
                if num + toAdd == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif num + toAdd > 0:
                    right -= 1
                elif num + toAdd < 0:
                    left += 1
        return ans

        