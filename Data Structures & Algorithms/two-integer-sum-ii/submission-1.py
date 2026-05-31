class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        while i < len(numbers):
            while j < len(numbers):
                if target - numbers[i] == numbers[j]:
                    return [i + 1, j + 1]
                j += 1
            i += 1
            j = i + 1

        return [i + 1, j + 1] 