class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen.pop(s[r]) + 1)
            seen[s[r]] = r
            longest = max(longest, r - l + 1)
        
        return longest


