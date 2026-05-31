class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                l, r = 0, len(matrix[i]) - 1

                while l <= r:
                    m = l + (r - l) // 2
                    if matrix[i][m] < target:
                        l += 1
                    elif matrix[i][m] > target:
                        r -= 1
                    else:
                        return True
        return False
