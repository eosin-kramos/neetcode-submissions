class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += str(len(s)) + '#' + s
        
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        strings = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            strings.append(s[i:j])
            i = j 

        return strings