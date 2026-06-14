class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        l = 0

        while l < len(temperatures):
            r = l + 1
            count = 0
            while r < len(temperatures):
                if temperatures[l] < temperatures[r]:
                    count += 1
                    break
                
                count += 1

                if temperatures[l] >= temperatures[r] and r == len(temperatures) - 1:
                    count = 0
                r += 1

            output.append(count)
            l += 1
        
        return output
                
