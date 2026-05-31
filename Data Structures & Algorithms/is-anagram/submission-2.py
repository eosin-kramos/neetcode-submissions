class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                value = s_dict.get(i)
                s_dict[i] = value + 1
            else: 
                s_dict[i] = 1
        for i in t:
            if i not in s_dict:
                return False
            elif i in t_dict:
                value = t_dict.get(i)
                t_dict[i] = value + 1
            else:
                t_dict[i] = 1
        for key in s_dict:
            if s_dict[key] != t_dict[key]:
                return False
        return True