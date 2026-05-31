class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        l = 0
        
        if len(s) == 0:
            return 0
        while l < len(s):
            seen = {}
            seen[s[l]] = l
            count = 1
            r = l + 1
            while r < len(s):
                if s[r] in seen:
                    l = seen[s[r]]
                    break
                seen[s[r]] = r
                count += 1
                longest = max(count, longest)
                r += 1
            l += 1

        return longest

                    
