class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [0] * 26
        for s in s1:
            counts1[ord(s) - ord('a')] += 1
        
        l = 0
        while l <= len(s2) - len(s1):
            counts2 = [0] * 26
            for r in range(l, len(s1) + l):
                counts2[ord(s2[r]) - ord('a')] += 1
            l += 1
            
            if counts1 == counts2:
                return True

        return False

