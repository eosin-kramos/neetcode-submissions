class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dictionary = {}
        for i in range(len(strs)):
            s_group = [strs[i]]
            if strs[i] in dictionary:
                continue
            else:
                dictionary[strs[i]] = True
            for j in range(i + 1, len(strs)):
                if self.checkAnagrams(strs[i], strs[j]):
                    dictionary[strs[j]] = True
                    s_group.append(strs[j])
            result.append(s_group)
        return result
    
    def checkAnagrams(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count [ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True
