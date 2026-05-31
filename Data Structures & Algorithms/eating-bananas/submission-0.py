class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        
        while l <= r:
            time = 0
            k = l + (r - l) // 2
            for pile in piles:
                time += math.ceil(float(pile) / k)
            if time <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1
        return ans

