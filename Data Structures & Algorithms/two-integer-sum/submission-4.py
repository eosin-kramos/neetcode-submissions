class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = dict()

        for i in range(len(nums)):
            j = target - nums[i]
            if nums[i] in sumMap:
                return [sumMap[nums[i]], i]
            else:
                sumMap[j] = i

        return [0, 0]