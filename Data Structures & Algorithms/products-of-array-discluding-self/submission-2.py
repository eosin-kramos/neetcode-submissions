#[1,1,2,8]
#[]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        products_left = [1]
        products_right = [1]

        for i in range(len(nums) - 1):
            products_left.append(products_left[i] * nums[i])
        
        for i in range(len(nums) - 1, 0, -1):
            products_right.append(products_right[(len(nums) - 1) - i] * nums[i])

        for i in range(len(products_left)):
            output.append(products_left[i] * products_right[(len(nums) - 1) - i])
        
        return output

